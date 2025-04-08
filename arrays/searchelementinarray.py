def search_element(arr, x):
    
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n = int(input())

arr = list(map(int, input().split()))

x = int(input())

index = search_element(arr, x)

if index != -1:
    print(f"element found at {index}")
else:
    print(f"element not found in the array")