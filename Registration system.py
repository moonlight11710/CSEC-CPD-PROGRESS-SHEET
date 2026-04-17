t = int(input())
dic = {}
for _ in range(t):
    word = input()
    if word in dic:
        dic[word]+=1
        print(word+str(dic[word]))

    else:
        dic[word]=0
        print("OK")    
