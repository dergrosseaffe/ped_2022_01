pontos_vida_jinx = int(input())
pontos_vida_ekko = int(input())

for i in range(int(input())):
	golpe = int(input())
	if (pontos_vida_jinx > 0):
		if (pontos_vida_ekko > pontos_vida_jinx):
			golpe //= 2
		if (pontos_vida_ekko - golpe < 0):
			pontos_vida_ekko = 0;
		else:			
			pontos_vida_ekko -= golpe
		
for i in range(int(input())):
	golpe = int(input())
	if (pontos_vida_ekko > 0):
		if (pontos_vida_jinx > pontos_vida_ekko):
			golpe //= 2
		if (pontos_vida_jinx - golpe < 0):
			pontos_vida_jinx = 0;
		else:			
			pontos_vida_jinx -= golpe		
		
print(f"Vida da Jinx: {pontos_vida_jinx}")
print(f"Vida do Ekko: {pontos_vida_ekko}")

if (pontos_vida_jinx > pontos_vida_ekko):
	print("Jinx foi a vencedora da batalha")
elif (pontos_vida_ekko > pontos_vida_jinx):
	print("Ekko foi o vencedor da batalha")
else:
	print("A batalha terminou empatada")
		
