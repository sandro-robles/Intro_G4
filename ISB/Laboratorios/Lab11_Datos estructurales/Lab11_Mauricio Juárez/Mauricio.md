# **LABORATORIO 11: – Datos estructurales Edge Impulse**

## **Procedimiento:**
<p align="justify"> Las señales que se utilizarán en este laboratorio son de laboratorios pasados de EMG, ECG y EEG. Para leer cada archivo .txt se utilizará el siguiente código:</p>

```python
import pandas as pd
import numpy as np
import csv
def lectura(n_archivo):
    with open(n_archivo, 'r') as archivo:
        n=0
        signal=np.array([])
        for linea in archivo:
            if n>2:
                #print(linea)
                vec=linea.split()
                signal=np.append(signal,int(vec[5]))
                n=n+1
            else:
                n=n+1
        t=np.arange(len(signal))
        fs=1000
        ts=1/fs
        t=t*ts
        return t,signal
```
<p align="justify">Dicho código nos permitirá obtener los valores de la señal en cada muestreo de la señal. Luego de leer la data, corresponde hacer una segmentación de las señales (en este caso 2 segundos) y luego pasar cada señal segmentada a un archivo .csv</p>

```python
flag=0
for i in range(2000,len(signal1),2000):
    nom=Nombre del archivo+str(int(i/2000)) +'.csv'
    signal=signal1[flag:i]
    t=t1[flag:i]*1000
    q.append(signal)
    u.append(t)
    print(u)
    flag=flag+2000
    with open(nom, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['tiempo', 'valor'])
        for t, s in zip(t, signal):
            writer.writerow([t, s])
```

<p align="justify"> Con la data segmentada en archivos .csv se procede a utilizar Google Colab para subir las señales a cada proyecto de Edge Impulse creado para este laboratorio y separado por EMG, ECG y EEG.</p>

```python
flag=0
for i in range(2000,len(signal1),2000):
    nom=Nombre del archivo+str(int(i/2000)) +'.csv'
    signal=signal1[flag:i]
    t=t1[flag:i]*1000
    q.append(signal)
    flag=flag+2000
    with open(nom, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['tiempo', 'valor'])
        for t, s in zip(t, signal):
            writer.writerow([t, s])
```

<p align="justify"> 3. Con la data separada por intervalo ya se procedio a subirla a los respositorios de Edge Impulse de esta forma:.</p>

```python

api_key = "ei_4b85dea157371a359b7327c3b66dd5d8acb8ae07ac3f6ea18a55cfdd54fa44a3"

# Ruta del archivo CSV
file_path = Nombre del archivio
file_name = os.path.basename(file_path)

upload_url = "https://ingestion.edgeimpulse.com/api/training/data"

# Cabeceras para autenticación y nombre del archivo
headers = {
    "x-api-key": api_key,
    "x-file-name": file_name,
    "Content-Type": "application/json"
}


with open(file_path, "r") as file:
    file_content = file.read()

response = requests.post(
    upload_url,
    headers=headers,
    params=metadata,
    data=file_content 
)

    )

if response.status_code == 200:
    print(f"Archivo CSV subido con éxito: {file_name}")
else:
    print(f"Error al subir el archivo: {response.text}")
```

## **Repositorios:**

<p align="justify">Luego de haber subido todos los archivos con las señales segmentadas a cada repositorio, se presentan los enlaces para cada tipo de señal:</p>

<p align="center">EMG: https://studio.edgeimpulse.com/public/560501/live</p>
<p align="center">ECG: https://studio.edgeimpulse.com/public/560505/live</p>
<p align="center">EEG: https://studio.edgeimpulse.com/public/560508/live</p>

