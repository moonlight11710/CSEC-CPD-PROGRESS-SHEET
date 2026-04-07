t = int(input())
for _ in range(t):
    s = input()

    s = s[::-1]
    new = ""

    for i in s:
        if i == "p":
            new+="q"
        elif i == "q":
            new+="p"
        else:
            new+=i
    print(new)
