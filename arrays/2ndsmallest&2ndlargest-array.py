n = int(input())

arr = list(map(int, input().split()))

if n < 2:
    print("there should be at least 2 elements")

else:
    arr = sorted(set(arr))

    if len(arr) < 2:
        print("there should be at least 2 distinct elements")
    else:
        second_smallest = arr[1]
        second_largest = arr[-2]

        print(f"Second smallest: {second_smallest}")
        print(f"Second largest: {second_largest}")