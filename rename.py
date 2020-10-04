import os
import sys
import glob

args = sys.argv[1:] if len(sys.argv) > 1 else False
start_number = 1
new_name = "File_{:03d}{}"
pattern = '*'

if args:
    if '-n' in args:
        index = args.index('-n')
        if len(args) > index + 1:
            nn = args[index + 1].split('|')
            if nn[1].isnumeric():
                start_number = int(nn[1])
                new_name = nn[0] + '{:0' + str(len(nn[1])) + 'd}' + nn[2] + '{}'
    if '-f' in args:
        index = args.index('-f')
        if len(args) > index + 1:
            pattern = args[index + 1]
    if '-p' in args:
        index = args.index('-p')
        if len(args) > index + 1:
            directory = args[index + 1]
            if os.path.exists(directory):
                os.chdir(directory)
                files = glob.glob(os.path.join(directory, pattern))
                if len(files):
                    for i, f in enumerate(files, start_number):
                        nn = new_name.format(i, os.path.splitext(f)[1])
                        if os.path.isfile(nn):
                            print(" File: {} exists.".format(nn))
                        else:
                            os.rename(f, nn)
                    sys.exit(0)
                else:
                    print('\n No files: {}, in dir: "{}"\n'.format(pattern, directory))
            else:
                print("\n The path '{}' not exists!\n".format(directory))

print(' USAGE: \n    rename.py [-p "path/to/dir/contains/files"] [-f "FILTER"] [-n "name_prefix|start_number|name_suffix"]')
print(' FILTER: \n    * - all files (default)')
print('    *.txt - all ".txt" files')
print('    *[0-9]* - all files contains numbers')
print('    abc*.txt - all ".txt" files starting with "abc"')
print('    and more regular expression patterns...')
print(' example: \n    rename.py -p "c:/my_files" -f "*.txt" -n "new_name_|010|_file"')
print(' result:  \n    new_name_010_file.txt')
print('    new_name_011_file.txt')
print('    new_name_012_file.txt')
print('    new_name_0.._file.txt')
