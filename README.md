# CSV Divider
### Import a CSV file by only giving the `FileReader` class a `string` containing the full name of the file without the *.csv* part.
> `new_file = FileReader("my_file")`
***
## Getting the characters that define the CSV file's layout. The `get_dialect` method.
Calling this method on a FileReader object returns it's dialect property.
The dialect property contains:
* lineterminator
* quoting
* doublequote
* delimiter
* quotechar
* skipinitialspace
> `new_file.get_dialect().delimiter`

> `new_file.get_dialect().lineterminator`

> `new_file.get_dialect().quoting`
***

## Opening the file. The **private method** `__open()`.
It returns a `TextIO` type object with the open CSV file in read mode.
***
## Creating a new CSV file. The `create()` method.
It receives a string as only argument and it creates a new CSV file using that string.
***
## Getting the headers row. The `get_headers()` method.
Returns only the first line on the CSV file, which is presumed to be the one containing the headers.
> ``new_file.get_headers()`` # ["Name", "Email"]

***
## Getting the total number of rows in the CSV file. The **private method** `__get_row_count()`.
This method is used internally by other methods to be know how many rows a file has. It returns the number of rows that the file contains, without taking into account the headers row.
> `new_file.__get_row_count()` # 45
***
## Getting the content of all rows in the CSV file. The `get_all_rows()` method.
Returns a list containing the content of each individual row, including the header row. This is different from `get_row_count()` in that it returns the complete content of the rows, not only how many there are.
> `new_file.get_all_rows()` # ``[['John', 'john@mail.com'], ['Anne', 'anne@mail.com]]``
***
## Slicing the CSV file in half. The `slice()` method.
Returns a dictionary with two key-value pairs. The keys are called "First_Half" and "Second_Half", and they respectively contain each half of the file's rows.
If the total nomber of rows is odd, the first half will contain one more row to compensate.

Neither half will contain the header column. That must be obtained with the `get_headers()` method.
> `new_file.slice()` # ``{ 'First_Half':[], 'Second_Half':[] }``
***
## Dividing the CSV file in n number of parts. The `divide()` method.
Returns a list containing smaller lists that in themselves contain equal amounts of elements (one for every part asked for in the method call). If the number of parts is not even, the amount of elements will be spread in the most equitative way possible.

The headers are not included on any of the returned lists. That must be obtained with the `get_headers()` method.
> `new_file.divide(3)` # `[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]`
***
## Deleting everything in the CSV file and adding new rows. The `overwrite()` method.
The `overwrite()` method taks as argument an object with a structure of `list[list[str]]`. It is the kind of object returned by the reading methods in the library like `slice()` or `divide()`.
The file is truncated (all the content is deleted) and the object is usedd to add new rows to the file.
***
## Adding new rows without deleting the existing ones. The `append_rows()` method.
It takes an argument of the same kind of object as the `overwrite()` method, that is, a `list[list[str]]`. It adds the rows in that object to the file below the already existing rows.
***
## In case there's empty rows in the file. The `cleanup()` method.
Executing this method on a `FileReader` instance will delete all blank rows from a CSV file.