import sys
import os
from ExceptionClasses import InvalidFileError, FileNotFoundException
from color_constant import BOLD_RED
from main import main, help

if len(sys.argv) == 1:
    main()
    exit()
file_add = sys.argv[-1].strip()
if file_add == "details":
    print("Version: 0.1.2")
    print("Usage:")
    print("\tpython3 agraph <file name with extention .agt>")
    print("\t                    OR")
    print("\tpython agraph <file name with extension .agt>")
    print('python and python3 commands varies from system to system depending on python interpreter installed on it. ')
    help()
    exit()

if os.path.exists(file_add):
    fl = open(file_add, "r")
    if os.path.splitext(file_add)[-1] == ".agt":
        for cmd in fl:
            main(command="from file " + cmd.strip().lower())
    else:
        print(BOLD_RED)
        raise InvalidFileError('File must have an .agt extension')
else:
    print(BOLD_RED)
    raise FileNotFoundException('File not found')
