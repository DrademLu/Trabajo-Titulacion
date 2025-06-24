import pandas as pd

# Leer el CSV generado mediante Godot
df = pd.read_csv('OpcCliente9.csv')

# Seleccionar solo las columnas NivelTanque1 y NivelTanque2
niveles = df[[' CtrlBomba', 'CtrlSValve', 'CtrlBValve']]
# Mostrar el resultado
print(niveles)

# Guardar el resultado en un nuevo CSV
niveles.to_csv('apertura_valvulas1.csv', index=False)