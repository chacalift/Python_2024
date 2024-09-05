""" Exercício 1
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
''' Primeira forma
numero_str = input('Digite um número inteiro: ')
try:
    numero_int = int(numero_str)
    par_impar = numero_int % 2 == 0
    resposta = 'ímpar'
    if par_impar:
        resposta = 'par'
    print(f'O número que você digitou {numero_int} é {resposta}')
except:
    print('Você não digitou um número inteiro!')
'''

''' Segunda forma :)
numero_str = input('Digite um número: ')
if numero_str.isdigit():
    numero_int = int(numero_str)
    par_impar = numero_int % 2 == 0
    resposta = 'ímpar'
    if par_impar:
        resposta = 'par'
    print(f'O número que você digitou {numero_int} é {resposta}')
else:
    print('Você não digitou um número inteiro!')
'''


"""Exercício 2
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.

entrada = input('Digite a hora em números interios: ')
try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa Noite!')
    else:
        print('Não é uma hora valida!')
except:
    print('Digite apenas numeros inteiros! ')        
"""


"""Exercício 3
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 


entrada = input('Digite seu primeiro nome: ')
nome =len(entrada)
if nome > 1:
    if nome <= 4:
        print('Seu nome é curto')
    elif nome >= 5 and nome <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Escreva mais de uma letra')
"""