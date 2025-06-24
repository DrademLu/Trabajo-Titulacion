# Si se desea probar este scipt, se recomienda tener en primer plano la ventana ejecutable del DT
# de lo contrario, la pulsación podría no detectarse
from opcua import Client
from datetime import datetime
import csv
import time
import os
import keyboard  # pip install keyboard
from time import sleep

# === CONFIGURACIÓN ===
URL = "opc.tcp://10.21.162.10:4840"

# IDs de nodos OPC UA
NODO_1_ID = "ns=1;i=1005"  # altura tanque 1
NODO_2_ID = "ns=1;i=1006"  # altura tanque 2
NODO_3_ID = "ns=1;i=1007"  # Qin
NODO_4_ID = "ns=1;i=1008"  # Qout
NODO_5_ID = "ns=1;i=1009"  # Qint

TIEMPO_EJECUCION = 720                  # Segundos totales
CSV_FILE = "lecturas_simuladas6.csv"  # Nombre del archivo a generar
APPEND_MODE = False

INTERVALO_INTERNO = 1 / 3              # Polling cada 0.333 segundos
LECTURAS_POR_SEGUNDO = 3

# Estados iniciales de los controles simulados
ctrl_bomba = 0
ctrl_svalve = 0
ctrl_bvalve = 0

# División de fases
fase_duracion = TIEMPO_EJECUCION / 5
fase_2_inicio = fase_duracion
fase_2_fin = 4 * fase_duracion
fase_4_inicio = TIEMPO_EJECUCION - fase_duracion

# Timers de teclas
ultimo_4 = -99
ultimo_5 = -99
ultimo_6 = -99

# Conectar cliente
client = Client(URL)
sleep(6.0) # Ventana de tiempo para ubicarse en la ventana del ejecutable

try:
    with client:
        print("Conectado al servidor OPC UA")

        # Obtener nodos
        nodo1 = client.get_node(NODO_1_ID)
        nodo2 = client.get_node(NODO_2_ID)
        nodo3 = client.get_node(NODO_3_ID)
        nodo4 = client.get_node(NODO_4_ID)
        nodo5 = client.get_node(NODO_5_ID)

        # Preparar CSV
        mode = 'a' if APPEND_MODE and os.path.exists(CSV_FILE) else 'w'
        with open(CSV_FILE, mode=mode, newline='') as archivo:
            writer = csv.writer(archivo)
            if mode == 'w' or not os.path.exists(CSV_FILE):
                writer.writerow([
                    "TimestampLocal", "Nivel1", "Nivel2",
                    "CtrlBomba", "CtrlSValve", "CtrlBValve",
                    "Qin", "Qout", "Qint"
                ])

            print("Iniciando simulación...")

            start = time.time()
            while (time.time() - start) < TIEMPO_EJECUCION:
                elapsed = time.time() - start
                seg = int(elapsed)

                # === FASES DE SIMULACIÓN ===
                if fase_2_inicio <= elapsed < fase_2_fin:
                    if seg - ultimo_4 >= 15:
                        ctrl_bomba = 1 - ctrl_bomba
                        keyboard.press_and_release('4')
                        ultimo_4 = seg
                        print("Tecla 4 simulada")

                    if seg - ultimo_5 >= 5:
                        ctrl_svalve = 1 - ctrl_svalve
                        keyboard.press_and_release('5')
                        ultimo_5 = seg
                        print("Tecla 5 simulada")

                    if seg - ultimo_6 >= 10:
                        ctrl_bvalve = 1 - ctrl_bvalve
                        keyboard.press_and_release('6')
                        ultimo_6 = seg
                        print("Tecla 6 simulada")

                elif elapsed >= fase_4_inicio:
                    # Última fase: poner todo en 0 una vez
                    if ctrl_bomba != 0 or ctrl_svalve != 0 or ctrl_bvalve != 0:
                        ctrl_bomba = ctrl_svalve = ctrl_bvalve = 0
                        if ctrl_bomba != 0:
                            keyboard.press_and_release('4')
                        if ctrl_bvalve != 0:
                            keyboard.press_and_release('6')
                        if ctrl_svalve != 0:
                            keyboard.press_and_release('5')
                        print("Reset final de controles: B=0, S=0, V=0")

                # Leer caudales
                try:
                    val_qin = float(nodo3.get_value())
                    val_qout = float(nodo4.get_value())
                    val_qint = float(nodo5.get_value())
                except Exception as e:
                    print(f"Error al leer caudales: {e}")
                    val_qin = val_qout = val_qint = 0.0

                # Promediar niveles
                vals_1 = []
                vals_2 = []
                for _ in range(LECTURAS_POR_SEGUNDO):
                    try:
                        vals_1.append(float(nodo1.get_value()))
                        vals_2.append(float(nodo2.get_value()))
                    except Exception as e:
                        print(f"Error al leer niveles: {e}")
                        vals_1.append(0.0)
                        vals_2.append(0.0)
                    time.sleep(INTERVALO_INTERNO)

                promedio_1 = sum(vals_1) / len(vals_1)
                promedio_2 = sum(vals_2) / len(vals_2)

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                writer.writerow([
                    timestamp, promedio_1, promedio_2,
                    ctrl_bomba, ctrl_svalve, ctrl_bvalve,
                    val_qin, val_qout, val_qint
                ])

                print(f"[{timestamp}] Niveles: {promedio_1:.2f}, {promedio_2:.2f} | B: {ctrl_bomba} S: {ctrl_svalve} V: {ctrl_bvalve}")

        print("Finalizado y datos guardados.")

except Exception as e:
    print("Error:", e)

finally:
    print("Desconectado del servidor OPC UA.")