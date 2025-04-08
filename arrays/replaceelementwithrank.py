def replace_with_rank(arr):
    
    sorted_arr = sorted(set(arr))

    ranked_dict = {value: rank + 1 for rank, value in enumerate(sorted_arr)}

    result = [ranked_dict[num] for num in arr]

    return result

n = int(input())

arr = list(map(int, input().split()))

result = replace_with_rank(arr)

print(*result)

