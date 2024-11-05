primeiro_numero = int(input("Give me the first number: "))
segundo_numero  = int(input("Give me the second number: "))


operacoes = ["+", "-", "*", "/"]

for x in range(4):
	if (operacoes[x] == "+"):
		resultado = primeiro_numero + segundo_numero
	elif (operacoes[x] == '-'):
		resultado = primeiro_numero - segundo_numero
	elif (operacoes[x] == '*'):
		resultado = primeiro_numero * segundo_numero
	elif (operacoes[x] == '/'):
		resultado = primeiro_numero / segundo_numero
	print(f'{primeiro_numero} {operacoes[x]} {segundo_numero} = {resultado}')
