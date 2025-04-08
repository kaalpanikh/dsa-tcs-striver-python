n = int(input())

arr = list(map(int, input().split()))

reversed_arr = arr[::-1]
print(*reversed_arr)  # Print reversed array (unpacked)

# Alternative methods:
# Method 2: Using reverse() method
# arr.reverse()
# print(*arr)

# Method 3: Using reversed() function
# print(*list(reversed(arr)))

# Method 4: Manual reversal with loop
# reversed_arr = []
# for i in range(len(arr)-1, -1, -1):
#     reversed_arr.append(arr[i])
# print(*reversed_arr)