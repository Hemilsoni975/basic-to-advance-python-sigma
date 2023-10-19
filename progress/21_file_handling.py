# FILE HANDLING IS AN IMPORTANT PART OF ANY WEB APPLICATION
# FILE HANDLING IS A POWERFUL AND VERSATILE TOOL THAT CAN BE USED TO PERFORM A WIDE RANGE OF OPERATIONS.

# METHODS IN PYTHON FILE HANDLING:
# 01) read       : "r" - open file for only reading and it is the default mode if not mentioned.
# 02) write      : "w" - open file for only writing and also helps to create new file.
# 03) append     : "a" - add more content to file and also helps to create new file.
# 04) create     : "x" - creates file if not exist.
# 05) text       : "t" - helps to handle text files.
# 06) binary     : "b" - helps to handle binary files like jpg file, image file, exe files, pdf
# 07) close      : helps to close the existing file
# 08) readline   : returns file content
# 09) readlines  : returns list of file content
# 10) seek       : helps to change the current file positions
# 11) tell       : helps to print specific number of word in file
# 12) writelines : helps to write list of strings

#  open()   - to open txt or binary file
#           - takes two arguement : name of file and mode


print("--------------------write_function--------------------")

f = open("hello.txt", "w")
a = f.write("hello! hemil is best!!!  ")
f.close()

x = open("hello.txt", "w")
y = ['line1\n', 'line2\n', 'line3']
x.writelines(y)  # wrtielines() does not add newline character between the strings in sequence
x.close()

x = open("marks.txt", "w")
y = x.write("33,44,55\n66,77,88\n94,87,67")

print("--------------------read_function--------------------")

f = open("hello.txt", "r")
a = f.read()
print(a)
f.close()

x = open("marks.txt", "r")
i = 0
while True:
    i = i+1
    y = x.readline()
    if not y:
         break
    m1 = y.split(",")[0]
    m2 = y.split(",")[1]
    m3 = y.split(",")[2]
    print(f"Marks : {i} in maths {m1}")
    print(f"Marks : {i} in eng {m2}")
    print(f"Marks : {i} in guj {m3}")

x.close()


print("--------------------append_function--------------------")

f = open("hello.txt", "a")
a = f.write(" yeah yeah !!! ")
print(a)
f.close()

print("---------------------seek_function---------------------")
# seek() always allows you to move current position within file to a specific point.
# The position is specified in bytes and you can move either forward or backward from current position
with open("hello.txt", "r") as f:
    # print(type(f))
    f.seek(1)

    a = f.read(3)
    print(a)

print("---------------------tell_function---------------------")
#  function return current position within the files in bytes
with open("hello.txt", "r") as f:
    # print(type(f))
    f.seek(3)

    print(f.tell())
    a = f.read(10)
    print(a)

print("---------------------truncate_function---------------------")
# truncate() helps to keep specific nummber of words in txt file

with open("wow.txt", "w") as f:
    f.write("hemil you are good at coding!!!")
    f.truncate(10)

with open("wow.txt", "r") as f:
    print(f.read())
