def circular_rotation(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

n = int(input())

arr = list(map(int, input().split()))

k = int(input())

result = circular_rotation(arr, k)

print(*result)