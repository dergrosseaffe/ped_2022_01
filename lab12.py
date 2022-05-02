N = int(input())

mapa = []
for _ in range(N):
    mapa.append(input().split())

commands = "NSLO*#"

portais = {}
for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        key = mapa[i][j]
        if (key not in commands):
            l = []
            if (key  in portais):
                l = portais[key]

            l.append((i, j))
            portais[key] = l

l, c = (int(i) for i in input().split())

next = mapa[l][c]
track = []
prev = ""
while next != '.' and next != '*' and next != '#' and c >= 0 and l >= 0:
    track.append((l, c, mapa[l][c]))
    if (mapa[l][c] in commands):
        mapa[l][c] = "." # mark pos as visited
    
    if next == 'N':
        l -= 1
    elif next == 'S':
        l += 1
    elif next == 'L':
        c += 1
    elif next == 'O':
        c -= 1
    else:
        pos = (l, c)
        p1, p2 = portais[next]
        if (p1 == pos):
            pos = p2
        else:
            pos = p1

        l, c = pos
        if prev == 'N':
            l -= 1
        elif prev == 'S':
            l += 1
        elif prev == 'L':
            c += 1
        elif prev == 'O':
            c -= 1
    
    prev = next
    next = mapa[l][c]

#print(track)
if (next == '*'):
    print("Jayce conseguiu chegar em Piltover")
else:
    print("Jayce nao conseguiu chegar em Piltover")
