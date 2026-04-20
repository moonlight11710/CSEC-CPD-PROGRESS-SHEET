from collections import defaultdict
t = int(input())
for _ in range(t):
    dict1 = defaultdict(int)
    count = 0
    n = int(input())
    lis = list(map(int, input().split()))

    for i in range(n):
        a = lis[i] - i
        count += dict1[a]
        dict1[a] += 1
    print(count)
   
