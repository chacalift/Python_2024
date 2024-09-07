''' Exercício
***Calculadora com while
1 - Pedir o primeiro e o segundo numero para o usuário
2 - Pedir um operador (+,-,*,/)
'''
while True:
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite o operador (+, -, *, /): ')

    # Validação dos números
    try:
        primeiro_numero = float(num1)
        segundo_numero = float(num2)
    except ValueError:
        print("Por favor, digite números válidos.")
        continue  # Volta ao início do loop se houver erro

    # Operações com base no operador
    if operador == '+':
        soma = primeiro_numero + segundo_numero
        print(f'Resultado: {soma}')
    elif operador == '-':
        subtracao = primeiro_numero - segundo_numero
        print(f'Resultado: {subtracao}')
    elif operador == '*':
        multiplicacao = primeiro_numero * segundo_numero
        print(f'Resultado: {multiplicacao}')
    elif operador == '/':
        if segundo_numero == 0:
            print("Erro: divisão por zero!")
        else:
            divisao = primeiro_numero / segundo_numero
            print(f'Resultado: {divisao}')
    else:
        print("Operador inválido! Use +, -, * ou /.")

    # Verificar se o usuário quer sair
    sair = input('Quer sair? [s]im para encerrar: ').lower().startswith('s')
    if sair:
        break
