n = int(input())

arr = list(map(int, input().split()))

frequency = {}

for elements in arr:
    if elements in frequency:
        frequency[elements] += 1
    else:
        frequency[elements] = 1

for elements, count in frequency.items():
    print(f"{elements}: {count}")