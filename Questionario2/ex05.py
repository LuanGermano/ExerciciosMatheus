"""Faça uma função chamada dias que retorne o número de dias que um dado mês, passado por argumento, contém. O mês é indicado
por um número entre 1 e 12, sendo 1 o mês de janeiro. A sua função deve também receber um argumento opcional chamado bissexto
de valor padrão False. Quando o valor do argumento bissexto é True considere fevereiro com 29 dias, senão 28.
"""


def dias(dias, bissexto=False):
    if dias in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif dias in [4, 6, 9, 11]:
        return 30
    else:
        if bissexto:
            return 29
        else:
            return 28

print(dias(1))
print(dias(2))
print(dias(2, True))
print(dias(3))
print(dias(3, True))
print(dias(1, True))
print(dias(1, False))
print(dias(3, False))
print(dias(4))
print(dias(3, True))
print(dias(3, False))
print(dias(5))
print(dias(6))