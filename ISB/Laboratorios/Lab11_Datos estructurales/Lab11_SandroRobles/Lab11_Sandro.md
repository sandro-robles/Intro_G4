# **LABORATORIO 11: – Edge Impulse**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Introduccion, ¿Qué es Edge Impulse?](#Introduccion)
3. [Metodología](#Metodología)
5. [Cronología de mediciones](#Cronologíademediciones)
6. [Posiciones de los electrodos](#Posicionesdeloselectrodos)
7. [Resultados](#Resultados)
8. [Discusión](#Discusión)
9. [Ultracortex](#Ultracortex)
10. [Bibliografia](#Bibliografia)
    
## **Objetivos:**<a id="Objetivos"></a>
- Diseñar un proyecto en Edge Impulse para cada categoría de señal procesada (EMG, ECG y EEG).
- Desarrollar un script en VisualStudio que permita cargar las señales correspondientes en la plataforma Edge Impulse.
  
## **¿Qué es Edge Impulse?**<a id="Introduccion"></a>
<p align="justify"> Edge Impulse es una plataforma de desarrollo especializada en aprendizaje automático para dispositivos de borde (edge devices). Su objetivo es facilitar a los desarrolladores la creación, optimización y despliegue de modelos de machine learning en hardware embebido de forma eficiente y accesible.[1]​.‌ </p>

<p align="center"><img src="Anexos/edgeimpulse.png" width="400"></p>

<p align="center"><i>Figura 1: Logo Edge Impulse [1].</i></p>

## **Metodología:**<a id="Metodología"></a>
<p align="justify"> Los datos empleados para este laboratorio fueron obtenidos en formato .txt, los cuales fueron adquiridos de los laboratorios de señales biológicas (ECG, EMG y EEG). La plataforma Edge Impulse requiere de archivos en formato .csv para poder ser procesados y clasificados, por lo que se empleó un script en Visual Studio Code, el cual que convierte automáticamente los archivos .txt al formato .csv, ajustando así su estructura para cumplir con los requisitos de la plataforma principal. </p>
     
|  **Señal biológica**  | **Imagen de obtención** | **Señal obtenida** |
|:------------:|:---------------:|:---------------:|
| ECG |   <p align="center"><img src="Anexos/ecg_foto.png" width="400"></p>  |  <p align="center"><img src="Anexos/ecg_señalobtenida.png" width="400"></p> | 
| EEG |  <p align="center"><img src="Anexos/eeg_foto.png" width="400"></p>  |  <p align="center"><img src="Anexos/eeg_señalobtenida.png" width="400"></p> | 
| EMG |   <p align="center"><img src="Anexos/emg_foto.png" width="400"></p>  |  <p align="center"><img src="Anexos/emg_señalobtenida.png" width="400"></p> | 
</div>
<p align="center"><i>Tabla 1. Señales biológicas que serán procesadas. </i> </p>

### **Coversión de .txt a .csv:**<a id="Conversion"></a>
```python
import csv

def transformar_txt_a_csv(ruta_origen, ruta_destino, indice_columna=5, cabecera=None):
    """
    Convierte un archivo .txt en un archivo .csv, extrayendo una columna específica
    y añadiendo un contador de tiempo como referencia.
    """
    with open(ruta_origen, 'r') as archivo_entrada, open(ruta_destino, 'w', newline='') as archivo_salida:
        escritor = csv.writer(archivo_salida)

        # Escribir la cabecera en el archivo CSV
        if cabecera:
            escritor.writerow(cabecera)
        else:
            escritor.writerow(['tiempo', 'valor'])

        contador_tiempo = 0  # Inicializa el contador de tiempo

        # Procesar cada línea del archivo .txt
        for linea in archivo_entrada:
            if linea.startswith('#'):  # Ignorar líneas de encabezado o comentarios
                continue
            datos = linea.strip().split('\t')  # Dividir las columnas por tabulaciones
            if len(datos) > indice_columna:  # Verificar si la columna requerida existe
                escritor.writerow([contador_tiempo, datos[indice_columna]])  # Guardar tiempo y valor
                contador_tiempo += 1  # Incrementar el contador

# Ejemplo de uso
archivo_txt = 'ECG_ejercicio.txt'
archivo_csv = 'ECG_ejercicio.csv'
transformar_txt_a_csv(archivo_txt, archivo_csv, indice_columna=5, cabecera=['Tiempo (ms)', 'Señal EMG'])

```

<p align="center"><img src="Anexos/txtacsv.png" width="400"></p>

<p align="center"><i>Figura 2: Conversión de .txt a .csv </i></p>

### **Señal ECG en Edge Impulse:**<a id="SeñalEMG"></a>
<p align="justify"> Código utilizado para subirlo a la plataforma:</p>

```python
import requests
import os
import csv

# =======================
# Configuración
# =======================

# Clave API para Edge Impulse
clave_api = 'ei_f65e60f5f26d74bd5d6670d43186d03e007d69d0ee4796bf9d4675f4b5609212'

# Lista de rutas de archivos CSV a procesar
lista_csv = [
    r'C:\Users\User\Downloads\Lab11_SandroRobles\ECG\ECG_ejercicio.csv',
    r'C:\Users\User\Downloads\Lab11_SandroRobles\ECG\ECG_postrespiracion.csv',
    r'C:\Users\User\Downloads\Lab11_SandroRobles\ECG\ECG_prosim.csv',
    r'C:\Users\User\Downloads\Lab11_SandroRobles\ECG\ECG_prosim.csv',
    r'C:\Users\User\Downloads\Lab11_SandroRobles\ECG\ECG_respiracion.csv',
]

# Tamaño inicial del intervalo (en filas)
tamano_intervalo = 500  # Configurar según la cantidad de muestras por segundo

# Incremento del intervalo en filas
incremento_intervalo = 100

# Límite máximo de fragmentos por archivo
max_fragmentos = 15

# Carpeta para guardar los fragmentos temporalmente
carpeta_salida = 'csv_fragmentos'
os.makedirs(carpeta_salida, exist_ok=True)

# =======================
# Código Principal
# =======================

for archivo in lista_csv:
    # Obtener el nombre base del archivo
    nombre_archivo = os.path.basename(archivo).replace('.csv', '')

    print(f"\nProcesando el archivo: {archivo}...")
    try:
        # Leer el archivo CSV línea por línea
        with open(archivo, 'r') as entrada_csv:
            lector = csv.reader(entrada_csv)
            encabezado = next(lector)  # Leer el encabezado

            # Renombrar la columna de datos a "Datos"
            if len(encabezado) > 1:
                encabezado[1] = "Datos"

            # Fragmentos
            fragmento_actual = []
            contador_filas = 0
            indice_fragmento = 1
            filas_por_fragmento = tamano_intervalo

            for fila in lector:
                if indice_fragmento > max_fragmentos:
                    break  # Detener si se alcanza el límite de fragmentos

                fragmento_actual.append(fila)
                contador_filas += 1

                # Guardar el fragmento cuando se alcance el tamaño del intervalo
                if contador_filas == filas_por_fragmento:
                    nombre_fragmento = f"{nombre_archivo}_parte_{indice_fragmento}.csv"
                    ruta_fragmento = os.path.join(carpeta_salida, nombre_fragmento)

                    with open(ruta_fragmento, 'w', newline='') as salida_fragmento:
                        escritor = csv.writer(salida_fragmento)
                        escritor.writerow(encabezado)
                        escritor.writerows(fragmento_actual)

                    # Subir el fragmento a Edge Impulse
                    print(f"Subiendo: {nombre_fragmento}...")
                    archivo_preparado = [('data', (nombre_fragmento, open(ruta_fragmento, 'rb'), 'text/csv'))]
                    try:
                        respuesta = requests.post(
                            url='https://ingestion.edgeimpulse.com/api/training/files',
                            headers={
                                'x-label': nombre_archivo,
                                'x-api-key': clave_api,
                            },
                            files=archivo_preparado
                        )

                        if respuesta.status_code == 200:
                            print(f"¡Subida exitosa! Fragmento: {nombre_fragmento}")
                        else:
                            print(f"Error al subir el fragmento: {nombre_fragmento}. Código:", respuesta.status_code)
                            print("Mensaje del servidor:", respuesta.text)
                    finally:
                        for _, fileobj in archivo_preparado:
                            fileobj[1].close()

                    # Reiniciar para el siguiente fragmento
                    fragmento_actual = []
                    contador_filas = 0
                    indice_fragmento += 1
                    filas_por_fragmento += incremento_intervalo

            # Guardar el último fragmento si hay filas restantes
            if fragmento_actual and indice_fragmento <= max_fragmentos:
                nombre_fragmento = f"{nombre_archivo}_parte_{indice_fragmento}.csv"
                ruta_fragmento = os.path.join(carpeta_salida, nombre_fragmento)

                with open(ruta_fragmento, 'w', newline='') as salida_fragmento:
                    escritor = csv.writer(salida_fragmento)
                    escritor.writerow(encabezado)
                    escritor.writerows(fragmento_actual)

                print(f"Subiendo fragmento final: {nombre_fragmento}...")
                archivo_preparado = [('data', (nombre_fragmento, open(ruta_fragmento, 'rb'), 'text/csv'))]
                try:
                    respuesta = requests.post(
                        url='https://ingestion.edgeimpulse.com/api/training/files',
                        headers={
                            'x-label': nombre_archivo,
                            'x-api-key': clave_api,
                        },
                        files=archivo_preparado
                    )

                    if respuesta.status_code == 200:
                        print(f"¡Subida exitosa! Fragmento final: {nombre_fragmento}")
                    else:
                        print(f"Error al subir el fragmento final: {nombre_fragmento}. Código:", respuesta.status_code)
                        print("Mensaje del servidor:", respuesta.text)
                finally:
                    for _, fileobj in archivo_preparado:
                        fileobj[1].close()

    except Exception as error:
        print(f"Error al procesar el archivo {archivo}: {error}")

print("\nProceso completado.")

```
<p align="center"><img src="Anexos/ecg_edge.png" width="1000"></p>

<p align="center"><i>Figura 3: Señal ECG en Edge Impulse </i></p>

***Justificación de parámetros para la Señal EMG***
| **Músculo** | **Señales**|
|:------------:|:---------------:|
|Tricep en reposo| ![tricep_en_reposo1](https://github.com/user-attachments/assets/7a7f44a0-bf2e-40df-87f6-eb8e25601987)|
|Gastro en reposo|![gastrorepososs](https://github.com/user-attachments/assets/c77da4ab-5dd5-4f28-ac09-11ea39e0a676)|
|Mano en reposo|![manosreposo](https://github.com/user-attachments/assets/e31c8bdf-c221-4c6f-8dec-57d819c12725)|
|Bícep braquial en reposo|![biceoreposo](https://github.com/user-attachments/assets/225313e2-8673-43ee-b6a9-601c8d22805a)|
|Trapecio en reposo|![trapecioo](https://github.com/user-attachments/assets/a0d15370-ae7e-409a-91a3-ad316d773bf2)|

**Interpretación**

-Señal EMG Original: Esta es la señal original que representa la actividad muscular en un estado de reposo durante el intervalo de 0 a 10 segundos. La señal muestra variaciones leves, lo cual es típico en condiciones de reposo, donde la actividad muscular es mínima o casi inexistent

-Coeficientes de Detalle Nivel 1: Este nivel de descomposición wavelet recoge las componentes de frecuencias altas y de corta duración. Las variaciones detectadas son muy leves, lo que sugiere la falta de actividad muscular rápida o de interferencias de alta frecuencia, lo cual concuerda con un estado de reposo.

-Coeficientes de Detalle Nivel 2: Los coeficientes de este nivel corresponden a una combinación de frecuencias medias y altas. Aunque las fluctuaciones son un poco más marcadas que en el primer nivel, continúan siendo moderadas, lo que sigue reflejando la tranquilidad de la señal muscular en estado de reposo.

-Coeficientes de Detalle Nivel 3: Este nivel captura componentes de frecuencia más baja en comparación con los niveles anteriores. Los patrones de actividad muscular son aún más constantes y uniformes, lo que confirma la ausencia de actividad muscular relevante durante el estado de reposo.

-Coeficientes de Detalle Nivel 4: Este nivel recoge las componentes de baja frecuencia. Las variaciones son más notorias que en los niveles anteriores, pero continúan reflejando una actividad muy baja y constante, característica de la falta de contracción muscular.


### **SEÑAL EEG:**<a id="SeñalECG"></a>
<p align="justify"> Se consideraron las señales de electroencefalograma (EEG) obtenidas en el Laboratorio 06 para el proceso de filtrado utilizando la transformada wavelet. Estas señales fueron registradas en diferentes estados:</p>

- Estado de reposo: El sujeto permaneció en una posición estable y tranquila, manteniendo la calma, con el fin de registrar una línea base de señal con mínimas interferencias y sin movimientos. Este estado sirve como prueba de control, y el registro de la señal duró 30 segundos.

- Estado de ojos cerrados y abiertos: El sujeto realizó un ciclo de abrir y cerrar los ojos en cinco ocasiones, manteniendo cada estado durante 5 segundos. Para evitar artefactos en la señal, el sujeto permaneció tranquilo y mirando a un punto fijo. La señal fue registrada durante 50 segundos.

- Estado de segundo reposo: Después de la actividad de parpadeo, el sujeto retomó el estado de calma, sin movimientos, como una segunda fase de referencia. La señal fue grabada nuevamente por 30 segundos.

- Estado de razonamiento: El sujeto resolvió mentalmente una serie de ejercicios matemáticos, de menor a mayor dificultad, mientras mantenía la mirada fija en un punto para evitar artefactos. Entre cada respuesta y la siguiente pregunta, se dejó un lapso de 12 segundos para el registro de la señal.

***Justificación de parámetros para la Señal EEG***
<p align="justify"> En el estudio titulado "Procesamiento de señales de electroencefalograma mediante wavelets para la eliminación de artefactos cardíacos",  se seleccionaron tres tipos de wavelets: Coiflets de orden 3, Daubechies de orden 4 y Symlets de orden 5. Estas fueron elegidas por su capacidad de filtrar artefactos cardíacos sin distorsionar la señal EEG. Los niveles de detalle eliminados fueron los niveles 2 y 3, ya que los artefactos cardíacos suelen aparecer en frecuencias bajas (0.5 a 4 Hz), y la eliminación de estos niveles permite eliminar el ruido sin afectar las ondas cerebrales importantes. El umbral de eliminación se ajustó usando SNR y NMSE para optimizar el filtrado sin pérdida significativa de información [5].</p>


## **Discusión:**<a id="Discusión"></a>
<p align="justify"> </p>


## **Bibliografia:**<a id="Bibliografia"></a>
<p align="justify">[1]Seshapu Prassanna, et al. “Application of Wavelet Based Security and Compression Techniques for Biomedical Instrumentation Signals.” International Journal of Innovative Technology and Exploring Engineering, vol. 9, no. 4, 13 Feb. 2020, pp. 57–64, www.researchgate.net/publication/364028066_Application_of_Wavelet_Based_Security_and_Compression_Techniques_for_Biomedical_Instrumentation_Signals, https://doi.org/10.35940/ijitee.c9014.029420. Accessed 20 Oct. 2024.</p>
<p align="justify">[2] S. Kouro and R. Musalem, “Tutorial introductorio a la Teoría de Wavelet.” Available: http://www2.elo.utfsm.cl/~elo377/documentos/Wavelet.pdf
‌.</p>
<p align="justify">[3]G. Antonio and L. Paredes, “Reconocimiento de patrones en electroforesis capilar utilizando análisis multiresolucional y programación dinámica / Gerardo Ceballos,” 2024. https://www.researchgate.net/publication/44720047_Reconocimiento_de_patrones_en_electroforesis_capilar_utilizando_analisis_multiresolucional_y_programacion_dinamica_Gerardo_Ceballos (accessed Oct. 20, 2024).</p>
<p align="justify">[4] N. N. B and D. Marcela, “El uso de la transformada wavelet discreta en la reconstrucción de señales senosoidales.,” Scientia et Technica, vol. 1, no. 38, pp. 381–386, 2024, doi: https://dialnet.unirioja.es/descarga/articulo/4782789.pdf.‌‌</p>
<p align="justify">[5] R Singh and R Mehta, “Efficient wavelet families for ECG classification using neural classifiers” Science Direct, 2014, doi: https://doi.org/10.1016/j.procs.2018.05.054</p>
<p align="justify">[5] Beatriz, Pérez Alberruche. “Procesamiento de Señales de Electroencefalograma Mediante Wavelets Para La Eliminación de Artefactos Cardíacos  | Archivo Digital UPM.” Oa.upm.es, Sept. 2022, oa.upm.es/71888/, https://oa.upm.es/71888/. Accessed 21 Oct. 2024.</p>


