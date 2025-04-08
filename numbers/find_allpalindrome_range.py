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

start = int(input())
end = int(input())

palindromes = [num for num in range(start, end + 1) if is_palindrome(num)]

if palindromes:
    print(*palindromes)
else:
    print("No Palindrome Numbers")