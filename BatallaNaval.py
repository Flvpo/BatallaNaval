import random

# Función para crear una cuadrícula vacía
def crear_cuadricula(filas, columnas):
    return [['~' for _ in range(columnas)] for _ in range(filas)]

# Función para imprimir la cuadrícula
def imprimir_cuadricula(cuadricula):
    for fila in cuadricula:
        print(" ".join(fila))

# Función para colocar los barcos de la máquina de manera aleatoria
def colocar_barcos_maquina(cuadricula, num_barcos):
    filas = len(cuadricula)
    columnas = len(cuadricula[0])
    for _ in range(num_barcos):
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - 1)
        while cuadricula[fila][columna] == 'X':
            fila = random.randint(0, filas - 1)
            columna = random.randint(0, columnas - 1)
        cuadricula[fila][columna] = 'X'

# Función para que el jugador adivine la ubicación de los barcos de la máquina
def adivinar(cuadricula_maquina, fila, columna):
    if cuadricula_maquina[fila][columna] == 'X':
        return True
    else:
        return False

# Configuración del juego
filas = 5
columnas = 5
num_barcos_maquina = 3

# Crear las cuadrículas del jugador y la máquina
cuadricula_jugador = crear_cuadricula(filas, columnas)
cuadricula_maquina = crear_cuadricula(filas, columnas)

# Colocar los barcos de la máquina de manera aleatoria
colocar_barcos_maquina(cuadricula_maquina, num_barcos_maquina)

print("¡Bienvenido al juego de Batalla Naval!")
print("Puedes adivinar la ubicación de los barcos de la máquina.")
print("La cuadrícula tiene", filas, "filas y", columnas, "columnas.")
print("Buena suerte!\n")

intentos = 0

while True:
    print("Intento #", intentos + 1)
    imprimir_cuadricula(cuadricula_jugador)

    try:
        fila = int(input("Ingresa el número de fila (0-4): "))
        columna = int(input("Ingresa el número de columna (0-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
        print("Fuera de rango. Ingresa números entre 0 y 4.")
        continue

    if adivinar(cuadricula_maquina, fila, columna):
        print("¡Ganaste! Has hundido un barco de la máquina.")
        cuadricula_jugador[fila][columna] = 'X'
        intentos += 1
        break
    else:
        print("Lo siento, no has acertado.")
        cuadricula_jugador[fila][columna] = 'O'
        intentos += 1

if intentos == 1:
    print("¡Lo lograste en 1 intento!")
else:
    print("¡Lo lograste en", intentos, "intentos!")
