n = int(input())

arr = list(map(int, input().split()))

unique_arr = []
seen = set()

for num in arr:
    if num not in seen:
        unique_arr.append(num)
        seen.add(num)

print(*unique_arr)