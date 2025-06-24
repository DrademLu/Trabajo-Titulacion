# Como las lecturas del código SimularPulsacionTeclas.py llegan a presentar "saltos" entre muestras
# este código busca realizar una interpolación para igualar la cantidad de muestrar con el tiempo de muestreo total

import pandas as pd

# Cargar CSV
df = pd.read_csv("lecturas_simuladas5.csv", parse_dates=["TimestampLocal"])

# Establecer índice de tiempo
df = df.set_index("TimestampLocal")

# Reindexar con frecuencia de 1 segundo
df_resample = df.resample("1S").mean()

# Interpolación método tiempo
df_interp = df_resample.interpolate(method="time", order=3)

# Resetear índice
df_interp = df_interp.reset_index()

# Guardar a un nuevo CSV
df_interp.to_csv("datos_interpolados1.csv", index=False)
