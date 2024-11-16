# **LABORATORIO 11: Datos estructurales Edge Impulse**
## **Edge impluse:**
Edge Impulse es una plataforma para desarrollar algoritmos de aprendizaje máquina enfocados a implementarse en sistemas embebidos como microcontroladores o computadoras con recursos reducidos. Tiene disponibles diversas herramientas que la hacen adecuada tanto para principiantes como usuarios avanzados. La practicidad de esta herramienta es que no necesitas involucrarte demasiado con el código, puedes implementar tu algoritmo con ingresar tu base de datos, ajustas los hiperparámetros y entrenas el programa.
<p align="center"><img width="394" alt="edge" src="https://github.com/user-attachments/assets/a41215c7-e936-4a1f-9e4d-b771579a7825">
<p align="center"><i>Figura 1:Logo Edge Impulse</i></p>

## **Pasos a seguir:**
<p align="justify">1.- Los datos utilizados para el desarrollo de este laboratorio se obtuvieron a partir de los experimentos realizados en los laboratorios 3, 4 y 5, correspondientes a las señales de ECG, EMG y EEG. Estos datos fueron adquiridos originalmente en formato ".txt". Para integrarlos en el entorno de Edge Impulse, fue necesario convertirlos al formato ".csv", asegurando así su compatibilidad y procesamiento adecuado. A continuación, se presenta el código empleado para realizar dicha conversión: </p>

```python
import pandas as pd
import numpy as np
import csv

# Cargar los datos desde un archivo de texto
data_cruda = np.loadtxt('eegsimples.txt')

# Seleccionar la última columna (si es necesario)
data_cruda = data_cruda[:, -1]

# Escalar la señal (según los factores dados)
signal = ((data_cruda - 507) / 1023) * 3.3 * 1000

# Frecuencia de muestreo
fs = 1000  # en Hz

# Convertir la señal a una lista
signal_data = list(signal)

# Calcular el número total de datos
total_data = len(signal_data)

# Generar una línea de tiempo para la señal
time_total = total_data / fs  # Tiempo total en segundos
time_data = np.linspace(0, time_total, total_data)  # Generar un array de tiempo
time_data = list(time_data)  # Convertirlo a lista

# Nombre del archivo de salida
output_file = 'EEG_respiracion2.csv'

# Escribir los datos en un archivo CSV
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Escribir la cabecera del archivo CSV
    csvwriter.writerow(['timestamp', 'valores'])
    
    # Escribir cada par de valores (tiempo y señal) en el archivo
    for t, v in zip(time_data, signal_data):
        csvwriter.writerow([t, v])

print(f"Archivo guardado exitosamente como {output_file}")
```

<p align="justify">2.-Una vez convertidos los datos al formato ".csv", se utilizó Google Colab como herramienta para procesar y preparar los archivos antes de subirlos a los respectivos repositorios. En este paso, los datos fueron segmentados en intervalos de 2 a 3 segundos, asegurando un formato adecuado para su posterior análisis. Cabe destacar que herramientas como Google Colab o entornos como Visual Studio pueden ser empleadas para este tipo de tareas.
<table align="center">
  <tr>
    <td align="center">
      <img width="200" alt="Logo de Colab" src="https://github.com/user-attachments/assets/80e11574-0156-44b7-b78c-0f7529df3034">
      <br>Logo de Colab
    </td>
    <td align="center">
      <img width="200" alt="Logo de Visual Studio" src="https://github.com/user-attachments/assets/bd31a68a-95ab-447f-b574-61c514ff724c">
      <br>Logo de Visual Studio
    </td>
  </tr>
</table>

<p align="justify">3.-



