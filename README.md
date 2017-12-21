This Python script is a simplified version of the Linux 'ls' command.
It can :
- List files of a specified folder
- List files of a folder that begin with a given prefix
- List file modes and last modification dates


Type in command prompt :
python3 ls.py [-l] path

Examples :
Let us assume that a folder that has the path '/path/to/folder' contains two files named 'some_file' and 'another_file'.
The command :
python3 ls.py /path/to/folder/

Returns :
some_file
another_file

The command :
python3 ls.py /path/to/folder/som

Returns :
some_file

And the command :
python3 ls.py -l /path/to/folder

Returns :
rwxr--r--  2017-12-15 17:44 some_file
rwxr-xr-x  2017-12-15 17:44 another_file


To run unit tests please type in command prompt :
python3 unit_test.py