from collections import defaultdict
n = int(input())
records = []
total = defaultdict(int)
for _ in range(n):
    name, score = input().split()
    score = int(score)
    records.append((name, score))
    total[name] += score
max_score = max(total.values())
current = defaultdict(int)
for name, score in records:
    current[name] += score
    if total[name] == max_score and current[name] >= max_score:
        print(name)
        break
