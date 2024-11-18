# **LABORATORIO 11: Datos estructurales Edge Impulse**
## **Edge impluse:**
Edge Impulse es una plataforma para desarrollar algoritmos de aprendizaje máquina enfocados a implementarse en sistemas embebidos como microcontroladores o computadoras con recursos reducidos. Tiene disponibles diversas herramientas que la hacen adecuada tanto para principiantes como usuarios avanzados. La practicidad de esta herramienta es que no necesitas involucrarte demasiado con el código, puedes implementar tu algoritmo con ingresar tu base de datos, ajustas los hiperparámetros y entrenas el programa.
<p align="center"><img width="394" alt="edge" src="https://github.com/user-attachments/assets/a41215c7-e936-4a1f-9e4d-b771579a7825">
<p align="center"><i>Figura 1:Logo Edge Impulse</i></p>

## **Objetivos del laboratorio:**
- Crear un proyecto en Edge Impulse (EI) para cada tipo de señal que se desea trabajar: EMG, ECG y EEG.
- Diseñar un script en Python que automatice la carga de datos de cada tipo de señal en la plataforma de EI.

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

<p align="justify">3.- Usamos este código para poder subir nuestros archivos al Edge Impulse, veremos a continuación algunas gráficas.
    
-ECG:


```python
import pandas as pd
import os
import requests
# Configuración
# =======================
# Clave API de Edge Impulse
api_key = 'ei_ce7073c877a48e7ef577de9ac7f8854970d040427c75448bc990c316b27ff490'

# Lista de archivos CSV a procesar
archivos_csv = [
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/ECG/ECG_ejercicio.csv',
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/ECG/ECG_prosim.csv',
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/ECG/ECG_reposo.csv',
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/ECG/ECG_respiracion.csv'
]
tamanio_intervalo = 500  # Ajusta según tus datos
label = 'tu_etiqueta'  # Etiqueta para los datos en Edge Impulse
# =======================
# Código Principal
# =======================
for archivo in archivos_csv:
    try:
        # Cargar los datos del archivo CSV
        data = pd.read_csv(archivo)
        nombre_base = os.path.basename(archivo).replace('.csv', '')

        # Calcular el número total de intervalos
        num_filas = len(data)
        num_intervalos = (num_filas // tamanio_intervalo) + (1 if num_filas % tamanio_intervalo != 0 else 0)

        print(f"\nProcesando archivo: {archivo}")
        print(f"Total de intervalos a subir: {num_intervalos}")

        for i in range(num_intervalos):
            # Filtrar datos para el intervalo actual
            inicio = i * tamanio_intervalo
            fin = min((i + 1) * tamanio_intervalo, num_filas)
            intervalo_data = data.iloc[inicio:fin]

            # Crear el nombre del archivo para el intervalo
            intervalo_filename = f'{nombre_base}_intervalo_{i + 1}.csv'
            intervalo_data.to_csv(intervalo_filename, index=False)  # Guardar en un archivo CSV temporal

            # Preparar el archivo para la subida
            file_tuple = ('data', (os.path.basename(intervalo_filename), open(intervalo_filename, 'rb'), 'application/csv'))

            print(f"Subiendo intervalo {i + 1}/{num_intervalos}...")
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files=[file_tuple]
            )

            # Verificar la respuesta de la subida
            if res.status_code == 200:
                print(f"¡Subida exitosa! Intervalo {i + 1}")
            else:
                print(f"Error al subir intervalo {i + 1}: {res.status_code}, {res.text}")

            # Cerrar el archivo después de la subida
            file_tuple[1][1].close()

    except Exception as e:
        print(f"Error al procesar el archivo {archivo}: {e}")
print("\nProceso completado.")

```

<p align="center"><img width="505" alt="Ejercicico intervalo 19" src="https://github.com/user-attachments/assets/bdc682e0-f2cd-47e7-9756-b7bb652ac012">

<p align="center"><i>Figura 2:Ejercicico intervalo 19</i></p>
<p align="center"><img width="505" alt="Reposo intervalo 76" src="https://github.com/user-attachments/assets/29dcdc41-0c7b-472f-93b6-497a7536bf24">
<p align="center"><i>Figura 3:Reposo intervalo 76</i></p>
<p align="center"><img width="505" alt="Respiracion intervalor 48" src="https://github.com/user-attachments/assets/45a956b3-c83a-46c6-a0b9-7db08fb94576">
<p align="center"><i>Figura 4:Respiracion intervalor 48</i></p>
<p align="center"><img width="505" alt="Pro sim intervalo 42" src="https://github.com/user-attachments/assets/d6d3b98f-6645-428f-ab5f-f1c21b3cbb8f">

<p align="center"><i>Figura 5:Pro sim intervalo 42</i></p>

-EMG:

```python
import pandas as pd
import os
import requests
# Configuración
# =======================
# Clave API de Edge Impulse
api_key = 'ei_3144080d5c50c4ccf956fc3dd33f457151ca704e625ef39ac9fba0b153c620a3'

# Lista de archivos CSV a procesar
archivos_csv = [
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/EMG/EMG_mano.csv',
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/EMG/EMG_manofuerza.csv',
    r'/Users/fernandaramirez/Desktop/LAB11_ANELRAMIREZ/EMG/EMG_manoreposo.csv',
]
tamanio_intervalo = 500  # Ajusta según tus datos
label = 'tu_etiqueta'  # Etiqueta para los datos en Edge Impulse
# =======================
# Código Principal
# =======================
for archivo in archivos_csv:
    try:
        # Cargar los datos del archivo CSV
        data = pd.read_csv(archivo)
        nombre_base = os.path.basename(archivo).replace('.csv', '')

        # Calcular el número total de intervalos
        num_filas = len(data)
        num_intervalos = (num_filas // tamanio_intervalo) + (1 if num_filas % tamanio_intervalo != 0 else 0)

        print(f"\nProcesando archivo: {archivo}")
        print(f"Total de intervalos a subir: {num_intervalos}")

        for i in range(num_intervalos):
            # Filtrar datos para el intervalo actual
            inicio = i * tamanio_intervalo
            fin = min((i + 1) * tamanio_intervalo, num_filas)
            intervalo_data = data.iloc[inicio:fin]

            # Crear el nombre del archivo para el intervalo
            intervalo_filename = f'{nombre_base}_intervalo_{i + 1}.csv'
            intervalo_data.to_csv(intervalo_filename, index=False)  # Guardar en un archivo CSV temporal

            # Preparar el archivo para la subida
            file_tuple = ('data', (os.path.basename(intervalo_filename), open(intervalo_filename, 'rb'), 'application/csv'))

            print(f"Subiendo intervalo {i + 1}/{num_intervalos}...")
            res = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files=[file_tuple]
            )

            # Verificar la respuesta de la subida
            if res.status_code == 200:
                print(f"¡Subida exitosa! Intervalo {i + 1}")
            else:
                print(f"Error al subir intervalo {i + 1}: {res.status_code}, {res.text}")

            # Cerrar el archivo después de la subida
            file_tuple[1][1].close()

    except Exception as e:
        print(f"Error al procesar el archivo {archivo}: {e}")
print("\nProceso completado.")


```
<p align="center"><img width="505" alt="Mano intervalo 4" src="https://github.com/user-attachments/assets/777c3faa-ddcc-4354-ab10-27b0cc83de2e">

<p align="center"><i>Figura 6:Mano intervalo 4</i></p>
<p align="center"><img width="505" alt="Mano reposo intervalo 34" src="https://github.com/user-attachments/assets/cc5a7896-49d9-4c4e-be7c-fbeb60bd6032">

<p align="center"><i>Figura 7:Mano reposo intervalo 34</i></p>
<p align="center"><img width="505" alt="Mano fuerza intervalo 36" src="https://github.com/user-attachments/assets/0b8ac9ba-323d-4174-85dc-d5e62c0be059">

<p align="center"><i>Figura 8:Mano fuerza intervalo 36</i></p>




