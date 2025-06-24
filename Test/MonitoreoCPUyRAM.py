import psutil
import time
import csv
from datetime import datetime, timedelta

# PID del proceso que deseas monitorear
PID_OBJETIVO = 31528  # PID proceso generado por la ejecución del DT (Encontrar manualmente mediante administrador de tareas)

# Intervalo de muestreo en segundos
INTERVALO = 1.0

# Duración total del monitoreo en minutos
DURACION_MINUTOS = 10

# Nombre del archivo de salida
nombre_csv = f"uso_cpu_ram_{PID_OBJETIVO}.csv"

# Obtener el proceso
try:
    proceso = psutil.Process(PID_OBJETIVO)
except psutil.NoSuchProcess:
    print(" No existe un proceso con ese PID.")
    exit()

# Tiempo de fin
tiempo_inicio = datetime.now()
tiempo_fin = tiempo_inicio + timedelta(minutes=DURACION_MINUTOS)

# Crear archivo CSV y escribir encabezado
with open(nombre_csv, mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(['Timestamp', 'CPU (%)', 'RAM (MB)'])

    print(f" Monitoreando PID {PID_OBJETIVO} durante {DURACION_MINUTOS} minutos...")
    try:
        while datetime.now() < tiempo_fin:
            cpu = proceso.cpu_percent(interval=None)  # % de CPU desde la última llamada
            ram = proceso.memory_info().rss / (1024 * 1024)  # RAM en MB
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            escritor.writerow([timestamp, cpu, ram])
            print(f"{timestamp} | CPU: {cpu:.2f}% | RAM: {ram:.2f} MB")
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print("\n Monitoreo detenido manualmente.")
    finally:
        print(" Monitoreo finalizado. Datos guardados en:", nombre_csv)
