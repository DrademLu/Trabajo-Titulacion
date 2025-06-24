import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer los archivos CSV
df1 = pd.read_csv('apertura_valvulas1.csv')  # CSV generado por godot
df2 = pd.read_csv('apertura_valvulas_planta1.csv')  # CSV con los datos interpolados

# Crear un eje temporal ficticio (índice secuencial, 1 segundo por fila)
max_rows = max(len(df1), len(df2))  # Usar la longitud del CSV más largo
tiempo = np.arange(max_rows)  # [0, 1, 2, ..., max_rows-1]

# Crear una figura con 2 subgráficos
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(15, 8), sharex=True)

# Gráfico 1: NivelTanque1 y Valor_1
#ax1.plot(tiempo[:len(df1)], df1[' CtrlBomba'], label='Godot DT', color='blue', marker='o')
ax1.plot(tiempo[:len(df2)], df2['CtrlBomba'], label='Planta', color='red',linestyle='--')
ax1.set_title('Estado de la Bomba')
ax1.set_ylabel('cm')
ax2.set_ylim(-0.1, 1.5)  # Establecer límites del eje y de 0 a 30
ax1.legend()
ax1.grid(True)

# Gráfico 2: NivelTanque2 y Valor_2
#ax2.plot(tiempo[:len(df1)], df1['CtrlSValve'], label='Godot DT', color='blue')
ax2.plot(tiempo[:len(df2)], df2['CtrlSValve'], label='Planta', color='red', linestyle='--')
ax2.set_title('Estado de la válvula solenoide')
ax2.set_xlabel('Índice Temporal (segundos)')
ax2.set_ylabel('cm')
ax2.set_ylim(-0.1, 1.5)  # Establecer límites del eje y de 0 a 30
ax2.legend()
ax2.grid(True)

# Gráfico 2: NivelTanque2 y Valor_2
#ax3.plot(tiempo[:len(df1)], df1['CtrlBValve'], label='Godot DT', color='blue')
ax3.plot(tiempo[:len(df2)], df2['CtrlBValve'], label='Planta', color='red',linestyle='--')
ax3.set_title('Estado de la válvula bola')
ax3.set_xlabel('Índice Temporal (segundos)')
ax3.set_ylabel('cm')
ax3.set_ylim(-0.1, 1.5)  # Establecer límites del eje y de 0 a 30
#ax3.set_xlim(275,325)
ax3.legend()
ax3.grid(True)

# Ajustar el espaciado entre subgráficos
plt.tight_layout()

# Mostrar el gráfico
plt.show()