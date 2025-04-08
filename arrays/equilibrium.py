def find_equilibrium_index(arr):
    total_sum = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1

n = int(input())

arr = list(map(int, input().split()))

result = find_equilibrium_index(arr)

print(result)

