# 1.)
precio_inicial = 1000
porcentaje_iva = 0.21
precio_final = precio_inicial + (precio_inicial * porcentaje_iva)
print(precio_final)

# 2.)
capital = 10000
interes = 0.05
tiempo = 3

for i in range(tiempo):
    capital = capital + (capital * interes)

print(capital)