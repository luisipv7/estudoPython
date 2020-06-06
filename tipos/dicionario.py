aluno = {
  'nome': 'Pedro Henrique',
  'nota': 9.2,
  'ativo': True,
}

print(type(aluno))
print(aluno['nome'])
print(aluno['nota'])
print(aluno['ativo'])
print(len(aluno))


print('\n')

pessoa = {
  'nome': 'Prof(a). Ana',
  'idade': 38,
  'cursos': ['Inglês', 'Português']
}

print(type(pessoa))
# print(dir(dict))
print(len(pessoa))

print(pessoa)
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cursos'])
print(pessoa['cursos'][1])
# print(pessoa['tags'])
print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('idade'))
print(pessoa.get('tags'))
print(pessoa.get('tags', []))


print('\n')

pessoa = {
    'nome': 'Prof(a). Adalberto',
    'idade': 43,
    'cursos': ['React', 'Python']
}

pessoa['idade'] = 44
print(pessoa)
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({
  'idade': 40,
  'Sexo': 'M'
})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)
