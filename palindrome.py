string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("The given string is a Palindrome")
else:
    print("The given string is Not a Palindrome")