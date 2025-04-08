def sort_according_to_order(arr1, arr2):
    
    ordered_dict = {value : index for index, value in enumerate(arr2)}

    sorted_arr = sorted(arr1, key= lambda x : ordered_dict.get(x, float('inf'), x))

    return sorted_arr

n = int(input())

arr1 = list(map(int, input().split()))

arr2 = list(map(int, input().split()))

result = sort_according_to_order(arr1, arr2)

print(*result)

