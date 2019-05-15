
import csv
import sys

#looking for vowels

#vowels

vowels=['a','e','i','o','u']

fileInput =input("\Enter File Path: ")

filecontent =open(fileInput,'r').read()


print("\nCONTENTS OF THE FILE :")
print(fileContent)

print("\nLIST OF VOWELS AND ITS INDICES:")

for i in range(len(fileContent)):

    if filecontent[i] in vowels:

       print(fileContent[i],end=':')
       print(i,end=',')
sys.exit(o)
