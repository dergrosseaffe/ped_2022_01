n = int(input())

i = 0
while (i < n):	
	inicial = int(input())

	x = maior = inicial
	pares = 0; impares = 0;
	while (x != 1):
		if (x % 2 == 0):
			pares += 1
			x //= 2
		else:
			impares += 1
			x = 3*x + 1

		if (x > maior): maior = x
	
	print(f"Valor inicial: {inicial}")
	print(f"Numeros Pares: {pares}")
	print(f"Numeros Impares: {impares+1}")
	print(f"Maior Numero: {maior}")
	i += 1