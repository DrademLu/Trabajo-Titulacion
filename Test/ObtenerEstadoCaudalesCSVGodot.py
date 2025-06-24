import pandas as pd

# Leer el CSV generado mediante Godot
df = pd.read_csv('OpcCliente9.csv')

# Seleccionar solo las columnas NivelTanque1 y NivelTanque2
niveles = df[['CaudalEntrada', 'CaudalSalida', 'CaudalIntermedio']]
# Mostrar el resultado
print(niveles)

niveles['CaudalEntrada'] = niveles['CaudalEntrada'] * 60
niveles['CaudalSalida'] = niveles['CaudalSalida'] * 60
niveles['CaudalIntermedio'] = niveles['CaudalIntermedio'] * 60

# Guardar el resultado en un nuevo CSV
niveles.to_csv('caudales_1.csv', index=False)