from csv import reader, Sniffer

def open_file(file, column=None, delimiter=','):
    with open(str(file)) as opened_file:
        parser = reader(opened_file, delimiter=str(delimiter))
        for row in parser:
            if column != None:
                print(row[column])
            else:
                print(row)

open_file('employees_from_excel.csv')