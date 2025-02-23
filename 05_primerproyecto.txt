import numpy as np
import pandas as pd
import streamlit as st

# 📌 Para ejecutar este script, abre la terminal y usa:
# `streamlit run 05_primerproyecto.py`

# 🏆 Simulación de datos de rendimiento de jugadores
np.random.seed(42)  # Fijar semilla para reproducibilidad

data = {
    "Jugador": ["P.Guerrero", "G.Lapadula", "E.Flores", "A.Valera", "J.Rivera", "L.Ramos"],
    "Tiros": np.random.randint(3, 10, size=4),
    "Goles": np.random.randint(0, 5, size=4)
}

df = pd.DataFrame(data)

# ➕ Agregar asistencias aleatorias entre 0 y 5
df["Asistencias"] = np.random.randint(0, 6, size=4)

# 🎯 Calcular Efectividad (Goles/Tiros)
df["Efectividad"] = (df["Goles"] / df["Tiros"]).round(2)

# 🔥 Calcular 'Participación en goles' (Goles + Asistencias)
df["Participación en goles"] = df["Goles"] + df["Asistencias"]

# 📊 INTERFAZ EN STREAMLIT
st.title("📈 Reporte de Rendimiento de Jugadores")
st.write("Análisis de tiros, goles, asistencias y efectividad")

# Mostrar la tabla de rendimiento
st.subheader("📋 Tabla de Rendimiento")
st.dataframe(df)

# 🏅 Jugador más efectivo
jugador_mas_efectivo = df.loc[df["Efectividad"].idxmax()]
st.subheader("⚽ Jugador Más Efectivo")
st.write(jugador_mas_efectivo)

# 🔝 Jugador con mayor participación en goles
jugador_top_participacion = df.loc[df["Participación en goles"].idxmax()]
st.subheader("🎯 Jugador con Mayor Participación en Goles")
st.write(jugador_top_participacion)

# 📌 Para ejecutar: en la terminal usa `streamlit run 05_primerproyecto.py`