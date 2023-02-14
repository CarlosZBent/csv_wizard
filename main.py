from typing import Type, IO
from csv import reader, writer, Sniffer, Dialect
from chardet import detect


class FileReader:
    def __init__(self, source:str) -> None:
        # concat the .csv extension so it is not necessary when instatiating
        self.source = f'{source}.csv'

    def get_encoding(self):
        """
        Detect the encoding of the file
        """
        with open(self.source, 'rb') as file:
            line = file.readline()
            encoding = detect(line)['encoding']
            return encoding

    @staticmethod
    def create(name:str) -> None:
        """
        Create a new CSV file
        """
        with open(f'{str(name)}.csv', mode='x') as new_file:
            new_file.close()

    def get_dialect(self) -> Type[Dialect]:
        """
        Return the dialect from the file. The dialect contains properties 
        regarding the way the CSV file is structured.
        """
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            parser = reader(file)
            for row in parser:
                dialect = Sniffer().sniff(str(row))
                return dialect

    def __get_row_count(self) -> int:
        """
        Private method to get the amount of rows that 
        the file contains, excluding the headers row.
        """
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            try:
                parser = reader(file, delimiter=self.get_dialect().delimiter)
                row_count = -1
                for line in parser:
                    row_count += 1
                return row_count
            except UnicodeDecodeError as e:
                # if there is an error while decoding it will be catched
                # here because its the first method called by the methods
                # that perform operations on the file data
                print(f"The file contains encoding inconsistencies => {e}")

    def get_headers(self) -> list[str]:
        """
        Return the headers on a file.
        """
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            parser = reader(file, delimiter=self.get_dialect().delimiter)
            for line in parser:
                return line

    def get_all_rows(self) -> list:
        """
        Get the content of all the rows in the file.
        """
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            parser = reader(file, delimiter=self.get_dialect().delimiter)
            row_container = []
            for line in parser:
                row_container.append(line)
            return row_container

    def slice(self) -> dict:
        """
        Divide the file's rows exactly in half if possible.
        If the total number of rows is odd the first half will contain one extra row.
        """
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            parser = reader(file, delimiter=self.get_dialect().delimiter)
            # original csv.reader object is not iterable
            # saving it's elements to this iterable gives greater flexibility
            parser_iterable = []
            row_container1 = []
            row_container2 = []
            half = int(self.__get_row_count())/2
            for line in parser:
                parser_iterable.append(line)
                # slice the parser_iterable after it's first item 
                # to leave the header row out of the result
            # file.close()
            for item in parser_iterable[1:]:
                row_container1.append(item)
                if len(row_container1) > half:
                    break
                row_container2.append(item)
            master_container = {
                'First_Half': row_container1, 
                'Second_Half':row_container2
                }
            return master_container

    def divide(self, number_of_parts:int) -> list:
        """
        Divide the file in the amount of parts indicated by the user.
        """
        if type(number_of_parts) == float:
            raise TypeError("number_of_parts must be of type integer")
        with open(self.source, 'r', encoding=self.get_encoding()) as file:
            parser = reader(file, delimiter=self.get_dialect().delimiter)
            row_count = self.__get_row_count()
            if number_of_parts > row_count:
                raise IndexError('number_of_parts is greater than row_count')
            parser_iterable = []
            for line in parser:
                parser_iterable.append(line)
            parser_iterable.pop(0)
            def sever(list, n) -> list:
                p = len(list) // n
                if len(list)-p > 0:
                    return [list[:p]] + sever(list[p:], n-1)
                else:
                    return [list]
            return sever(parser_iterable, number_of_parts)

    def write_headers(self, headers_object:list[str]) -> None:
        """
        Write the headers to a file.
        The file can be empty or have data
        """
        rows = self.get_all_rows()
        rows.insert(0, headers_object)
        self.overwrite(rows)

    def overwrite(self, rows_object:list[list[str]]) -> None:
        """
        Write rows to a file (after truncating it)
        """
        with open(self.source, 'w', newline='') as file:
            file_writer = writer(file, dialect=self.get_dialect())
            file_writer.writerows(rows_object)
            file.close()

    def append_rows(self, rows_object:list[list[str]], append_on_top:bool=False) -> None:
        """
        Append rows at the end of a file 
        without deleting the existing rows
        """
        # read the existing and rows
        rows = self.get_all_rows()
        # append the new rows object to the existing ones
        for i in rows_object:
            if append_on_top:
                rows.insert(1, i)
            else:
                rows.append(i)
        # overwrite the resulting list into the file
        self.overwrite(rows)

    def find_common_rows(self, second_file) -> list[list[str]]:
        """
        Find the rows that are on one file but no the other
        """
        all_rows_1 = self.get_all_rows()
        all_rows_2 = second_file.get_all_rows()
        common_items = []
        for item in all_rows_1:
            if item in all_rows_2[1:]:
                common_items.append(item)
        return common_items

 # type: ignore
    def cleanup(self) -> None:
        """
        delete empty rows on the file
        """
        with open(self.source, 'r') as file:
            parser = reader(file, delimiter=self.get_dialect().delimiter)
            parser_iterable = []
            for line in parser:
                parser_iterable.append(line)
            for row in parser_iterable: 
                try:
                    while len(row) == 0:
                        index = parser_iterable.index(row)
                        parser_iterable.pop(index)
                except ValueError:
                        self.overwrite(parser_iterable)
