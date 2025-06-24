import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos
df = pd.read_csv("uso_cpu_ram_PID_OBJETIVO.csv")
cpu = df["CPU (%)"]
ram = df["RAM (MB)"]

# Función para generar cada boxplot
def graficar_boxplot(datos, etiqueta, color, unidad):
    media = datos.mean()
    std = datos.std()
    minimo = datos.min()
    maximo = datos.max()

    plt.figure(figsize=(5, 5))
    plt.boxplot(datos, patch_artist=True,
                boxprops=dict(facecolor=color, color="blue"),
                medianprops=dict(color="red"),
                whiskerprops=dict(color="gray"),
                capprops=dict(color="gray"),
                flierprops=dict(markerfacecolor="orange", marker='o', markersize=6, linestyle='none'))

    plt.title(f"Distribución de {etiqueta}")
    plt.ylabel(f"{etiqueta} ({unidad})")
    plt.xticks([1], [etiqueta])
    plt.grid(True, linestyle='--', alpha=0.5)

    texto = (
        f"Media: {media:.2f} {unidad}\n"
        f"Desv. Est.: {std:.2f}\n"
        f"Min: {minimo:.2f}\n"
        f"Max: {maximo:.2f}"
    )

    plt.text(1.15, media, texto, ha='left', va='center', fontsize=10,
             bbox=dict(facecolor='white', alpha=0.85))

    plt.tight_layout()
    plt.show()

# Graficar por separado
graficar_boxplot(cpu, "CPU", "lightblue", "%")
graficar_boxplot(ram, "RAM", "lightgreen", "MB")
