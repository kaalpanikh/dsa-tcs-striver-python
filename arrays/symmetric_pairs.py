n = int(input())

pairs = []
for _ in range(n):
    x, y = map(int, input().split())
    pairs.append((x,y))

pairs_dict = {}

symmetric_pairs = []

for x, y in pairs:
    if(y,x) in pairs_dict:
        symmetric_pairs.append((x,y))
    else:
        pairs_dict[(x,y)] = True

if symmetric_pairs:
    for pair in symmetric_pairs:
        print(pair[0], pair[1])
    else:
        print("No symmetric pairs found")

