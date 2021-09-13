'''Escreva uma função em Python 3 com o seguinte protótipo:
quadrado(x)
Sua função deve retornar o quadrado do número x.
O código que usa esta função é automaticamente atrelado pelo corretor.'''

def quadrado(x):
    return x*x


valor = int(input("Digite um valor: "))
quad = quadrado(valor)
print(f'O Numero {valor} tem seu quadrado de {quad}')