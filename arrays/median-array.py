n = int(input())

arr = list(map(int, input().split()))

arr.sort()

if n % 2 == 1:
    median = arr[n //2]
else:
    median = (arr[n //2 -1] + arr[n //2]) / 2


print(f"{median:.2f}" if isinstance(median, float) else median)