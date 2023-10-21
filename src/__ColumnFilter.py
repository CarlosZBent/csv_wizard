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

# class ColumnFilter:
#     def __init__(self, rows_object, column, value):
#         self.rows_object = rows_object
#         self.column = column
#         self.value = value


#     def contains(self):
#         matching_rows = []
#         for row in self.rows_object:
#             if self.value in row[self.column]:
#                 row_index = self.rows_object.index(row)
#                 matching_rows.append(row_index)

#         return matching_rows