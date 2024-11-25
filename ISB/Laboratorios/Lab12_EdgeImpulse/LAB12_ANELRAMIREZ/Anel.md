# **LABORATORIO 12: Continuación Edge Impulse**

Integrante: Anel Fernanda Ramirez Condori

Link Edge Impulse -> https://studio.edgeimpulse.com/public/565803/live

## **¿Qué es el Edge impulse?**
<p align="justify">Edge Impulse es una plataforma de aprendizaje automático diseñada para desarrollar modelos de inteligencia artificial. Permite a los usuarios entrenar y optimizar modelos de machine learning utilizando datos de sensores, como señales biométricas (EEG o ECG), audio, movimiento e imágenes, para ejecutarlos en dispositivos de bajo consumo como microcontroladores y sistemas embebidos. Con una interfaz gráfica intuitiva, facilita el flujo de trabajo desde la recopilación de datos hasta la implementación del modelo en hardware, sin necesidad de conocimientos avanzados. Edge Impulse es ampliamente utilizado en casos como reconocimiento de gestos, monitoreo de salud, clasificación de sonidos, visión por computadora y mantenimiento predictivo, destacándose por su enfoque en dispositivos pequeños, su integración con frameworks como TensorFlow Lite y su capacidad para crear modelos altamente eficientes.

## **Pasos a seguir en este laboratorio:**
<p align="justify">Como este laboratorio es la continuación del anterior, elegimos una de las señales, en este caso la del EMG. Observando asi que tenemos un Train/Test de 80% / 20%.
  
<p align="center"><img width="705" alt="Captura de pantalla 2024-11-25 a las 1 19 16 a  m" src="https://github.com/user-attachments/assets/23d6c334-3aa9-46c9-86c9-50fa1622d93e">

<p align="center"><i>Figura 1: Distribución Train/Test de EMG 80/20

1.- Creamos nuestro impulso:tiene como objetivo procesar datos en bruto provenientes de señales, como las biométricas o ambientales, utilizando análisis espectral y otras técnicas avanzadas para extraer características relevantes.

<p align="center"><<img width="1001" alt="Captura de pantalla 2024-11-25 a las 1 19 46 a  m" src="https://github.com/user-attachments/assets/bee27d26-e81c-4ea2-8ec9-eb9c451b7449">

<p align="center"><i>Figura 2: Creación del impulso

2.- Análisis espectral: En esta fase de procesamiento de datos, se implementó el análisis espectral utilizando la Transformada Rápida de Fourier (FFT) para analizar señales de ECG y extraer información clave del espectro de frecuencias. Se estableció un tamaño de ventana FFT de 16, aplicando una escala logarítmica para resaltar la distribución de la potencia en las distintas frecuencias de manera más clara. Además, se activó el traslape de marcos para capturar detalles adicionales de las señales, mejorando la resolución temporal y espectral. Este proceso generó un espectro que representa cómo se distribuye la energía en las frecuencias, proporcionando información esencial para que el modelo pueda detectar y aprender patrones característicos en las señales analizadas.


<p align="center"><img width="1001" alt="Captura de pantalla 2024-11-25 a las 1 20 22 a  m" src="https://github.com/user-attachments/assets/c2449d37-0fc3-4577-8d00-07dc93b658ea">
<p align="center"><i>Figura 3: Análisis espectral

3.- Training set: En esta etapa, se procesaron las señales del conjunto de datos de entrenamiento, generando un total de 145 ventanas de entrenamiento distribuidas equitativamente entre las 4 clases definidas.

<p align="center"><img width="1001" alt="Captura de pantalla 2024-11-25 a las 1 30 03 a  m" src="https://github.com/user-attachments/assets/bfafb732-5ad1-4a28-a603-8ac292403ae1">
<p align="center"><i>Figura 4: Training set del EMG

4.-Modelos de clasificación: El modelo logró una precisión del 52.2% con una pérdida de 0.94. Las clases "ECG_REPOSO" y "ECG_EJERCICIO" obtuvieron los mejores resultados en clasificación, mientras que "ECG_PROSIM" y "ECG_RESPIRACIÓN" presentaron un mayor número de errores. Además, el modelo alcanzó un área bajo la curva ROC (AUC) de 0.83, indicando un desempeño razonable en la diferenciación entre clases, aunque con margen de mejora en ciertas categorías.

<p align="center"><img width="477" alt="Captura de pantalla 2024-11-25 a las 1 41 16 a  m" src="https://github.com/user-attachments/assets/5919d1ce-29dd-4a8f-9fc6-cc52f53154b5">
<p align="center"> <i>Figura 5: Clasificación - resultados

5.- Retrain model with known parameters: El modelo es entrenado y vemos que se realizón con éxito

<p align="center"><img width="988" alt="Captura de pantalla 2024-11-25 a las 1 47 04 a  m" src="https://github.com/user-attachments/assets/269f1ba1-10e0-4197-89ad-aba26134feef">
<p align="center"><i>Figura 6: Modelo entrenado con éxito

6.-Model Testing: Evaluamos el modelo, obteniendo una precisión de 16.22%, el área bajo la curva (ROC) es de 0.82. Con la matriz de confusión podemos observar que nuestro modelo necesita mejoras o ajustes adicionales.

<p align="center"><img width="982" alt="Captura de pantalla 2024-11-25 a las 1 53 21 a  m" src="https://github.com/user-attachments/assets/8e6d0a6b-ca81-4823-8ef3-8854e611646c">
<p align="center"><i>Figura 7: Model Testing - resultados





