matriz = [['.' for _ in range(20)] for _ in range(20)]

linha, coluna = input().split()

linha = int(linha)
coluna = int(coluna)

matriz[linha][coluna] = "+"

value = input()
while value != "F":
    if (value == "A"):
        matriz[linha][coluna] = "#"
    else:
        v, s = value.split()
        s = int(s)
        for _ in range(s):
            if (v == "S"):
                linha += 1
            if (v == "N"):
                linha -= 1
            if (v == "L"):
                coluna += 1
            if (v == "O"):
                coluna -= 1
        
            if (matriz[linha][coluna] == "."):
                matriz[linha][coluna] = "+"

    value = input()

for linha in matriz:
    print(' '.join(linha))