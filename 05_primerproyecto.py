import numpy as np
import pandas as pd
import streamlit as st

# 📌 Para ejecutar este script, usa:
# `streamlit run 05_primerproyecto.py`

# 🏆 Simulación de datos de rendimiento de jugadores
np.random.seed(42)  # Fijar semilla para reproducibilidad

# ✅ Asegurar que todas las listas tengan la misma longitud (6 jugadores)
num_jugadores = 6

data = {
    "Jugador": ["P.Guerrero", "G.Lapadula", "E.Flores", "A.Valera", "J.Rivera", "L.Ramos"],
    "Tiros": np.random.randint(3, 10, size=num_jugadores),
    "Goles": np.random.randint(0, 5, size=num_jugadores),
    "Asistencias": np.random.randint(0, 6, size=num_jugadores)
}

df = pd.DataFrame(data)

# 🎯 Calcular Efectividad (Goles/Tiros) evitando división por cero
df["Efectividad"] = np.where(df["Tiros"] > 0, (df["Goles"] / df["Tiros"]).round(2), 0)

# 🔥 Calcular 'Participación en goles' (Goles + Asistencias)
df["Participación en goles"] = df["Goles"] + df["Asistencias"]

# 📊 INTERFAZ EN STREAMLIT
st.title("📈 Reporte de Rendimiento de Jugadores")
st.write("🔍 Análisis de tiros, goles, asistencias y efectividad")

# 📋 Mostrar la tabla de rendimiento sin colores
st.subheader("📋 Tabla de Rendimiento")
st.dataframe(df)

# 🏅 Jugador más efectivo
jugador_mas_efectivo = df.loc[df["Efectividad"].idxmax()]
st.subheader("⚽ Jugador Más Efectivo")
st.write(jugador_mas_efectivo.to_frame().T)

# 🔝 Jugador con mayor participación en goles
jugador_top_participacion = df.loc[df["Participación en goles"].idxmax()]
st.subheader("🎯 Jugador con Mayor Participación en Goles")
st.write(jugador_top_participacion.to_frame().T)