# csv wizard

[![pdm-managed](https://img.shields.io/badge/pdm-managed-blueviolet)](https://pdm.fming.dev)

***
## Import a CSV file by only giving the `CSVWizard` class a `string` containing the full name of the file without the *.csv* extension.
> `new_file = CSVWizard("my_file")`
***
## Handling decoding/encoding on a file.
All methods have an optional `encoding` argument.
If left empty, csv_wizard will attempt to automatically figure out the encoding, however, if a `UnicodeDecodeError` or `UnicodeEncodeError` error are raised, the encoding should be specified manually. 
The encoding parameter accepts strings.
```
> file1.get_row_count(encoding='utf-8') 
```
***
### Getting the characters that define the CSV file's layout. The `get_dialect` method.
Calling this method on a CSVWizard object returns it's dialect property.
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
### The `create()` method. An easier way to create a file, optionally specify a path.
The create method receives a string as required argument and it creates a new CSV file using that string. 

**Specifing a path to create the folder in**

Optionally, this method receives a *path* argument to specify a folder to create the file in. If this is not specified, the file will be created in the current directory.

For security reasons, when using this method in a client-facing app feature, it is recommended to limit the access to parent folders, to avoid the creation of files in vulnerable locations.

**Predefined paths**

There are three predefined global variables you can use: 
* `CURRENT_DIR` to get the current directory
* `CURRENT_PARENT_DIR` to get the parent directory of the current location
* `ABSOLUTE_PATH` to get the current absolute path

> `CSVWizard.create(name="new-file", path=CURRENT_PARENT_DIR)`
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
> `new_file.get_all_rows()` # `[['John', 'john@mail.com'], ['Anne', 'anne@mail.com]]`

This method accepts an optional argument called `row_structure`. `get_all_rows()` will always return a list containin all the rows. But, by default, all the rows themselves will be inside lists. With the `row_structure` argument you can specify that the rows be enclosed in tuples or sets. Dicts won't work.

> `get_all_rows(row_structure='tuple')` # `[('John', 'john@mail.com'), ('Anne', 'anne@mail.com)]`

> `get_all_rows(row_structure='set')` # `[{'John', 'john@mail.com'}, {'Anne', 'anne@mail.com}]`

> `get_all_rows(row_structure='dict')` # `['ERROR => Unsupported type: dict']`
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
### Getting the common rows between two instances of the CSVWizard class. The `find_common_rows()` method.
The `find_common_rows()` method compares the complete set of rows of two instances of the CSVWizard class and returns a list containing the rows that are present on both instances. One CSVWizard instance is the one the method is called on, the other one is passed as an argument.

This method internally calls the `get_all_rows()` method, and it specifically asks fora `row_structure` of tuples. This is done for performance reasons. So the rows will be returned in the format `[('col1', 'col2')]`.
```
file1 = CSVWizard('fileNo1')
file2 = CSVWizard('fileNo2')
file1.find_common_rows(file2)
> [(row1"), ("row2), ("row3)] 
``` 

***
### Finding the different rows between two instances of the CSVWizard class. The `find_different_rows()` method.
The `find_different_rows()` method compares the complete set of rows of two instances of the CSVWizard class and returns a list containing only the rows that are present on the firts file but not on the second. One CSVWizard instance is the one the method is called on, the other one is passed as an argument.

This method internally calls the `get_all_rows()` method, and it specifically asks fora `row_structure` of tuples. This is done for performance reasons. So the rows will be returned in the format `[('col1', 'col2')]`.
```
file1 = CSVWizard('fileNo1')
file2 = CSVWizard('fileNo2')
file1.find_different_rows(file2)
> [(row5"), ("row8), (row14)] 
```
```
file1 = CSVWizard('fileNo1')
file2 = CSVWizard('fileNo2')
file2.find_different_rows(file1)
> [(row1"), ("row4), (row34)] 
``` 

***
### Finding duplicate rows in a file. The `get_duplicates()` method.
When called on an instance of the CSVWizard class, this method will return a dictionary with the following format: `{'row_name': number_of occurrences}`
```
file1 = CSVWizard('fileNo1')
file1.get_duplicates()
> {"[' Alex ', 'alex@mail.com']": 2, "[' Adriana ', 'adriana@mail.com']": 5}
```
***
### In case there's empty rows in the file. The `delete_blanks()` method.
Executing this method on a `CSVWizard` instance will delete all blank rows from the CSV file. If there are many empty rows, the method may fail to delete them all in one run. If this happens, running it again should eventually delete them all.
***
# Usage warnings
1. When finding common rows or different rows between very large CSV files, keep in mind that execution time can be slower. To provide a frame of reference, while testing, comparing two files of a bit over 91000 rows, took between 1.7 and 2.1 seconds.
2. When comparing files, if they contain special characters like spanish *tildes* (eg. á, í), if the files' encoding differs, and on of them recognizes this characters but the other one doesn't, they will be read as different characters, thus being recognized as different rows.
3. When writing to an empty file (created manually or with the `create` method), an encoding must be specified.

***

# Testing instructions
The unit tests for this library is made with pytest. 

Every time the tests run, a CSV file is created from the test_file_backup.csv. The tests will run on that copy file. Once they are finished, the copy file will stay there, until you review it and manually delete it.

This is because some of the methods tested here make modifications on the test file that make it unusable for running tests again.