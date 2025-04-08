n = int(input())

arr = list(map(int, input.split()))

arr.sort()

mid = (n +1) // 2

result = arr[:mid] + arr[mid:][::-1]

print(*result)