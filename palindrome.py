import sys

# Program to check if a string is a palindrome
# Usage:
# python palindrome.py madam

if len(sys.argv) == 2:
    text = sys.argv[1]  # Take input from system argument
    print("User provided input:")
else:
    print("No command-line input provided. Using default value:")
    text = "8"  # Default value

# Check palindrome
if text == text[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
