#Ejemplo para la sentencia continue

print('While con la sentencia Break \n')
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        continue

    print('Valor actual de la variable: ', contador)

