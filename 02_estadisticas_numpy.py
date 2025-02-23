# Importamos la biblioteca NumPy para trabajar con datos numéricos de forma eficiente
import numpy as np

# ==============================
# ANÁLISIS ESTADÍSTICO DE GOLES
# ==============================

# Creamos un array con el número de goles por partido
goles = np.array([2, 1, 3, 0, 4])

# Calculamos el promedio de goles por partido
promedio_goles = np.mean(goles)  # Suma de todos los goles dividido por la cantidad de partidos

# Calculamos la mediana de goles
mediana_goles = np.median(goles)  # Valor central cuando los datos están ordenados

# Calculamos la desviación estándar de goles
desviacion_goles = np.std(goles)  # Mide la dispersión de los datos respecto al promedio

# Calculamos la varianza de goles (cuadrado de la desviación estándar)
varianza_goles = np.var(goles)

# Calculamos la moda de goles (valor más frecuente)
# Usamos np.bincount para contar ocurrencias y np.argmax para obtener el índice del mayor recuento
moda_goles = np.bincount(goles).argmax()

# Calculamos el rango de goles (diferencia entre el valor máximo y mínimo)
rango_goles = np.ptp(goles)

# Calculamos percentiles para entender la distribución de los datos
percentil_25_goles = np.percentile(goles, 25)  # 25% de los datos están por debajo de este valor
percentil_50_goles = np.percentile(goles, 50)  # Equivale a la mediana
percentil_75_goles = np.percentile(goles, 75)  # 75% de los datos están por debajo de este valor

# Calculamos el coeficiente de variación (desviación estándar dividida entre el promedio)
coeficiente_variacion_goles = desviacion_goles / promedio_goles if promedio_goles != 0 else 0

# Imprimimos los resultados de las estadísticas de goles
print("=== Estadísticas de Goles por Partido ===")
print("Promedio de goles:", promedio_goles)
print("Mediana de goles:", mediana_goles)
print("Desviación estándar:", desviacion_goles)
print("Varianza:", varianza_goles)
print("Moda de goles:", moda_goles)
print("Rango (máximo - mínimo):", rango_goles)
print("Percentil 25:", percentil_25_goles)
print("Percentil 50 (Mediana):", percentil_50_goles)
print("Percentil 75:", percentil_75_goles)
print("Coeficiente de variación:", coeficiente_variacion_goles)

# ==========================================
# ANÁLISIS ESTADÍSTICO DE ASISTENCIAS
# ==========================================

# Creamos un array con el número de asistencias por partido
asistencias = np.array([1, 0, 2, 1, 3, 2, 1, 4, 0, 3])

# Calculamos el promedio de asistencias
promedio_asistencias = np.mean(asistencias)  # Suma de asistencias dividido por la cantidad de partidos

# Calculamos la diferencia entre el máximo y el mínimo de asistencias (rango)
diferencia_asistencias = np.ptp(asistencias)

# Calculamos la mediana de asistencias
mediana_asistencias = np.median(asistencias)

# Calculamos la desviación estándar de asistencias
desviacion_asistencias = np.std(asistencias)

# Calculamos percentiles para asistencias
percentil_25_asistencias = np.percentile(asistencias, 25)
percentil_50_asistencias = np.percentile(asistencias, 50)  # Equivale a la mediana
percentil_75_asistencias = np.percentile(asistencias, 75)

# Imprimimos los resultados de las estadísticas de asistencias
print("\n=== Estadísticas de Asistencias por Partido ===")
print("Promedio de asistencias:", promedio_asistencias)
print("Diferencia entre máximo y mínimo:", diferencia_asistencias)
print("Mediana de asistencias:", mediana_asistencias)
print("Desviación estándar:", desviacion_asistencias)
print("Percentil 25:", percentil_25_asistencias)
print("Percentil 50 (Mediana):", percentil_50_asistencias)
print("Percentil 75:", percentil_75_asistencias)