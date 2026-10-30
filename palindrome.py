import sys

string = sys.argv[1]

reverse = string[::-1]

if string == reverse:
    print(string, "is a Palindrome")
else:
    print(string, "is not a Palindrome")


    