import os
import sys
import glob

args = sys.argv[1:] if len(sys.argv) > 1 else False
start_number = 1
new_name = "File_{:03d}{}"
pattern = '*'
extension = None

if args:
    if '-n' in args:
        index = args.index('-n') + 1
        if len(args) > index:
            nn = args[index].split('|')
            if nn[1].isnumeric():
                start_number = int(nn[1])
                new_name = nn[0] + '{:0' + str(len(nn[1])) + 'd}' + nn[2] + '{}'
    if '-f' in args:
        index = args.index('-f') + 1
        if len(args) > index:
            pattern = args[index]
    if '-e' in args:
        index = args.index('-e') + 1
        if len(args) > index:
            extension = args[index]
    if '-p' in args:
        index = args.index('-p') + 1
        if len(args) > index:
            directory = args[index]
            if os.path.exists(directory):
                os.chdir(directory)
                files = glob.glob(os.path.join(directory, pattern))
                if len(files):
                    for i, f in enumerate(files, start_number):
                        if extension:
                            extension = '.' + extension.replace('.', '')
                        else:
                            extension = os.path.splitext(f)[1]
                        nn = new_name.format(i, extension)
                        if os.path.isfile(nn):
                            print(" File: {} exists.".format(nn))
                        else:
                            os.rename(f, nn)
                    sys.exit(0)
                else:
                    print('\n No files: {}, in dir: "{}"\n'.format(pattern, directory))
            else:
                print("\n The path '{}' not exists!\n".format(directory))

print(' USAGE: \n    rename.py [-p "path/to/dir/contains/files"] [-f "FILTER"] [-n "name_prefix|start_number|name_suffix"] [-e "new_extension"]')
print(' -p : path to files')
print('      -p "c:/my_files"')
print(' -f : file filter')
print('      -f "*" - all files (default)')
print('      -f "*.txt" - all ".txt" files')
print('      -f "*[0-9]*" - all files contains numbers')
print('      -f "abc*.txt" - all ".txt" files starting with "abc"')
print('      -f ... and more regular expression patterns')
print(' -n : new name with start number format beatwen "|"')
print('      -n "File_|001|" (default)')
print('      -n "my_new_|00900|_file"')
print('      -n "|1|-image"')
print(' -e : change extension')
print('      -e "xxx"')
print(' example:')
print('      rename.py -p "c:/my_files" -f "*.txt" -n "new_name_|010|_file" -e "doc"')
print(' result:')
print('      new_name_010_file.doc')
print('      new_name_011_file.doc')
print('      new_name_012_file.doc')
print('      new_name_0.._file.doc')
