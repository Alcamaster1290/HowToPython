import pandas as pd
import numpy as np

# ============================================
# Filtros y análisis con Pandas y NumPy ⚽
# ============================================

# Creamos un DataFrame con datos ficticios de jugadores

np.random.seed(42)  # NO TE ASUSTES ! ASI TENDRAS LOS MISMOS VALORES ALEATORIOS QUE YO

data = {
    "Jugador": ["P.Guerrero", "G.Lapadula", "E.Flores", "A.Valera", "J.Rivera", "L.Ramos"],
    "Tiros": np.random.randint(5, 15, size=6),
    "Goles": np.random.randint(0, 6, size=6),
    "Asistencias": np.random.randint(0, 5, size=6),
    "Edad": [22, 25, 28, 21, 24, 27],
    "Minutos_Jugados": np.random.randint(200, 900, size=6),
}

df = pd.DataFrame(data)

# Mostramos la tabla de jugadores
print("⚽ Tabla de jugadores:")
print(df)

# --------------------------------------------
# Filtros útiles para scouting y análisis ⚽
# --------------------------------------------

# 🔍 Jugadores con más de 3 goles
jugadores_goleadores = df[df["Goles"] > 3]
print("\n🔥 Jugadores con más de 3 goles:")
print(jugadores_goleadores)

# 🎯 Jugadores con más de 10 tiros y al menos 2 asistencias
jugadores_activos = df[(df["Tiros"] > 10) & (df["Asistencias"] >= 2)]
print("\n🎯 Jugadores con más de 10 tiros y al menos 2 asistencias:")
print(jugadores_activos)

# 🏆 Jugador con más goles
jugador_top_goleador = df.loc[df["Goles"].idxmax()]
print("\n🏆 Jugador con más goles:")
print(jugador_top_goleador)

# 📊 Jugadores menores de 25 años con más de 500 minutos jugados
jugadores_jovenes = df[(df["Edad"] < 25) & (df["Minutos_Jugados"] > 500)]
print("\n🚀 Jugadores menores de 25 años con más de 500 minutos jugados:")
print(jugadores_jovenes)

# 🎯 Efectividad de cada jugador (Goles/Tiros)
df["Efectividad"] = df["Goles"] / df["Tiros"]
print("\n📈 Tabla con efectividad de jugadores:")
print(df)

# 🏅 Jugadores con efectividad mayor al 40%
jugadores_efectivos = df[df["Efectividad"] > 0.4]
print("\n🏅 Jugadores con efectividad mayor al 40%:")
print(jugadores_efectivos)

# --------------------------------------------
# EJERCICIO: Realiza un filtro para encontrar jugadores con:
# - Más de 2 asistencias y una efectividad mayor al 30%
# - Menos de 500 minutos jugados pero con al menos 2 goles
