from os import system

system('cls')

preco = 0
novopreco = 0
desconto = 0

preco = float(input('Digite o preço do produto: '))
desconto = preco * 10 / 100
novopreco = preco - desconto

print('Preço do produto com desconto = ', novopreco)