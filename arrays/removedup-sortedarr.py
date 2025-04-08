n = int(input())

arr = list(map(int, input().split()))

unique_arr = []

for num in arr:
    if not unique_arr or unique_arr[-1] != num:
        unique_arr.append(num)

print(*unique_arr)