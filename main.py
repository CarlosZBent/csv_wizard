from csv import reader, Sniffer

class File:
    def __init__(self, source:str) -> None:
        self.source = source

    def read_delimiter(self):
        """
        'Sniff' the delimiter in a file
        """
        with open(str(self.source)) as file:
            parser = reader(file)
            for row in parser:
                dialect = Sniffer().sniff(str(row))
                return dialect.delimiter        


    def read_headers(self, delimiter=','):
        '''
        Read all rows on a file
        '''
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            for line in parser:
                return line
                