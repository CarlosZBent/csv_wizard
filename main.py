from csv import reader, Sniffer

class FileReader:
    def __init__(self, source:str) -> None:
        # concat the .csv extension so it is not necessary when instatiating
        self.source = f'{source}.csv'

    def get_dialect(self):
        """
        Return the dialect from the file. The dialect contains properties 
        regarding the way the CSV file is structured.
        """
        with open(str(self.source)) as file:
            parser = reader(file)
            for row in parser:
                dialect = Sniffer().sniff(str(row))
                return dialect


    def get_headers(self, delimiter=','):
        """
        Return the headers on a file.
        """
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            for line in parser:
                return line

    def get_row_count(self, delimiter=','):
        """
        Get the amount of rows that the file contains, excluding the headers row.
        """
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            row_count = -1
            for line in parser:
                row_count += 1
            return row_count

    def get_all_rows(self, delimiter=','):
        """
        Get the content of all the rows in the file.
        """
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            row_container = []
            for line in parser:
                row_container.append(line)
            return row_container

    def slice(self, row_count:int, delimiter=','):
        """
        Divide the file's rows exactly in half if possible.
        If the total number of rows is odd the first half will contain one extra row.
        """
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            # original csv.reader object is not iterable
            # saving it's elements to this iterable gives greater flexibility
            parser_iterable = []
            row_container1 = []
            row_container2 = []
            half = row_count/2
            for line in parser:
                parser_iterable.append(line)
                # slice the parser_iterable after it's first item 
                # to leave the header row out of the result
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

    def divide(self, row_count:int, parts, delimiter=','):
         """
         Divide the file in the amount of parts indicated by the user.
         """
         with open(str(self.source)) as file:
             parser = reader(file, delimiter=str(delimiter))
             parser_iterable = []
             parts_size = row_count/parts
             for line in parser:
                 parser_iterable.append(line)
             parser_iterable.pop(0)
             def sever(list, n):
                 p = len(list) // n
                 if len(list)-p > 0:
                     return [list[:p]] + sever(list[p:], n-1)
                 else:
                     return [list]
             return sever(parser_iterable, parts)
            