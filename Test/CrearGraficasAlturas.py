import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer los archivos CSV
df1 = pd.read_csv('niveles_tanques_cm1.csv')   # CSV generado por godot
df2 = pd.read_csv('niveles_tanques_pool_cm1.csv')  # CSV con los datos interpolados

# Crear un eje temporal ficticio (índice secuencial, 1 segundo por fila)
max_rows = max(len(df1), len(df2))  # Usar la longitud del CSV más largo
tiempo = np.arange(max_rows)  # [0, 1, 2, ..., max_rows-1]

# Crear una figura con 2 subgráficos
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 8), sharex=True)

# Gráfico 1: NivelTanque1 y Valor_1
ax1.plot(tiempo[:len(df1)], df1['NivelTanque1'], label='Godot DT', color='blue', marker='o')
ax1.plot(tiempo[:len(df2)], df2['Nivel1'], label='Planta', color='red', linestyle='--')
ax1.set_title('Nivel de agua en el tanque 1')
ax1.set_ylabel('cm')
ax1.set_ylim(0, 30)  # Establecer límites del eje y de 0 a 30
ax1.legend()
ax1.grid(True)

# Gráfico 2: NivelTanque2 y Valor_2
ax2.plot(tiempo[:len(df1)], df1['NivelTanque2'], label='Godot DT', color='red', marker='o')
ax2.plot(tiempo[:len(df2)], df2['Nivel2'], label='Planta', color='blue', linestyle='--')
ax2.set_title('Nivel de agua en el tanque 2')
ax2.set_xlabel('Índice Temporal (segundos)')
ax2.set_ylabel('cm')
ax2.set_ylim(0, 30)  # Establecer límites del eje y de 0 a 30
ax2.legend()
ax2.grid(True)

# Ajustar el espaciado entre subgráficos
plt.tight_layout()

# Mostrar el gráfico
plt.show()