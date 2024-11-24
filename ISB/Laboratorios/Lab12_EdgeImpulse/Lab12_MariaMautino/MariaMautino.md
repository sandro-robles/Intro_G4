# **LABORATORIO 12: – Mejora Edge Impulse**

Integrante: María Fernanda Mautino Rodríguez

<h2 style = "text-align: center;">Links de Edge Impulse:</h2>

1. [EDGE IMPULSE - ECG](https://studio.edgeimpulse.com/public/560002/live)</p>

## **Edge impluse:**
<p align="justify">Edge Impulse es una plataforma de inteligencia artificial especializada en el desarrollo y entrenamiento de modelos para dispositivos periféricos o de borde. Estos dispositivos incluyen sensores, microcontroladores y hardware de bajo consumo, permitiendo procesar datos localmente sin depender de conexiones constantes a la nube. Esto optimiza el rendimiento y la seguridad en aplicaciones que requieren análisis en tiempo real. </p>

<p align="center"><img src="Anexos Lab12/3.png" width="400"></p>
<p align="center"><i>Figura 1: Página de Edge Impulse personal.</i></p>

<p align="justify">Tras aplicar el proceso de fragmentación y subida de los datos preprocesados a la plataforma Edge Impulse, se logró recolectar un total de 19 minutos y 50 segundos de datos clasificados. La distribución inicial del conjunto de datos presentó un balance general de 74% para entrenamiento y 26% para prueba. Este resultado fue producto de la segmentación y balanceo de los archivos originales en fragmentos más pequeños, con la finalidad de optimizar la representación de cada clase.</p>

<p align="justify">El proceso permitió trabajar con cinco categorías principales:</p>

1. ECG_BASAL
2. ECG_EJERCICIOS
3. ECG_POST_RESP
4. ECG_PRUEBAPROSIM
5. ECG_RESP

<p align="center"><img src="Anexos Lab12/1.png" width="400"></p>
<p align="center"><i>Figura 2:Distribución Train/Test: 74% entrenamiento y 26% prueba con un total de 19 minutos y 50 segundos.</i></p> 

<p align="justify"> Luego, se implementó un proceso de ajuste en el dataset para mejorar la proporción de las etiquetas y acercarlas a una distribución del 80% entrenamiento y 20% prueba. El ajuste consistió en aplicar resampling a los datos originales, aumentando o disminuyendo la cantidad de muestras en función de un factor de corrección específico para cada etiqueta.</p>

## **Ajuste del Dataset mediante Resampling:**
```python
import os
import pandas as pd
import requests

# =======================
# Configuración general
# =======================
# Clave API de Edge Impulse
api_key = 'ei_9cd4d3d4ae4c68bd1c9a7b8021a172de05cea4cbf3ba12f170f3bb25b11e13a2'

# Archivos CSV base
file_paths = {
    "ECG_basal": r'C:\Users\User\Desktop\ECG_basal.csv',
    "ECG_ejercicios": r'C:\Users\User\Desktop\ECG_ejercicios.csv',
    "ECG_post_resp": r'C:\Users\User\Desktop\ECG_post_resp.csv',
    "ECG_pruebaprosim": r'C:\Users\User\Desktop\ECG_pruebaprosim.csv',
    "ECG_resp": r'C:\Users\User\Desktop\ECG_resp.csv'
}

# Carpeta de salida para archivos ajustados
output_folder = r'C:\Users\User\Desktop\ECG_correcciones'
os.makedirs(output_folder, exist_ok=True)

# Configuración de resampleo
factores_ajuste = {
    "ECG_basal": 1.05,  # Ajustes pequeños para mejorar la distribución
    "ECG_ejercicios": 1.2,
    "ECG_post_resp": 1.1,
    "ECG_pruebaprosim": 1.1,
    "ECG_resp": 1.0  # Sin cambio en este caso
}

# =======================
# Funciones principales
# =======================

def ajustar_resampleo(file_paths, factores_ajuste):
    """
    Aplica ajustes de resampleo para equilibrar las proporciones.
    """
    fragmentos_generados = []
    for label, file_path in file_paths.items():
        print(f"Ajustando archivo: {label}...")
        try:
            # Leer datos originales
            data = pd.read_csv(file_path, sep=',')
            
            # Determinar factor de ajuste
            factor = factores_ajuste.get(label, 1.0)
            n_samples = int(len(data) * factor)
            
            # Aplicar resampleo
            data_resampleada = data.reindex(
                pd.RangeIndex(start=0, stop=n_samples),
                method=None
            ).interpolate(method="linear").ffill().bfill()
            
            # Guardar archivo ajustado
            output_path = os.path.join(output_folder, f"{label}_ajustado.csv")
            data_resampleada.to_csv(output_path, index=False)
            fragmentos_generados.append((output_path, label))
        
        except Exception as e:
            print(f"Error al ajustar {label}: {e}")
    
    return fragmentos_generados

def subir_a_edge_impulse(fragmentos, api_key):
    """
    Sube los archivos ajustados a Edge Impulse.
    """
    for ruta_fragmento, label in fragmentos:
        prepared_file = [('data', (os.path.basename(ruta_fragmento), open(ruta_fragmento, 'rb'), 'text/csv'))]
        print(f"Subiendo {os.path.basename(ruta_fragmento)} con etiqueta {label}...")
        try:
            response = requests.post(
                url='https://ingestion.edgeimpulse.com/api/training/files',
                headers={
                    'x-label': label,
                    'x-api-key': api_key,
                },
                files=prepared_file
            )
            if response.status_code == 200:
                print(f"¡Subida exitosa! Archivo: {os.path.basename(ruta_fragmento)}")
            else:
                print(f"Error al subir {os.path.basename(ruta_fragmento)}: {response.status_code}, {response.text}")
        finally:
            for _, fileobj in prepared_file:
                fileobj[1].close()

# =======================
# Código principal
# =======================

# Ajustar archivos con resampleo
fragmentos_ajustados = ajustar_resampleo(file_paths, factores_ajuste)
print(f"\nSe generaron {len(fragmentos_ajustados)} archivos ajustados.")

# Subir los archivos ajustados a Edge Impulse
print("\nSubiendo archivos ajustados a Edge Impulse...")
subir_a_edge_impulse(fragmentos_ajustados, api_key)

print("\nProceso completado. Archivos ajustados y subidos a Edge Impulse.")

```
<p align="center"><img src="Anexos Lab12/2.png" width="400"></p>
<p align="center"><i>Figura 3: Distribución Train/Test: 78% entrenamiento y 22% prueba con un total de 24 minutos y 10 segundos.</i></p> 

<p align="justify"> Para alcanzar el balance deseado de 80% Training / 20% Test, se realizó un ajuste manual en la distribución de las muestras. En particular, se movieron algunas muestras de la clase ECG_post_resp desde el conjunto de pruebas (Test) hacia el conjunto de entrenamiento (Training). Este cambio permitió equilibrar la proporción global del dataset, logrando el objetivo establecido para la separación entre los conjuntos de entrenamiento y prueba.</p>

<p align="center"><img src="Anexos Lab12/4.png" width="400"></p>
<p align="center"><i>Figura 4: Distribución Train/Test: 80% entrenamiento y 20% prueba con un total de 24 minutos y 10 segundos.</i></p> 

## **Creación de Impulse:**
<p align="justify">Para continuar con el proceso de clasificación de las señales de ECG, se procedió a la creación de un Impulse en Edge Impulse. Este impulse tiene como objetivo procesar los datos en bruto de las señales mediante análisis espectral para extraer características relevantes.</p>

<p align="center"><img src="Anexos Lab12/5.png" width="400"></p>
<p align="center"><i>Figura 5:Impulse.</i></p> 

## **Análisis Espectral:**
<p align="justify">En esta etapa del procesamiento de datos, se implementó el análisis espectral, se utilizó la Transformada Rápida de Fourier (FFT) para analizar las señales de ECG y extraer información del espectro de frecuencias. Se configuró un tamaño de FFT de 16 y se aplicó una escala logarítmica para visualizar mejor la potencia de las frecuencias. Además, se activó el traslape de marcos para capturar más detalles de las señales. El resultado fue un espectro que muestra cómo se distribuye la energía en las diferentes frecuencias, lo cual será útil para que el modelo pueda identificar patrones en las señales.</p>

<p align="center"><img src="Anexos Lab12/6.png" width="400"></p>
<p align="center"><i>Figura 6: Análisis Espectral.</i></p> 

## **Training set:**
<p align="justify">En esta etapa, se procesaron las señales del conjunto de datos de entrenamiento, obteniendo un total de 1,036 ventanas de entrenamiento distribuidas entre las cinco clases definidas: ECG_basal, ECG_ejercicios, ECG_post_resp, ECG_pruebaprosim y ECG_resp. Utilizando la técnica UMAP, se redujeron las dimensiones de las características para su análisis visual en el explorador de características, donde se identificaron patrones específicos para cada clase.</p>

<p align="center"><img src="Anexos Lab12/7.png" width="400"></p>
<p align="center"><i>Figura 7:Training set.</i></p> 


## **Resultados del Modelo de Clasificación:**
<p align="justify">El modelo alcanzó una precisión del 59.1% y una pérdida de 1.01. Las clases "ECG_post_resp" y "ECG_pruebaprosim" fueron las mejor clasificadas, mientras que "ECG_basal", "ECG_ejercicios" y "ECG_resp" tuvieron más errores. El área bajo la curva ROC fue de 0.85, mostrando buen desempeño general, aunque se necesita mejorar la clasificación en algunas clases.</p>

<p align="center"><img src="Anexos Lab12/8.png" width="400"></p>
<p align="center"><i>Figura 8: Resultados del Modelo de Clasificación.</i></p> 

## **Retrain:**
<p align="justify">El modelo fue entrenado y validado con éxito utilizando las características espectrales generadas.</p>

<p align="center"><img src="Anexos Lab12/9.png" width="400"></p>
<p align="center"><i>Figura 9: Retraining output.</i></p> 

