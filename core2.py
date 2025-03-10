import numpy as np

# Solicitar número de patrones y neuronas
numero_patrones = int(input("Número de patrones a almacenar: "))
numero_neuronas = int(input("Cantidad de neuronas en la red: "))

# Inicializar matriz de pesos con ceros
W = np.zeros((numero_neuronas, numero_neuronas))

# Obtener patrones de entrada
patrones = []
for i in range(numero_patrones):
    print(f"Ingrese el patrón {i+1} con {numero_neuronas} valores (-1 o 1):")
    patron = np.array([int(x) for x in input().split()])
    patrones.append(patron)
    
    # metodo hebbiano
    W += np.outer(patron, patron)

# Asegurar que la diagonal de W sea cero
np.fill_diagonal(W, 0)

print("Matriz de pesos W:")
print(W)

# Recuperación de patrones
def actualizar_estado(estado):
    """Actualiza el estado de la red usando la regla de activación de Hopfield."""
    return np.sign(W @ estado)

# Introducir un patron de prueba
ingreso = np.array([int(x) for x in input("Ingrese un patrón de prueba: ").split()])

# Iterar hasta converger
estado_actual = ingreso.copy()
anterior = np.zeros_like(estado_actual)

#while not np.array_equal(estado_actual, anterior):
#    anterior = estado_actual.copy()
#    estado_actual = actualizar_estado(estado_actual)

for i in range (np.array_equal(estado_actual, anterior)):
    anterior = estado_actual.copy()
    estado_actual = actualizar_estado(estado_actual)

print("Patrón asociado:")
print(estado_actual)

