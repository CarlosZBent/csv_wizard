"""
- contains and not contains are only useable for strings
- if the value is int, the column value will be converted to int, else they are treated as str
"""

class RowFilter:
    def __init__(self, rows_object: list[list[str]], column:int):
        self.rows_object = rows_object[1:]
        self.column = column


    def contains(self, value:str or list) -> list:
        """
        Returns index of all rows that contain `value`
        """
        # adding one to the index to compensate for 
        # not having the headers row in self.rows_object
        # that way when the indexes are returned, 
        # they coincide with the index of the row in the original unaltered rows_object
        if type(value) == str:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value in row[self.column]]
        elif type(value) == list:
            result_rows = []
            for row in self.rows_object:
                for elem in value:
                    if len(row) > 0:
                        if str(elem).lower() in row[self.column] or str(elem).upper() in row[self.column] or str(elem).capitalize() in row[self.column]:
                            result_rows.append(self.rows_object.index(row) + 1)
            return result_rows
        else:
            raise TypeError("contains() can only be applied to strings")


    def not_contains(self, value:str) -> list:
        """
        Returns index of all rows that don't contain `value`
        """
        if type(value) != str:
            raise TypeError("not_contains() can only be applied to strings")
        return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value not in row[self.column]]


    def is_equal_length(self, value:str) -> list:
        """
        Returns index of all rows that have the same length as `value`
        """
        if type(value) != str:
            raise TypeError("is_equal_length() can only be applied to strings")
        return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and len(value) == len(row[self.column])]


    def equals(self, value:int or str) -> list:
        """
        Returns index of all rows that are equal to `value`.
        """
        if type(value) == int:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value == int(row[self.column])]
        else: # it comes from a CSV file so it'll be a string by default
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value == row[self.column]]
    
    
    def not_equals(self, value:int or str) -> list:
        """
        Returns index of all rows that are not equal to `value`.
        """
        if type(value) == int:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value != int(row[self.column])]
        else: 
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value != row[self.column]]

    def is_larger(self, value:int or str) -> list:
        """
        If `value` is str, returns index of all rows that have a smaller length than `value`
        If `value` is int, returns index of all rows that are smaller than `value`
        """
        if type(value) == str:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and len(value) > len(row[self.column])]
        elif type(value) == int:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value > int(row[self.column])]
        else:
            raise TypeError("Value can't be compared. Must be `str` or `int`")
    
    
    def is_smaller(self, value:int or str) -> list:
        """
        If `value` is str, returns index of all rows that have a larger length than `value`
        If `value` is int, returns index of all rows that are larger than `value`
        """
        if type(value) == str:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and len(value) < len(row[self.column])]
        elif type(value) == int:
            return [self.rows_object.index(row) + 1 for row in self.rows_object if len(row) > 0 and value < int(row[self.column])]
        else:
            raise TypeError("Value can't be compared. Must be `str` or `int`")

