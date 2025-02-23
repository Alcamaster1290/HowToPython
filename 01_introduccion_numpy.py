# 🥷 ¡Hola, aquí inicia tu camino ninja!  
# 📌 Importamos la biblioteca NumPy para hacer cálculos matemáticos eficientes.

import numpy as np

# Imagina una lista de valores en una fila de Excel.
# Representan la distancia al arco de los disparos a puerta de un equipo X.
distancias = np.array([20, 18, 25, 12, 9])

# Operaciones básicas con NumPy
print("Distancias al arco:", distancias)
print("Distancia máxima:", np.max(distancias))
print("Distancia mínima:", np.min(distancias))
print("Distancia promedio:", np.mean(distancias))

# 📌 Guardamos el promedio en una variable y lo imprimimos con formato
promedio_distancias = np.mean(distancias)
print(f"📊 Distancia promedio: {promedio_distancias:.2f}")

# 🏆 EJERCICIO:

# 🔢 Crea un array con el número de tiros de un jugador en distintos partidos.

# 📌 Calcula el total de tiros - usa np.sum() 
# 📌 Calcula el promedio de tiros por partido
# 📌 Calcula el máximo y mínimo de tiros

# IMPRIME TODOS LOS VALORES Y TOMALE SS PARA EL RECUERDO ACABAS DE ENTENDER NUMPY