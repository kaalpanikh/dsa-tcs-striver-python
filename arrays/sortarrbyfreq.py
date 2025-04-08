def sort_by_frequency(arr):

    frequency = {}
    for i in arr:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1

    sorted_arr = sorted(arr, key= lambda x: ( -frequency[x],X))
            
    return sorted_arr

n = int(input())

arr = list(map(int, input().split()))

result = sort_by_frequency(arr)

print(*result)
