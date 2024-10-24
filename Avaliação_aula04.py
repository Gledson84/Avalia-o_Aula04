n1 = int(input('Digite o primeiro número de um intervalo: '))
n2 = int(input('Digite outro número para o fim do intervalo: '))
soma = 0
for i in range(n1, n2 + 1):
    if i % 2 == 0:
        soma += i
else:
    if soma == 0:
        print('Não há números pares no intervalo')
    else:   
        print(f' A soma dos números pares do intervalo é: {soma}.')
    