# CSV Divider
### Import a CSV file by only giving the `FileReader` class a `string` containing the full name of the file without the *.csv* part.
> `new_file = FileReader("my_file")`
***
## Getting the characters that define the CSV's layout. The `get_dialect` method.
Calling this method on a FileReader object returns it's dialect property.
The dialect property contains:
* lineterminator
* quoting
* doublequote
* delimiter
* quotechar
* skipinitialspace
> ``new_file.get_dialect().delimiter``

> ``new_file.get_dialect().lineterminator``

> ``new_file.get_dialect().quoting``
***
## Getting the headers row. The `get_headers` method.
Returns only the first line on the CSV file, which is presumed to be the one containing the headers.
> ``new_file.get_headers()`` # ["Name", "Email"]

***
## Getting the total number of rows in the CSV file. The `get_row_count` method.
Returns the number of rows that the file contains, without taking into account the headers row.
> `new_file.get_row_count()` # 45
***
## Getting the content of all rows in the CSV file. The `get_all_rows` method.
Returns a list containing the content of each individual row, including the header row. This is different from `get_header_count` in that it returns the complete content of the rows, not only how many there are.
> `new_file.get_all_rows()` # ``[['John', 'john@mail.com'], ['Anne', 'anne@mail.com]]``
***
## Slicing the CSV file in half. The `slice` method.
Returns a dictionary with two key-value pairs. The keys are called "First_Half" and "Second_Half", and they respectively contain each half of the file's rows.
If the total nomber of rows is odd, it returns the first half will contain one more row to compensate.

Neither half will contain the header column. That must be obtained with the `get_headers` method.
> `new_file.slice(45)` # ``{ 'First_Half':[], 'Second_Half':[] }``
***
## Dividing the CSV file in n number of parts. The `divide` method.
Returns a list containing smaller lists that in themselves contain equal amounts of elements (one for every part asked for in the method call). If the number of parts is not even, the amount of elements will be spread in the most equitative way possible.

The headers are not included on any of the returned lists. That must be obtained with the `get_headers` method.
> `new_file.divide(15, 5)` # `[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]`