variavel = input('Digite: (+) para somar.\nDigite: (*) para multiplicar\nDigite: (/) para dividir\n:')

soma = int(input('Digite um número: '))
soma1 = int(input('Digite outro número: '))

if variavel == '+':
    valor = soma + soma1 
    print(valor)
elif variavel == '*':
    valor = soma * soma1
    print(valor)
elif variavel == '/':
    valor = soma / soma1
    print(valor)
else:
    print('Erro de varialvel. Digite novamente')