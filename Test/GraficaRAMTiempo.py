import pandas as pd
import matplotlib.pyplot as plt

# Ruta del archivo CSV generado
csv_path = "uso_cpu_ram_PID_OBJETIVO.csv"  # Cambiar PID_OBJETIVO por el PID en cuestión

# Leer CSV
df = pd.read_csv(csv_path)

# Convertir la columna de tiempo a tipo datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Crear figura y ejes
fig, ax1 = plt.subplots(figsize=(12, 6))


# Crear segundo eje Y para la RAM
ax2 = ax1.twinx()
ax2.set_ylabel('RAM (MB)', color='tab:blue')
ax2.plot(df['Timestamp'], df['RAM (MB)'], color='tab:blue', label='RAM (MB)')
ax2.tick_params(axis='y', labelcolor='tab:blue')

# Título y formato
plt.title("RAM del proceso a lo largo del tiempo")
fig.tight_layout()

# Mostrar
plt.show()
