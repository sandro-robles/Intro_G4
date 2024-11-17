# **LABORATORIO 11: – Datos estructurales / Edge Impulse**

Integrante: María Fernanda Mautino Rodríguez

## **Edge impluse:**
<p align="justify">Edge Impulse es una plataforma de inteligencia artificial especializada en el desarrollo y entrenamiento de modelos para dispositivos periféricos o de borde. Estos dispositivos incluyen sensores, microcontroladores y hardware de bajo consumo, permitiendo procesar datos localmente sin depender de conexiones constantes a la nube. Esto optimiza el rendimiento y la seguridad en aplicaciones que requieren análisis en tiempo real. </p>

## **Objetivos:**
- Crear un proyecto en Edge Impulse para cada tipo de señal procesada, como EMG, ECG y EEG, clasificándolas de manera adecuada.
- Implementar un código en Python para cargar las señales correspondientes a la plataforma Edge Impulse.

## **Metodología:**
<p align="justify">Los datos utilizados en este desarrollo fueron adquiridos en formato .txt, provenientes de los laboratorios de señales biológicas, específicamente de ECG, EMG y EEG. Dado que el entorno de Edge Impulse requiere archivos en formato .csv para su análisis, se desarrolló un script en Python que permite convertir automáticamente los archivos .txt en archivos .csv, adaptando su estructura al formato esperado. </p>

```python
import requests
import os
import csv

# =======================
# Configuración
# =======================

# Clave API de Edge Impulse
api_key = 'ei_9cd4d3d4ae4c68bd1c9a7b8021a172de05cea4cbf3ba12f170f3bb25b11e13a2'

# Archivos CSV a dividir y subir con rutas completas
archivos_csv = [
    r'C:\Users\User\Desktop\ECG_basal.csv',
    r'C:\Users\User\Desktop\ECG_pruebaprosim.csv',
    r'C:\Users\User\Desktop\ECG_post_resp.csv',
    r'C:\Users\User\Desktop\ECG_ejercicios.csv',
    r'C:\Users\User\Desktop\ECG_resp.csv'  
]

# Tamaño base del intervalo (en número de filas)
intervalo_filas_base = 500  # Ajusta según el número de muestras por segundo

# Incremento del intervalo (en filas) para cambiar dinámicamente el `length`
incremento_filas = 100

# Número máximo de intervalos por archivo
max_intervalos = 15
# Carpeta temporal para guardar los fragmentos
carpeta_temporal = 'fragmentos_csv'
os.makedirs(carpeta_temporal, exist_ok=True)

# =======================
# Código Principal
# =======================

for ruta_archivo in archivos_csv:
    # Extraer el nombre base del archivo para generar etiquetas
    nombre_base = os.path.basename(ruta_archivo).replace('.csv', '')

    print(f"\nProcesando archivo: {ruta_archivo}...")
    try:
        # Leer el archivo CSV línea por línea
        with open(ruta_archivo, 'r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            encabezado = next(lector_csv)  # Leer la primera fila como encabezado
            
            # Cambiar el nombre de la columna de datos a "ECG"
            if len(encabezado) > 1:  # Asegurarse de que haya más de una columna
                encabezado[1] = "ECG"

            # Fragmentos
            fragmento = []
            contador = 0
            fragmento_idx = 1
            intervalo_filas = intervalo_filas_base

            for fila in lector_csv:
                if fragmento_idx > max_intervalos:
                    break  # Detener el proceso si alcanzamos el máximo de intervalos
                
                fragmento.append(fila)
                contador += 1

                # Si alcanzamos el tamaño del intervalo, guardamos el fragmento
                if contador == intervalo_filas:
                    # Guardar el fragmento como archivo CSV
                    fragmento_nombre = f"{nombre_base}_intervalo_{fragmento_idx}.csv"
                    ruta_fragmento = os.path.join(carpeta_temporal, fragmento_nombre)
                    
                    with open(ruta_fragmento, 'w', newline='') as archivo_fragmento:
                        escritor_csv = csv.writer(archivo_fragmento)
                        escritor_csv.writerow(encabezado)  # Escribir encabezado con "ECG"
                        escritor_csv.writerows(fragmento)  # Escribir datos

                    # Subir el archivo fragmento a Edge Impulse
                    print(f"Subiendo fragmento: {fragmento_nombre}...")
                    prepared_file = [('data', (fragmento_nombre, open(ruta_fragmento, 'rb'), 'text/csv'))]
                    try:
                        res = requests.post(
                            url='https://ingestion.edgeimpulse.com/api/training/files',
                            headers={
                                'x-label': nombre_base,  # Etiqueta basada en el nombre del archivo
                                'x-api-key': api_key,
                            },
                            files=prepared_file
                        )

                        if res.status_code == 200:
                            print(f"¡Subida exitosa! Fragmento: {fragmento_nombre}")
                        else:
                            print(f"Falló la subida del fragmento: {fragmento_nombre}. Código de estado:", res.status_code)
                            print("Respuesta del servidor:", res.text)
                    finally:
                        # Cerrar el archivo después de la solicitud
                        for _, fileobj in prepared_file:
                            fileobj[1].close()

                    # Reiniciar el fragmento
                    fragmento = []
                    contador = 0
                    fragmento_idx += 1
                    intervalo_filas += incremento_filas  # Incrementar dinámicamente el tamaño del intervalo

            # Si hay datos restantes y no se alcanzó el límite de intervalos, guardar el último fragmento
            if fragmento and fragmento_idx <= max_intervalos:
                fragmento_nombre = f"{nombre_base}_intervalo_{fragmento_idx}.csv"
                ruta_fragmento = os.path.join(carpeta_temporal, fragmento_nombre)
                
                with open(ruta_fragmento, 'w', newline='') as archivo_fragmento:
                    escritor_csv = csv.writer(archivo_fragmento)
                    escritor_csv.writerow(encabezado)
                    escritor_csv.writerows(fragmento)

                print(f"Subiendo fragmento final: {fragmento_nombre}...")
                prepared_file = [('data', (fragmento_nombre, open(ruta_fragmento, 'rb'), 'text/csv'))]
                try:
                    res = requests.post(
                        url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': nombre_base,
                            'x-api-key': api_key,
                        },
                        files=prepared_file
                    )

                    if res.status_code == 200:
                        print(f"¡Subida exitosa! Fragmento final: {fragmento_nombre}")
                    else:
                        print(f"Falló la subida del fragmento final: {fragmento_nombre}. Código de estado:", res.status_code)
                        print("Respuesta del servidor:", res.text)
                finally:
                    for _, fileobj in prepared_file:
                        fileobj[1].close()

    except Exception as e:
        print(f"Error al procesar el archivo {ruta_archivo}: {e}")

print("\nProceso completado.")
```
