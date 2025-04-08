n = int(input())

arr = list(map(int, input().split()))

maximum = arr[0]

for i in arr:
    if i > maximum:
        maximum = i

print(maximum)

# Alternative one-liner:
# print(max(arr))