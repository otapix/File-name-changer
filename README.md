# File-name-changer
### USAGE:
    rename.py [-p "path/to/dir/contains/files"] [-f "FILTER"] [-n "name_prefix|start_number|name_suffix"]
### FILTER:
    * - all files (default)
    *.txt - all ".txt" files
    *[0-9]* - all files contains numbers
    abc*.txt - all ".txt" files starting with "abc"
    and more regular expression patterns...
### example:
    rename.py -p "c:/my_files" -f "*.txt" -n "new_name_|010|_file"
### result:
    new_name_010_file.txt
    new_name_011_file.txt
    new_name_012_file.txt
    new_name_0.._file.txt
