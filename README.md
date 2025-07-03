# Trabajo-Titulacion
Archvios relacionados con el trabajo de titualción de Luis Antonio Andrade Matute

Universidad de Cuenca

Facultad de Ingeniería

Carrera de Telecomuniaciones

## Directorio 3D
En este directorio puede encontrar el modelado 3D de los componentes físicos del sistema, tanto la versión para Blender como el exportado hacia Godot
## Directorio Test
En este directorio puede encontrar los scripts utilizados para la evaluación final del sistema.
- Los archivos .py se pueden ejecutar por separado, con el orden recomendado
  1. MonitoreoCPUyRAM.py
  2. SimularPulsacionTeclas.py (Conexión con a planta física)
  3. GraficaRAMTiempo.py
  4. BoxPlotRamCPU.py
  5. InterpolarSaltos.py
  6. ObtenerEstadoAlturasCSVGodot.py
  7. ObtenerEstadoAlturasCSVServidor.py
  8. ObtenerEstadoCaudalesCSVGodot.py
  9. ObtenerEstadoCaudalesCSVServidor.py
  10. ObtenerEstadoValvulasCSVGodot.py
  11. ObtenerEstadoValvulasCSVServidor.py
  12. CrearGraficasAlturas.py
  13. CrearGraficasCaudakes.py
  14. CrearGraficasEstadoValvulas.py
- Archivos .ipynb pueden ser ejecutados en VSCode, con Jupyter Notebooks instalado. Solo existen 2 archivos que recopilan todos los .py:
  1. RecopilarDatos.ipynb, recopila los scripts para la comparación de operación entre el sistema físico y el sistema digital.
  2. AnalisisTemporalEstados.ipynb, recopila los scripts para la recopilación de estadisticas de funcionamiento, entre uso de memoría, latencia de la comuniación así como la recopilación de datos para comparar el sistema físico con el sistema digital.
