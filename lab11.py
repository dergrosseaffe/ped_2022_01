from re import S


matriz = []
for _ in range(10):
    matriz.append(input().split())

letters = {}

for linha in matriz:
    for char in linha:
        if (char != "."):
            if (char not in letters):
                letters[char] = 0
            
            letters[char] += 1

N = int(input())

inputs = []

for _ in range(N):
    inputs.append(input())


for i in range(N):
    linha, coluna = inputs[i].split()

    linha = ord(linha) - ord('A')
    coluna = int(coluna) - 1

    if (matriz[linha][coluna] != "."):
        char = matriz[linha][coluna]
        letters[char] -= 1
        if (letters[char] > 0):
            print("atingiu o navio", char)
        else:
            print("afundou o navio", char)
        matriz[linha][coluna] == "."
    else:
        print("agua")