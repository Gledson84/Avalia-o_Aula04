n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = 0
for i in range(n1, n2):
    if i % 2 == 0:
        soma += i
        print(soma)
else:
    print('Não há números pares no  intervalo')

    