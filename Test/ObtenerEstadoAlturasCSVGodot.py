import pandas as pd

# Leer el CSV generado mediante Godot
df = pd.read_csv('OpcCliente9.csv')

# Seleccionar NivelTanque1 y NivelTanque2
niveles = df[['NivelTanque1', 'NivelTanque2']]

# Multiplicar ambos valores por 30/100 (0.3)
niveles['NivelTanque1'] = niveles['NivelTanque1'] * 0.3
niveles['NivelTanque2'] = niveles['NivelTanque2'] * 0.3

# Mostrar el resultado
print(niveles)

# Opcional: Guardar el resultado en un nuevo CSV
niveles.to_csv('niveles_tanques_cm1.csv', index=False)