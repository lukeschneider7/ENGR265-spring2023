from os.path import exists

# Find Week2-formulas using relative file path
relative_path = "../../Module 1/0 - Lecture Examples/week2-formulas.py"
if exists(relative_path):
    print("Can see week 2 formulas!")
else:
    print("Cannot locate week2-formulas at path: ", relative_path)

# Check to see another module 6 file via relative path
relative_path = "./debugging-example.py"
if exists(relative_path):
    print("Can see debugger examples!")
else:
    print("Cannot locate debugging - examples via path: ", relative_path)

# Check to see fibo.py using absolute filepath
absolute_path = "/Users/luke/Documents/GitHub/ENGR265-spring2023/Module 6 - SWE/0 - Lecture Examples/fibo.py"
if exists(absolute_path):
    print("Can see absolute file path to fibo.ph!")
else:
    print("Cannot locate absolute file path to fibo.py: ", absolute_path)

# check to see if we can see "train_data.txt" via relative path
relative_path = "train_data.txt"
if exists(relative_path):
    print("Can see train_data!")
else:
    print("Cannot locate train_data at path: ", relative_path)

# check if we can see "test_data.txt" via relative path option #1
relative_path = "subfolder/test_data.txt"
if exists(relative_path):
    print("Can see test_data!")
else:
    print("Cannot locate test_data at path: ", relative_path)

# check if we can see "test_data.txt" via relative path option #2
relative_path = "./subfolder/test_data.txt"
if exists(relative_path):
    print("Can see test_data!")
else:
    print("Cannot locate test_data at path: ", relative_path)

# check an absolute path based upon Windows notation
absolute_path = r"C:\Users\Jason Work\Documents\GitHub\ENGR298-2022-Private\lecture-examples\week8-file-paths\train_data.txt"
if exists(absolute_path):
    print("Can see train_data!")
else:
    print("Cannot locate train_data at path: ", absolute_path)

