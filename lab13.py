N = input()

print(N)
while N != "6174":
    C = int(''.join(sorted(N)))
    D = int(''.join(sorted(N, reverse=True)))

    N = str(D - C)
    print(N)