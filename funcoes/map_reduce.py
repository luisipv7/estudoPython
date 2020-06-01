from functools import reduce


def somarNota(delta):
    def somar(nota):
        return nota + delta
    return somar


notas = [6.4, 7.2, 5.8, 8.4]
notas_finais_1 = map(somarNota(1.5), notas)
notas_finais_2 = map(somarNota(1.6), notas)

print(list(notas_finais_1))
print(list(notas_finais_2))

def soma(a, b):
    return a + b

total = reduce(soma, notas, 0)
print(total)
# for i, nota in enumerate(notas):
#   notas[i] = nota + 1.5

# for i in range(len(notas)):
#   notas[i] = notas[i] + 1.5
