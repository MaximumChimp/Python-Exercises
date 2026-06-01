#PROBLEM: Write a script that opens an existing .txt file and counts the total number of words it contains.
#PURPOSE: This exercise teaches “Data Parsing.” In professional environments, you rarely work with data you typed into the code yourself; you almost always pull data from external sources. This script simulates basic text-mining techniques used to analyze documents or logs.

try:
    with open("sample.txt",'w') as file:
        file.write("Coding is the language of the future.")


    with open("sample.txt","r") as file:
        res = file.read().split()
        word_length = len(res)
        print(f"The file contains {word_length} words")

except FileNotFoundError:
    print("File does not exist!")