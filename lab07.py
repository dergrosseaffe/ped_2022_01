# Leitura do número de partidas
N = int(input())

p1_list = []
p2_list = []

for _ in range (N):
	p1_list.append([int(i) for i in input().split()])
	p2_list.append([int(i) for i in input().split()])

for e in range (N):
	P1 = p1_list[e]
	P2 = p2_list[e]

	# Processamento das possibilidades de encaixe

	# ordem normal
	best_candidate = 0
	for i in range (len(P2)-len(P1)+1):
		candidate = []
		for j in range(len(P1)):
			candidate.append(P1[j] + P2[i+j])

		max_candidate = max(candidate)
		pontos = 0
		for j in range(len(candidate)):
			if (max_candidate != candidate[j]):
				pontos += max_candidate - candidate[j]

		if (pontos == 0):
			best_candidate = (i, 0, "Normal")
			break
		else:
			if (best_candidate != 0):
				_, p, _ = best_candidate				
				if (pontos < p):
					best_candidate = (i, pontos, "Normal")
			else:
				best_candidate = (i, pontos, "Normal")

	# ordem inversa
	if (pontos != 0): # caso haja uma posição perfeita, ignora essa iteraçao
		for i in range (len(P2)-len(P1)+1):
			candidate = []
			for j in range(len(P1)):
				candidate.append(P1[len(P1)-1-j] + P2[i+j]) # len(P1)-1-j: pega posiçao invertida

			max_candidate = max(candidate)
			pontos = 0
			for j in range(len(candidate)):
				if (max_candidate != candidate[j]):
					pontos += max_candidate - candidate[j]

			if (pontos == 0):
				best_candidate = (i, 0, "Invertida")
				break
			else:
				if (best_candidate != 0):
					_, p, _ = best_candidate				
					if (pontos < p):
						best_candidate = (i, pontos, "Invertida")
				else:
					best_candidate = (i, pontos, "Invertida")
				
	P, R, S = best_candidate
	if (R == 0):
		print("Encaixe Perfeito!")
	else:
		print("Pontuacao:", R)
	print("Posicao de Encaixe:", P+1)
	print("Peca 1:", S)