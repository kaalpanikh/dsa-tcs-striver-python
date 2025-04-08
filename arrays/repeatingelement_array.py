n = int(input())

arr = list(map(int, input().split()))

frequency = {}

for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

repeated_elements = [key for key,value in frequency.items() if value > 1]

if repeated_elements:
    print(*repeated_elements)
else:
    print("No repeating elements")