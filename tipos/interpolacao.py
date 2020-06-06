from string import Template

nome, idade = 'Ana', 30

print('Nome: %s Idade: %d' % (nome,idade)) #mais Antigo
print('Nome: {0} Idade: {1}'.format(nome, idade)) #python < 3.6
print(f'Nome: {nome} Idade: {idade}')  # python >= 3.6

s = Template('Nome: $campoNome Idade: $campoIdade')
print(s.substitute(campoNome=nome, campoIdade=idade))
