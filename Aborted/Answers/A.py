from math import ceil
letters = [chr(ascii) for ascii in range(97, 105)]
v1, v2 = list(map(lambda x: (letters.index(x[0])+1, int(x[1])), input().split(" ")))
horiz = abs(v1[0]-v2[0])
vert = abs(v1[1]-v2[1])
steps = ceil(max(vert, horiz)/2)
print(steps)