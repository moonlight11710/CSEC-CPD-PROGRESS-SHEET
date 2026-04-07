n=int(input())
word=input().lower()

var=set(word)

if len(var)<26:
    print("NO")
else:
    print("YES")
