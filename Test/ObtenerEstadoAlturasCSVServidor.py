import pandas as pd

# Leer el CSV generado por el script InterpolarSaltos.py
df = pd.read_csv('datos_interpolados1.csv')

# Seleccionar NivelTanque1 y NivelTanque2
niveles = df[['Nivel1', 'Nivel2']]

# Multiplicar ambos valores por 30/100 (0.3)
niveles['Nivel1'] = niveles['Nivel1'] * 0.3
niveles['Nivel2'] = niveles['Nivel2'] * 0.3

# Mostrar el resultado
print(niveles)

# Guardar el resultado en un nuevo CSV
niveles.to_csv('niveles_tanques_pool_cm1.csv', index=False)