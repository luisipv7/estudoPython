lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhhul'

esta_chuvendo = True

print(f'Hoje estou com roupas ' + ('secas', 'molhadas')[esta_chuvendo] )
print(f'o status é {status}')
