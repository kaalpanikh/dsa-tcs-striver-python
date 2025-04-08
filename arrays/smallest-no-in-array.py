n = int(input())

arr = list(map(int, input().split()))

minimum = arr[0]

for i in arr:
    if i < minimum:
        minimum = i

print(minimum)