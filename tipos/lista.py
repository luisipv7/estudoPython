nums = [1, 2, 3]
print(type(nums))

nums.append(3)
print(len(nums))

nums[3] = 100
nums.insert(0, -2000)

print(nums[4])

print(nums[-1])

print(nums)

print("\n")
lista = []

# print(type(lista))
# print(help(list))
# print(dir(lista))
# print(len(lista))
lista.append(1)
print(lista)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = [1, 5, 'Bia', 'Ana']
print(nova_lista)
nova_lista.remove(5)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

print("\n")
lista = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista.index('Guilherme'))
# print(lista.index(42))
print(lista[2])
print(1 in lista)
print('Rebeca' in lista)
print('Pedro' not in lista)
print(lista[0])
print(lista[4])
# print(lista[5])
print(lista[-1])
print(lista[-5])

print("\n")

lista = ['Ana', 'Lia', 'Rui', 'Paulo', 'Dani']
print(lista[1:3])
print(lista[1:-1])
print(lista[1:])
print(lista[:-1])
print(lista[:])
print(lista[::2])
print(lista[::-1])
del lista[2]
print(lista)
del lista[1:]
print(lista)
