#Exercício IMC 2
nome = 'Daniel Feuser'
altura = 1.83
peso = 69
imc = int(peso / (altura * altura))
# "f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)