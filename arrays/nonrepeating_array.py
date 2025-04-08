# Read the size of the array
n = int(input())

# Read the array elements
arr = list(map(int, input().split()))

# Dictionary to store the frequency of each element
frequency = {}

# Count the frequency of each element
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Find and print all non-repeating elements
non_repeating_elements = [key for key, value in frequency.items() if value == 1]

if non_repeating_elements:
    print(*non_repeating_elements)
else:
    print("No non-repeating elements")