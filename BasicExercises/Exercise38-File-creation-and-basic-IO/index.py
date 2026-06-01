#PROBLEM: Write a program that creates a new text file named notes.txt, writes three separate lines of text to it, and then reads that file back to display the contents in the console.
#PURPOSE: This exercise introduces “Persistent Storage.” Unlike variables that disappear when the program stops, files allow you to save data to the hard drive. Learning the open(), write(), and read() workflow is essential for building logging systems and saving user settings.

try:
    with open("notes.txt",'w') as file:
        file.write("Hello, this is my first note.\n")
        file.write("Python file handling is simple.\n")
        file.write("End of file.")

    with open("notes.txt",'r') as file:
        print(file.read())

except FileNotFoundError:
    print("File does not exist!")