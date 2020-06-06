print({1,2,3})
print(type({1, 2, 3}))
conj = {1, 2, 3, 3, 3, 3, 3}
print({1, 2, 3, 3, 3, 3, 3})  # não duplica

# print(conj[1])

print(len(conj))

print('\n')

a = {1, 2, 3}
print(type(a))
#a[0]
a = set('codddder')
print(a)
print('3' in a, 4 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

#operacoes

c1 = {1,2}
c2 = {2, 3}
c1.union(c2)
print('c1', c1)
print('c2', c2)
c1.intersection(c2)
print('c1', c1)
print('c2', c2)
c1.update(c2)
print('c1', c1)
print('c2', c2)

print(c2 <= c1) # c2 é subconjunto de c1 ?
print(c1 >= c2)  # c1 é superconjunto de c2 ?

print({1, 2, 3} - {2})  # diferença entre os conjuntos

print(c1 - c2)
c1 -= {2}
print(c1)
