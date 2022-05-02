sexo = input()
peso = int(input())
altura = int(input())

if (sexo == 'M'):
	if (peso > 100):
		print("CX-102")
	else:
		if (altura <= 165):
			if (peso <= 70):
				print("LX-39")
			elif (peso <= 100):
				print("LX-40")
		elif (altura <= 190):
			if (peso <= 80):
				print("BW-02")
			else:
				print("MM-107")
		else:
			print("MM-107")
elif (sexo == 'F'):
	if (altura <= 140):
		print("LX-38")
	elif (altura <= 155):
		if (peso <= 90):
			print("BW-03")
		else:
			print("CX-101")
	elif (altura <= 170):
		if (peso <= 70):
			print("BW-03")
		else:
			print("CX-101")
	else:
		if (peso <= 90):
			print("BW-02")
		else:
			print("CX-102")