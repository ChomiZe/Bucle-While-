#Ejemplo para sentencia Break
#para romper el ciclo o bucle para agregar una nueva interaccion

print('While con la sentencia Break \n')
contador = 0
while contador < 10:
    contador += 1

    if contador == 5:
        break

    print('Valor actual de la variable: ', contador)

print('Fin del programa, la sentencia Break se ha ejecutado')