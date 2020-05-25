nota = float(input('Informe a nota do aluno: '))
comportado = True if input('Comportado? (y/n): ') == 'y' else False


if nota >= 9 and comportado:
  print('Você está no quadro de honra')
elif nota >= 7:
  print('Aprovado')
else:
  print('Voce não está no quadro de honra e reprovou bb')


# print(nota)
