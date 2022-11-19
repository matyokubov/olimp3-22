a = input().split(" ")
a = list(map(lambda x: int(x), a))
ch = "abcdefghijklmnopqrstuvwxyz"
if sum(a)>=1 and sum(a)<=1000:
    res = ""
    i = 0
    for m in range(max(a)):
        for item in a:
            if item != 0:
                res += ch[i]
                a[i] = item-1
            i += 1
        i = 0
    print(res)
