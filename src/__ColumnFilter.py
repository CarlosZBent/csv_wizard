"""
class receives an object from get_all_rows.
it also receives the column name, operator and value to search.

def contains(self, rows_object, column, value):
    
    matching_rows = []
    
    for row in rows_object:
        if value in row[column]:
            row_index = rows_object.index(row)
            matching_rows.append(row_index)

    return matching_rows

"""

class ColumnFilter:
    def __init__(rows_object, column, value):
        rows_object = self.rows_object
        column = self.column
        value = self.value


    def contains(self, rows_object, column, value):
        matching_rows = []
        for row in rows_object:
            if value in row[column]:
                row_index = rows_object.index(row)
                matching_rows.append(row_index)

        return matching_rows