def proximo_passo(next, x, y):
    if next == 'N':
        x -= 1
    elif next == 'S':
        x += 1
    elif next == 'L':
        y += 1
    elif next == 'O':
        y -= 1
    return (x, y)

def busca_caminho(M, x, y, previous):
    if (x < 0 or y < 0 or x >= len(mapa) or y >= len(mapa[0])):
        return False

    next = mapa[x][y]

    if (next == "#"):
        return False
        
    if (next == "*"):
        return True

    if (next == "."):
        commands = "NSLO"
        mapa[x][y] = '#'
        prex = x
        prey = y
        for command in commands:
            x, y = proximo_passo(command, prex, prey)
            previous = command
            trial = busca_caminho(mapa, x, y, previous)
            if (trial):
                return True

        return False
    
    if (next in "NSLO"):
        x, y = proximo_passo(next, x, y)
        previous = next
    else:
        pos = (x, y)
        p1, p2 = portais[next]
        if (p1 == pos):
            pos = p2
        else:
            pos = p1

        x, y = pos
        x, y = proximo_passo(previous, x, y)
    
    return busca_caminho(mapa, x, y, previous)

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

xi, yi = (int(i) for i in input().split())

if (busca_caminho(mapa, xi, yi, mapa[xi][yi])):
    print("Jayce conseguiu chegar em Piltover")
else:
    print("Jayce nao conseguiu chegar em Piltover")
