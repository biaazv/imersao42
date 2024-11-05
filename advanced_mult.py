numero = 0
i = 0

while (numero < 11):
	print(f" \n Tabuada de {numero}: ", end='')
	while (i < 11):
		print(f" {i * numero}", end='')
		i+=1
	numero+=1	
	i = 0
