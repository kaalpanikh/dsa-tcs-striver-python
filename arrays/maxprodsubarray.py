def max_product_subarray(arr):
    n = len(arr)
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]

    for i in range(1, n):
        if arr[i]<0:
            max_product, min_product = min_product, max_product

            max_product = max(arr[i], max_product*arr[i])
            min_product = min(arr[i], min_product*arr[i])
            result = max(result, max_product)

    return result

n = int(input())


arr = list(map(int, input().split()))

print(max_product_subarray(arr))
