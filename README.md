# File-name-changer
#### USAGE:
    rename.py [-p "path/to/dir/contains/files"] [-f "FILTER"] [-n "name_prefix|start_number|name_suffix"] [-e "new_extension"]
#### -p : path to files
      -p "c:/my_files"
#### -f : file filter
      -f "*" - all files (default)
      -f "*.txt" - all ".txt" files
      -f "*[0-9]*" - all files contains numbers
      -f "abc*.txt" - all ".txt" files starting with "abc"
      -f ... and more regular expression patterns
#### -n : new name with start number format beatwen "|"
      -n "my_new_|00100|_file"
      -n "file |9|"
      -n "|001|-image"
#### -e : change extension
      -e "xxx"
#### example:
      rename.py -p "c:/my_files" -f "*.txt" -n "new_name_|010|_file" -e "doc"
#### result:
      new_name_010_file.doc
      new_name_011_file.doc
      new_name_012_file.doc
      new_name_0.._file.doc
