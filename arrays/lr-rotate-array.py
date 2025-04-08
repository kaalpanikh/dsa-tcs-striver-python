def left_rotate(arr,k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

def right_rotate(arr,k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

n = int(input())

arr = list(map(int, input().split()))

k = int(input())

left_rotated = left_rotate(arr, k)
right_rotated = right_rotate(arr, k)

print("Left Rotated:", *left_rotated)
print("Right Rotated:", *right_rotated)

