import sys

# Program to check if a string is a palindrome
# Usage:
# python palindrome.py madam

if len(sys.argv) == 2:
    text = sys.argv[1]  # Take input from system argument
    print("User provided input:")
else:
    print("No command-line input provided. Using manual input:")
    text = input("Enter a string: ")  # Manual input when no argument is passed

# Check palindrome
if text == text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
