"""Dessa vez vamos usar FOR e WHILE!

Usamos FOR quando sabemos quantas repetições vamos ter
While quando existe uma condição de parada!"""

soma = 0

for i in range(1, 6):
    numero = int(input(f'Digite o numero {i}: '))
    soma += numero  # mesmo que soma = soma + numero
print(f"A soma total é: {soma}")

soma = 0

contador = 1
while contador < 6:
    numero = int(input(f'Digite o numero {contador}: '))
    soma += numero  # mesmo que soma = soma + numero
    contador += 1  # mesmo que contador = contador + 1
print(f"A soma total é: {soma}")
