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

## The `get_headers` method
The `get_headers` method returns only the first line on the CSV file, which is presumed to be the one containing the headers

## The `get_row_count` method
The `get_row_count` method returns the number of rows that the file contains, without taking into account the headers row