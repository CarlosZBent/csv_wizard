import os
from csv import Dialect, Sniffer, reader, writer
from dataclasses import dataclass
from typing import Type

from chardet import detect

CURRENT_DIR = os.path.realpath(".")
CURRENT_PARENT_DIR = os.path.realpath("..")
ABSOLUTE_PATH = os.path.abspath(".")


@dataclass
class CSVWizard:
    source: str
    path: str = None

    def __post_init__(self) -> None:
        # concat the .csv extension so it is not necessary when instatiating
        if self.path:
            self.source = f"{os.path.join(self.path, self.source)}.csv"
        else:
            self.source = f"{self.source}.csv"

    def get_encoding(self) -> str:
        """
        Detect the encoding of the file
        """

        with open(self.source, "rb") as file:
            line = file.readline()
            encoding = detect(line)["encoding"]
            if encoding == None:
                raise LookupError("Encoding=None | Is the file empty?")
            else:
                return str(encoding)

    @staticmethod
    def create(name: str, path: str = os.path.realpath(".")) -> None:
        """
        Create a new CSV file. Optionally provide a path for the new file.
        """
        try:
            with open(
                os.path.join(f"{path}", f"{str(name)}.csv"), mode="x"
            ) as new_file:
                new_file.close()
            print("\n-------------")
            print(f">>>> File <{name}.csv> created at <{path}>")
            print("-------------\n")
        except FileNotFoundError:
            print("\n-------------")
            print("Specified folder does not exist.\nCreating folder...")
            os.makedirs(path)
            with open(
                os.path.join(f"{path}", f"{str(name)}.csv"), mode="x"
            ) as new_file:
                new_file.close()
            print(f"\n>>>> File <{name}.csv> created at <{path}>")
            print("-------------\n")
        except FileExistsError:
            print("\n-------------")
            print(f"File <{name}.csv> already exists in the specified folder")
            print("-------------\n")

    def get_dialect(self, encoding: str = "") -> Type[Dialect]:
        """
        Return the dialect from the file. The dialect contains properties
        regarding the way the CSV file is structured.
        """
        print("encoding: ", encoding)
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(file)
            for row in parser:
                dialect = Sniffer().sniff(str(row))
                return dialect

    def get_row_count(self, encoding: str = "") -> int:
        """
        Method to get the amount of rows that
        the file contains, excluding the headers row.
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            row_count = -1
            for line in parser:
                row_count += 1
            return row_count

    def get_headers(self, encoding: str = "") -> list[str]:
        """
        Return the headers on a file.
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            for line in parser:
                return line

    def get_all_rows(self, encoding: str = "", row_structure="list") -> list:
        """
        Get the content of all the rows in the file.
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            row_container = []
            if row_structure == "set":
                for line in parser:
                    row_container.append(set(line))
            elif row_structure == "tuple":
                for line in parser:
                    row_container.append(tuple(line))
            elif row_structure == "dict":
                return ["ERROR => Unsupported type: dict"]
            else:
                for line in parser:
                    row_container.append(line)
            return row_container

    def slice(self, encoding: str = "") -> dict:
        """
        Divide the file's rows exactly in half if possible.
        If the total number of rows is odd the first half will contain one extra row.
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            # original csv.reader object is not iterable
            # saving it's elements to this iterable gives greater flexibility
            parser_iterable = []
            row_container1 = []
            row_container2 = []
            half = int(self.get_row_count(encoding=encoding)) / 2
            for line in parser:
                parser_iterable.append(line)
                # slice the parser_iterable after it's first item
                # to leave the header row out of the result
            row_container1 = parser_iterable[1 : int(half)]
            row_container2 = parser_iterable[int(half) :]

            master_container = {
                "First_Half": row_container1,
                "Second_Half": row_container2,
            }
            return master_container

    def divide(self, number_of_parts: int, encoding: str = "") -> list:
        """
        Divide the file in the amount of parts indicated by the user.
        """
        if type(number_of_parts) == float:
            raise TypeError("number_of_parts must be of type integer")
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            row_count = self.get_row_count(encoding=encoding)
            if number_of_parts > row_count:
                raise IndexError("number_of_parts is greater than row_count")
            parser_iterable = []
            for line in parser:
                parser_iterable.append(line)
            parser_iterable.pop(0)

            def sever(list, n) -> list:
                p = len(list) // n
                if len(list) - p > 0:
                    return [list[:p]] + sever(list[p:], n - 1)
                else:
                    return [list]

            return sever(parser_iterable, number_of_parts)

    def write_headers(self, headers_object: list[str], encoding: str = "") -> None:
        """
        Write the headers to a file.
        The file can be empty or have data
        """
        if not encoding:
            encoding = self.get_encoding()
        rows = self.get_all_rows(encoding=encoding)
        rows.insert(0, headers_object)
        self.overwrite(rows, encoding=encoding)

    def overwrite(self, rows_object: list[list[str]], encoding: str = "") -> None:
        """
        Write rows to a file (after truncating it)
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "w", newline="", encoding=encoding) as file:
            file_writer = writer(file, dialect=self.get_dialect(encoding=encoding))
            file_writer.writerows(rows_object)
            file.close()

    def append_rows(
        self,
        rows_object: list[list[str]],
        append_on_top: bool = False,
        encoding: str = "",
    ) -> None:
        """
        Append rows at the end of a file
        without deleting the existing rows
        """
        if not encoding:
            encoding = self.get_encoding()
        # read the existing and rows
        rows = self.get_all_rows(encoding=encoding)
        # append the new rows object to the existing ones
        for i in rows_object:
            if append_on_top:
                rows.insert(1, i)
            else:
                rows.append(i)
        # overwrite the resulting list into the file
        self.overwrite(rows, encoding=encoding)

    def find_common_rows(
        self, second_file: "CSVWizard", encoding: str = ""
    ) -> list[list[str]]:
        """
        Find the rows that are on both files
        """
        if not encoding:
            encoding = self.get_encoding()
        all_rows_1 = set(self.get_all_rows(encoding=encoding, row_structure="tuple"))
        all_rows_2 = set(
            second_file.get_all_rows(encoding=encoding, row_structure="tuple")
        )
        common_rows = list(all_rows_1.intersection(all_rows_2))

        return common_rows

    def find_different_rows(
        self, second_file: "CSVWizard", encoding: str = ""
    ) -> list[list[str]]:
        """
        Returns the rows that are on the first file
        but not on the second one
        """
        if not encoding:
            encoding = self.get_encoding()
        all_rows_1 = set(self.get_all_rows(encoding=encoding, row_structure="tuple"))
        all_rows_2 = set(
            second_file.get_all_rows(encoding=encoding, row_structure="tuple")
        )
        diff_rows = list(all_rows_1.difference(all_rows_2))

        return diff_rows

    def get_duplicates(self, encoding: str = "") -> dict:
        """
        Find duplicate rows and the number of occurrences for each one
        """
        if not encoding:
            encoding = self.get_encoding()
        rows = self.get_all_rows(encoding=encoding)

        dups_dict = {}

        for i in rows:
            # iterate over the file's rows
            if rows.count(i) > 1 and i != []:
                # if the count for this element is > 1 is duplicated
                # add that element and it's count to the dict
                dups_dict.update({str(i): rows.count(i)})

        if len(dups_dict) > 0:
            return dups_dict
        else:
            return {"Result": "No duplicate rows in the file"}

    def delete_blanks(self, encoding: str = "") -> None:
        """
        delete blank rows from file
        """
        if not encoding:
            encoding = self.get_encoding()
        with open(self.source, "r", encoding=encoding) as file:
            parser = reader(
                file, delimiter=self.get_dialect(encoding=encoding).delimiter
            )
            parser_iterable = []
            for line in parser:
                parser_iterable.append(line)
            for row in parser_iterable:
                try:
                    while all("" == i or i.isspace() for i in row):
                        # while a row has no characters or all its characters are whitespaces
                        index = parser_iterable.index(row)
                        parser_iterable.pop(index)
                except ValueError:
                    self.overwrite(parser_iterable)
