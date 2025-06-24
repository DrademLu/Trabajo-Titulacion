import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer los archivos CSV
df1 = pd.read_csv('caudales_1.csv')  # CSV generado por godot
df2 = pd.read_csv('caudales_planta1.csv')  # CSV con los datos interpolados

# Crear un eje temporal ficticio (índice secuencial, 1 segundo por fila)
max_rows = max(len(df1), len(df2))  # Usar la longitud del CSV más largo
tiempo = np.arange(max_rows)  # [0, 1, 2, ..., max_rows-1]

# Crear una figura con un solo gráfico
fig, ax1 = plt.subplots(1, 1, figsize=(15, 4))

# Gráfico: NivelTanque1 y Valor_1
ax1.plot(tiempo[:len(df1)], df1['CaudalEntrada'], label='Godot DT', color='blue', marker='o')
ax1.plot(tiempo[:len(df2)], df2['Qin'], label='Planta', color='red', marker='|', linestyle='--')
ax1.set_title('Estado de la Bomba')
ax1.set_xlabel('Índice Temporal (segundos)')
ax1.set_ylabel('cm')
ax1.legend()
ax1.grid(True)

# Ajustar el espaciado
plt.tight_layout()

# Mostrar el gráfico
plt.show()