from csv import reader, Sniffer

class File:
    def __init__(self, source:str) -> None:
        self.source = source

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
