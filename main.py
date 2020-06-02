
# print('ola mundo')

# import pacote.sub.arquivo

# ====================TIPOS===============================

# import tipos.variaveis
# from tipos import variaveis, basicos, lista, tuplas, conjuntos, dicionario

# ====================OPERADORES===============================
# from operadores import unarios, aritmeticos, relacionais, atribuicao, logicos

# ====================CONTROLE===============================
# from controle import if_1, if_2, for_1, while_1

# ====================FUNÇÔES===============================
# from funcoes import basico, args, funcional, map_reduce
# nome = input('Digite seu nome bb: ')
# idade = int(input('Digite sua idade: '))
# basico.saudacao_pela_manha(nome, idade)
# basico.saudacao_pela_manha()
# retorno = basico.soma_e_multi(x=10, a=2, b=3)
# print(retorno)
# soma = args.soma(1,2,3,4,5,6,7,8,9,10)
# print(soma)

# resultado = args.resultado_final(nome='Pedro',nota=6.3)
# print(resultado)

# funcional.soma(1, 1)

# ====================DESAFIOS===============================
from desafios import desafio_um, desafio_dois
#minhas Variaveis
# salario = 3450.45
# despesas = 2456.2

# result = desafio_um.calc_desafio(salario, despesas)

# print(result)

# O Trabalhos
trabalho_terca = bool(int(input('Digite 1(true) ou 0(false)')))
trabalho_quinta = bool(int(input('Digite 1(true) ou 0(false)')))

result_dois = desafio_dois.calc_desafioDois(trabalho_terca, trabalho_quinta)
print(result_dois, " terca={}, quinta={}".format(trabalho_terca, trabalho_quinta))
