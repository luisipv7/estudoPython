lockdown = False
grana = 30

status = 'Em casa' if lockdown or grana <= 100 else 'Uhhul'

print(f'o status é {status}')
