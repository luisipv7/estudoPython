for i in range(10):
  print(i)

for i in range(1,11):
  print(i)

for i in range(1,100,7):
  print(i)

for i in range(20,0,-3):
  print(i)

nums = [2, 4, 6, 8]

for n in nums:
  print(n, end=' ')

texto = 'Python é muito massa !'

for letra in texto:
  print(letra, end=' ')

for n in {1,2,3,4,4,4,4}:
  print(n, end=' ')

produto = {
    'nome': 'Caneca',
    'preco': 8.80,
    'desc': 0.5,
  }

for key in produto :
  print(key, '===>', produto[key])


for key, value in produto.items() :
  print(key, '===>', value)

for value in produto.values() :
  print(value, end=' ')

for key in produto.keys() :
  print(key, end=' ')
