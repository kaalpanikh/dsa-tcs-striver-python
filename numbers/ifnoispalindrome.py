# Function to check if a number is palindrome
def is_palindrome(num):
    # Handle negative numbers (negative numbers are not palindromes)
    if num < 0:
        return False

    # Store the original number
    original = num
    reversed_num = 0

    # Reverse the number
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    # Compare original and reversed number
    return original == reversed_num

# Input: Read the number
num = int(input())

# Check if the number is palindrome and print the result
if is_palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")