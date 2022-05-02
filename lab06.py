candidatos = int(input())

nomes = []
votos = []

nomes = [input() for i in range(candidatos)]
votos = [int(input()) for i in range(candidatos)]

votos.append(int(input()))
votos.append(int(input()))

total_votos = sum(votos)
total_validos = sum(votos[0:-2])

votos_calculo = votos.copy()

primeiro = votos.index(max(votos_calculo[0:-2]))
votos_calculo.pop(primeiro)
segundo = votos.index(max(votos_calculo[0:-2]))

if (votos[primeiro] >= total_validos//2):
	print(f"{nomes[primeiro]} foi o vencedor da eleição")
else:
	print(f"Haverá segundo turno entre:\n{nomes[primeiro]}\n{nomes[segundo]}")

print(f"Total de votos: {total_votos}")
print(f"Votos válidos: {total_validos}")