# Escribe un programa que solicite al usuario un número entero positivo y luego 
# calcule el factorial de ese número utilizando recursión. Debe manejar las siguientes excepciones:

# Si el usuario ingresa un valor que no es un número entero, mostrar un mensaje de error e invitar al usuario a intentarlo de nuevo.
# Si el usuario ingresa un número negativo, también mostrar un mensaje de error y pedir nuevamente el número.

def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n
    

def main():
    try:

        while True:
            numero = int(input('Ingrese un número entero positivo: '))

            if numero < 0:
                raise ValueError('El número debe ser positivo')
            
            else: 
                print(f'El factorial de {numero} es {factorial(numero)}')
                break
        
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error: {e}')
main()

# Ejercicio 2: Matriz y Suma de Números Pares en Archivos CSV (Puntaje: 25%)
# Crea una matriz de tamaño 4x5 con números aleatorios entre 1 y 100. Luego, guarda esta matriz en un archivo CSV. 
# A continuación, lee el archivo y calcula la suma de todos los números pares en la matriz. 
# Si el archivo no existe, el programa debe crear uno con la matriz generada.
