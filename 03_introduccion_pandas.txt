# ============================================
# Análisis de Rendimiento de Jugadores con Pandas ⚽
# ============================================

# Importamos la biblioteca Pandas para trabajar con datos en tablas
import pandas as pd

# --------------------------------------------
# Datos iniciales de jugadores: Nombre, Tiros y Goles
# --------------------------------------------
data = {
    "Jugador": ["J.Farfan", "E.Flores", "P.Guerrero", "A.Carrillo"],
    "Tiros": [5, 3, 8, 6],
    "Goles": [2, 1, 3, 2]
}

# Creamos el DataFrame a partir del diccionario de datos
df = pd.DataFrame(data)

# Mostramos la tabla de jugadores original
print("⚽ Tabla de jugadores:")
print(df)

# Calculamos el promedio de goles por jugador y lo mostramos
promedio_goles = df["Goles"].mean()  # Suma de goles / número de partidos
print("\n📊 Promedio de goles por jugador:", promedio_goles)

# EJERCICIOS MAS EPICOS

# 1. Calcular la efectividad de cada jugador: Efectividad = Goles / Tiros

df["Efectividad"] = df["Goles"] / df["Tiros"]

# 2. Ordenar el DataFrame por efectividad de mayor a menor

df_ordenado = df.sort_values(by="Efectividad", ascending=False)
print("\n📋 Tabla de jugadores ordenada por efectividad (Goles/Tiros):")
print(df_ordenado)

# 3. Filtrar jugadores con efectividad mayor a 0.4

jugadores_efectivos = df[df["Efectividad"] > 0.4]
print("\n🚀 Jugadores con efectividad mayor a 0.4:")
print(jugadores_efectivos)


# EN EL SIGUIENTE SE VIENE NUMPY + PANDAS