'''
A tarifa de um táxi é por padrão R$ 4,00 mais R$ 0,50 para cada 200 metros rodados. Faça uma função chamada tarifa que retorne o
valor de uma corrida com base nos quilômetros rodados. A função deve ter os seguintes argumentos:
km: Obrigatório, quilômetros rodados (lembre-se que o preço é por 200 metros);
largada: Opcional, o valor da largada, por padrão 4.00;
valor: Opcional, O valor em reais para cada 200 metros rodados, por padrão 0.50.
'''


def tarifa(km, largada, valor):
    conversao = km * 1000
    adicional = (conversao / 200) * valor
    return largada + adicional


kms = float(input("Quantos Quilometros foram rodados: "))

padrao = str(input("O valor da largada será o Padrão?[S/N]: ").upper().strip())
if padrao[0] in "Ss":
    valor = 4
else:
    valor = float(input("Digite o Valor de largada: "))


custo = str(input("O valor da corrida será o Padrão?[S/N]: ").strip().upper())
if custo[0] in "Ss":
    taxa = 0.5
else:
    taxa = float(input("Digite o Valor pra cada 200 metros: "))


kms = tarifa(kms, valor, taxa)
print(f'O valor da sua tarifa foi de R${kms:.2f}')
