"""Faça uma função chamada mediana que calcula e retorna a mediana de três valores passados por argumento. O valor da mediana é o
valor do meio de um conjunto de valores quando eles estão ordenados."""


def mediana(a=0, b=0, c=0):
    l = [a, b, c]
    l.sort()
    return l[1]


print(mediana(1,2))
print(mediana(2,3,1))
print(mediana(0,1,2))
print(mediana(4,3,6))
print(mediana(9, 10, 1))
print(mediana(10, 9, 11))
print(mediana(11, 10))
print(mediana(1, 9, 10))
print(mediana(4,3,6))