def rotate_array(arr,k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]
    
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

result = rotate_array(arr, k)
print(*result)