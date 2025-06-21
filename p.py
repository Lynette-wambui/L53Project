# write in the file using with()function
with open('file.txt', 'w') as file:
    file.write("Hello...This is my first file.")
    file.write("\n")
    file.write("I am learning operations in file in python.")
file.close()

# split file into words
with open('file.txt', 'r') as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print (word)
file.close()





#create a new file
new_file = open('file.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_mainfile exists or not..")
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")

#create a new file if it doesn't 
my_file = open("main.txt", "w")
my_file.write("Hi! My name is Lynette Wambui.")
my_file.close()





# the output file
outputFile = open('updatedfile.txt', "w")

# reading the input file
inputFile = open('file.txt', "r")

# holds lines already seen
lines_seen_so_far = set()
print("Eliminating duplicate lines.....")
# iterating each line in the file
for line in inputFile:

    #checking if line is unique
    if line not in lines_seen_so_far:
        outputFile.write(line)
        lines_seen_so_far.add(line)

# closing files
inputFile.close()
outputFile.close()

print("Done! Unique lines have been written to updatedfile.txt.")



# Program to merge two files into a third file

# Reading data from file1
with open('codingal.txt') as fp:
    data1 = fp.read()

# Reading data from file2
with open('sample.txt') as fp:
    data2 = fp.read()

# Merging 2 files
# To add the data of file2
# from next line
data1 += "\n"
data1 += data2
print("Merging two files...")
with open('MergedFile.txt', 'w') as fp:
    fp.write(data1)
        