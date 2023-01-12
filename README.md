# CSV Divider
The CSV file is imported by only giving the `File` class a string containing the full name of the file

## `get_dialect` method
Calling this method on a File object returns it's dialect property.
The dialect property contains:
* lineterminator
* quoting
* doublequote
* delimiter
* quotechar
* skipinitialspace

## `get_headers` method
The `get_headers` method returns only the first line on the CSV file, which is presumed to be the one containing the headers