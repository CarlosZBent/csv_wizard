from csv import reader, Sniffer

def open_file(file, delimiter, column):
    with open(str(file)) as opened_file:
        parser = reader(opened_file, delimiter=str(delimiter))
        for row in parser:
            # print(Sniffer.sniff(sample=str(row)))
            print(row[column])

open_file('employees_from_excel.csv', ';', 1)