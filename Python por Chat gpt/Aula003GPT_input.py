"""Vamos usar agora, o input()... que é a interação com o usuario"""


# nome = input("Digite seu nome:")
# print(f'Seu nome é: {nome}')

"""A variavel input, sempre retorna texto... ou seja... retorna Strings, para retornar valores inteiros, precisamos
fazer a conversão dos mesmo... por exemplo com int(input(''))"""

numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite outro numero: "))

print(f'Agora você verá esses dois numeros, na ordem digitada, com a realização das quatro operações básicas\n'
      f'SOMA: {numero_1 + numero_2}\n'
      f'SUBTRAÇÃO: {numero_1 - numero_2}\n'
      f'MULTIPLICAÇÃO: {numero_1 * numero_2}\n'
      f'DIVISÃO: {numero_1 / numero_2}')




