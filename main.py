from csv import reader, Sniffer

class File:
    def __init__(self, source:str) -> None:
        self.source = source

    def read_delimiter(self):
        with open(str(self.source)) as file:
            parser = reader(file)
            for row in parser:
                dialect = Sniffer().sniff(str(row))
                return dialect.delimiter        


    def read_rows(self, column=None, delimiter=','):
        '''
        Read all rows on a file
        '''
        with open(str(self.source)) as file:
            parser = reader(file, delimiter=str(delimiter))
            for row in parser:
                if column != None:
                    return row[column]
                else:
                    return row


emps = File('employees.csv')
print(emps.read_delimiter())