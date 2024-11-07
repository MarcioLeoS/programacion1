# Escribe un programa que pregunte al usuario una palabra. 
# Luego, debe contar cuántas veces aparece cada letra en la palabra y mostrar los resultados de la forma: <letra>: <cantidad de veces>. 
# Además, el programa debe indicar cuántas letras son vocales y cuántas son consonantes.


def contar_letras(palabra):
    letras = {}

    for letra in palabra:
        if letra in letras:
            letras[letra] += 1
        else:
            letras[letra] = 1

    return letras



def main():
    total = 0
    palabra = input('Por favor, ingrese una palabra: ')
    letras = contar_letras(palabra)
    print('-----------')

    for letra, cantidad in letras.items():
        total = total =+ cantidad

        print(f'{letra}      {cantidad}')
        
    print('\n')
    print('-----------')
    print('\n')
    print(f'Total     {total}')



main()


# Crea una matriz rectangular de dimensiones 3x4 con números aleatorios entre 1 y 50. 
# Luego, genera una lista que contenga la suma de los elementos impares en cada columna de la matriz. 
# Muestra la matriz y luego la lista de resultados obtenidos.

import random
def crear_matriz():
    matriz = []
    for i in range(3):
        fila = []
        for j in range(4):
            fila.append(random.randint(1,50))
        matriz.append(fila)
    print(matriz)
    return matriz

def sumar_impares(matriz):
    sumas = []
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[j][i] % 2 != 0:
                suma = suma + matriz[j][i]
        sumas.append(suma)
        
    return sumas


def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end= ' ')
        print()

def main():
    matriz = crear_matriz()
    sumas = sumar_impares(matriz)

    print('-----------')
    print(sumas)
    print('Matriz:')
    print()
    imprimir_matriz(matriz)


main()


# Escribe un programa que permita gestionar los gastos de un viaje. 
# El programa debe preguntar al usuario por diferentes categorías de gastos (transporte, alojamiento, comidas, etc.) 
# y su costo, y añadir cada gasto a un diccionario. 
# El usuario puede añadir tantos gastos como desee hasta indicar que ha terminado.

# Luego, el programa debe permitir que el usuario consulte el costo de una categoría específica de gasto. 
# Si la categoría no existe, debe mostrar un mensaje informando que no está en la lista.




def agregar_gastos():
    flag = True
    gastos = {}
    try:
        while flag:
            categoria = input('Ingrese la categoría que corresponde al gasto: ')
            costo = float(input('Ingrese el costo del gasto: '))

            if costo == 0:
                raise RuntimeError('El costo debe ser mayor a cero')

            gastos = agregar_gastos_diccionario(gastos, categoria, costo)


            continuar = int(input('Ingrese -1 para finalizar, 0 para continuar: '))
            if continuar == -1:
                flag = False

    except ValueError:
        print('El costo debe ser un número')
    except Exception as e:
        print(f'Error en el progeama: {e}')
    return gastos

    
def agregar_gastos_diccionario(gastos, categoria, costo):
    gastos[categoria] = costo
    return gastos



def consultar_gastos(gastos):
    categoria = input('Ingrese la categoria que desea consultar: ')
    if gastos == {}:
        raise RuntimeError('No hay gastos para consultar')
    if categoria in gastos:
        print(f'El costo de la categoría {categoria} es de {gastos[categoria]}')
    else:
        print('La categoría no está en la lista')

def main():
    gastos = agregar_gastos()
    consultar_gastos(gastos)
main()