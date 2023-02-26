# CSV Divider
👷‍♀️ **Alpha stage software! WIP** 🚧

**Any suggestion or request is appreciated** 🙂
***
## Import a CSV file by only giving the `CSVParser` class a `string` containing the full name of the file without the *.csv* part.
> `new_file = CSVParser("my_file")`
***
## Handling decoding/encoding on a file.
All methods have an optional `encoding` argument.
If left empty, csv_parser will attempt to automatically figure out the encoding, however, if a `UnicodeDecodeError` or `UnicodeEncodeError` error are raised, the encoding should be specified manually. 
The encoding parameter accepts strings.
```
> file1.get_row_count(encoding='utf-8') 
```
***
### Getting the characters that define the CSV file's layout. The `get_dialect` method.
Calling this method on a CSVParser object returns it's dialect property.
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
### The `__create()` **private method**. And an easier way to create a file.
The create method receives a string as only argument and it creates a new CSV file using that string.

However, is the `CSVParser` class is instantiated using the name of a file that doesn't exist, it will create it and treat it as any other class instance.
***
### Getting the headers row. The `get_headers()` method.
Returns only the first line on the CSV file, which is presumed to be the one containing the headers.
> ``new_file.get_headers()`` # ["Name", "Email"]

***
### Getting the total number of rows in the CSV file. The `get_row_count()` method.
This method is used internally by other methods to be know how many rows a file has. It returns the number of rows that the file contains, without taking into account the headers row.
> `new_file.get_row_count()` # 45
***
### Getting the content of all rows in the CSV file. The `get_all_rows()` method.
Returns a list containing the content of each individual row, including the header row. This is different from `get_row_count()` in that it returns the complete content of the rows, not only how many there are.
> `new_file.get_all_rows()` # ``[['John', 'john@mail.com'], ['Anne', 'anne@mail.com]]``
***
### Slicing the CSV file in half. The `slice()` method.
Returns a dictionary with two key-value pairs. The keys are called "First_Half" and "Second_Half", and they respectively contain each half of the file's rows.
If the total nomber of rows is odd, the first half will contain one more row to compensate.

Neither half will contain the header column. That must be obtained with the `get_headers()` method.
> `new_file.slice()` # ``{ 'First_Half':[], 'Second_Half':[] }``
***
### Dividing the CSV file in n number of parts. The `divide()` method.
Returns a list containing smaller lists that in themselves contain equal amounts of elements (one for every part asked for in the method call). If the number of parts is not even, the amount of elements will be spread in the most equitative way possible.

The headers are not included on any of the returned lists. That must be obtained with the `get_headers()` method.
> `new_file.divide(3)` # `[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]`
***
### Adding a headers row to a file. The `write_headers()` method.
This method takes a list as the only argument. It expects a list with the same format as outputed by the `get_headers()` method.
It can be used on a file with data as well as an empty one.
***
### Overwriting the whole file with a new set of rows. The `overwrite()` method.
The `overwrite()` method taks as argument an object with a structure of `list[list[str]]`. It is the kind of object returned by the reading methods in the library like `slice()` or `divide()`.
The file is truncated (all the content is deleted) and the object is usedd to add new rows to the file.
***
### Adding new rows without deleting the existing ones. The `append_rows()` method.
It takes an argument of the same kind of object as the `overwrite()` method, that is, a `list[list[str]]`. It adds the rows in that object to the file below the already existing rows.
### Appending the set of rows at the top of the file.
The `append_rows()` method accepts an optional boolean argument called `append_on_top`. By default its set to `False`, which makes the method append the new rows **below** the existing rows. 

If set to `True`, the `append_on_top` argument makes the method place the new rows **on top** of the file, just below the headers, moving down the existing rows.

After the rows are appended, they will be seen in reverse order on the file. The last element on the `rows_object` will be on top at the file.
***
### Getting the common rows between two instances of the CSVParser class. The `find_common_rows()` method.
The `find_common_rows()` method compares the complete set of rows of two instances of the CSVParser class and returns a list containing the rows that are present on both instances. One CSVParser instance is the one the method is called on, the other one is passed as an argument.
```
file1 = CSVParser('fileNo1')
file2 = CSVParser('fileNo2')
file1.find_common_rows(file2)
> [["row1"], ["row2], ["row3]] 
```

***
### Finding the different rows between two instances of the CSVParser class. The `find_different_rows()` method.
The `find_different_rows()` method compares the complete set of rows of two instances of the CSVParser class and returns a list containing only the rows that are present on the firts file but not on the second. One CSVParser instance is the one the method is called on, the other one is passed as an argument.
```
file1 = CSVParser('fileNo1')
file2 = CSVParser('fileNo2')
file1.find_different_rows(file2)
> [["row5"], ["row8], ["row14]] 
```
```
file1 = CSVParser('fileNo1')
file2 = CSVParser('fileNo2')
file2.find_different_rows(file1)
> [["row1"], ["row4], ["row34]] 
```

***
### Finding duplicate rows in a file. The `get_duplicates()` method.
When called on an instance of the CSVParser class, this method will return a dictionary with the following format: `{'row_name': number_of occurrences}`
```
file1 = CSVParser('fileNo1')
file1.get_duplicates()
> {"[' Alex ', 'alex@mail.com']": 2, "[' Adriana ', 'adriana@mail.com']": 5}
```
***
### **UNSTABLE**. In case there's empty rows in the file. The `cleanup()` method.
Executing this method on a `CSVParser` instance will delete all blank rows from a CSV file.