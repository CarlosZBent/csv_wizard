# CSV Divider
The CSV file is imported by only giving the `File` class a string containing the full name of the file

## The `get_dialect` method
Calling this method on a File object returns it's dialect property.
The dialect property contains:
* lineterminator
* quoting
* doublequote
* delimiter
* quotechar
* skipinitialspace
***
## The `get_headers` method
Returns only the first line on the CSV file, which is presumed to be the one containing the headers
***
## The `get_row_count` method
Returns the number of rows that the file contains, without taking into account the headers row
***
## The `get_all_rows` method
Returns a list containing the content of each individual row, including the header row. This is different from `get_header_count` in that it returns the complete content of the rows, not only how many there are.
***
## The `slice_in_half` method
Returns a dictionary with two key-value pairs. The keys are called "First_Half" and "Second_Half", and they respectively contain each half of the file's rows.
If the total nomber of rows is odd, it returns the first half will contain one more row to compensate.
Neither half will contain the header column. That must be obtained with the `get_headers` method. 