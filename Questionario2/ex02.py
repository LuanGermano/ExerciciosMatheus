'''Escreva uma função em Python 3 com o seguinte protótipo:
maior(a, b)
Sua função deve retornar o maior valor entre a e b.
Sua função deve retornar o valor mesmo quando a for igual a b.
'''

def maior(a,b):
    if a > b:
        return a
    else:
        return b


valor1 = float(input("Digite um Valor: "))
valor2 = float(input("Digite um Valor: "))
mai = maior(valor1, valor2)
print(f'O Maior Valor entre {valor1:.0f} e {valor2:.0f} é o {mai:.0f}')
