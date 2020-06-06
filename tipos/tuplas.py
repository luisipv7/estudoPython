nomes = ('Ana', 'Bia', 'Gui', 'Ana')

print('Bia' in nomes)
print('bia' in nomes)

print(nomes[0])
print(nomes[1:2])
print(nomes[1:-1])
print(nomes[2:])
print(nomes[:-2])


print(type(nomes))
print(len(nomes))
print(nomes)

print('\n')

tupla = tuple()
tupla = ()
print(type(tupla))
# print(dir(tupla))
# print(help(tuple))
print(type(tupla))
tupla = ('um')
print(type(tupla))
tupla = ('um',)
print(type(tupla))
print(tupla[0])
# tupla[0]='novo'
cores = ('verde', 'amarelo', 'azul', 'branco')
print(cores[0])
print(cores[-1])
print(cores[1:])

print(cores.index('amarelo'))
print(cores.count('azul'))
