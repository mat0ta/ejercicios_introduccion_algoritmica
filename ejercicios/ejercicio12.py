from random import randint, random


dinero_inicial = 00
cuentas = []

def crearCuenta():
    if dinero_inicial > 0:
        nombre = input('Bienvenido a Bancos Robles. Por favor, introduce tu nombre: ')
        numero_de_cuenta = randint(1000000000, 9999999999)
        for i in range(len(cuentas)):
            if numero_de_cuenta == cuentas[i]:
                numero_de_cuenta = randint(1000000000, 9999999999)
        cuentas.append({
            'Nombre': nombre,
            'Número de Cuenta': numero_de_cuenta
        })
        print(cuentas)
    else:
        print('No tiene dineso duficiente para crear una cuenta.')

crearCuenta()