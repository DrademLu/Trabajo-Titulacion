import pandas as pd

# Leer el CSV generado por el script InterpolarSaltos.py
df = pd.read_csv('datos_interpolados1.csv')

# Seleccionar solo las columnas NivelTanque1 y NivelTanque2
niveles = df[['Qin', 'Qout', 'Qint']]
# Mostrar el resultado
print(niveles)

# Guardar el resultado en un nuevo CSV
niveles.to_csv('caudales_planta1.csv', index=False)