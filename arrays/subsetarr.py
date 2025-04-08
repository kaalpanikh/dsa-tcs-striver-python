def is_subset(arr1, arr2):
    
    set_arr1 = set(arr1)

    for element in arr2:
        if element not in set_arr1:
            return False
    return True

n1 = int(input())
arr1 = list(map(int, input().split()))
n2 = int(input())
arr2 = list(map(int, input().split()))

result = is_subset(arr1, arr2)

if result:
    print("Yes")
else:
    print("No")
