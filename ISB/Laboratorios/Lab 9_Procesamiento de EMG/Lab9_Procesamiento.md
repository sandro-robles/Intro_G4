# **LABORATORIO 9: – Procesamiento de EMG**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Contexto](#Contexto)
3. [Procesamiento y Preprocesamiento de las señales sEMG](#ProcesamientoyPreprocesamiento)
4. [Equipos y materiales utilizados](#Equipos)
5. [Resultados](#Resultados)
6. [Discusión](#Discusión)
7. [Bibliografia](#Bibliografia)
## **Objetivos:**<a id="Objetivos"></a>
- Revisar la literatura científica sobre técnicas de procesamiento de señales EMG.
- Identificar e implementar el mejor filtrado para eliminar ruido en señales EMG.
- Implementar un proceso de segmentación eficiente para análisis de señales EMG.
- Extraer características relevantes en dominios del tiempo, frecuencia y tiempo-frecuencia.
- Comparar los filtros FIR, IIR y Wavelet para determinar su eficacia en señales EMG.
- Analizar señales EMG adquiridas en laboratorio mediante filtrado y extracción de características.
## **Contexto:**<a id="Contexto"></a>
<p align="justify"> La electromiografía de superficie (EMG) es una técnica utilizada para medir la actividad eléctrica de los músculos durante la contracción, proporcionando información esencial sobre las propiedades fisiológicas y funcionales del músculo. La electromiografía (EMG) se refiere a la señal eléctrica colectiva de los músculos, la cual es controlada por el sistema nervioso y producida durante la contracción muscular. La señal representa las propiedades anatómicas y fisiológicas de los músculos; de hecho, una señal EMG es la actividad eléctrica de las unidades motoras de un músculo, que consisten en dos tipos: EMG de superficie y EMG intramuscular. Las señales EMG de superficie y EMG intramuscular se registran mediante electrodos no invasivos y electrodos invasivos, respectivamente. Hoy en día, las señales detectadas en la superficie se prefieren para obtener información sobre el tiempo o la intensidad de la activación de los músculos superficiales. Las señales de electromiografía (EMG) se consideran las más útiles como señales electrofisiológicas tanto en los campos médicos como en los de ingeniería. El método básico para comprender el comportamiento del cuerpo humano bajo condiciones normales y patológicas se proporciona mediante el registro de señales EMG. Siempre que se registra una señal EMG del músculo, varios tipos de ruidos la contaminan. Por lo tanto, analizar y clasificar las señales EMG es muy difícil debido al patrón complicado de la EMG, especialmente cuando ocurre movimiento [1].</p>

## **Procesamiento y Preprocesamiento de las señales sEMG:**<a id="ProcesamientoyPreprocesamiento"></a>
<p align="justify">El procesamiento de las señales de electromiografía de superficie (sEMG) implica la adquisición de datos eléctricos generados por la actividad muscular, seguido de un conjunto de técnicas para eliminar el ruido, extraer características relevantes y clasificar los datos para diversas aplicaciones, como el control de prótesis, la ergonomía industrial y la interacción humano-máquina [2].</p>

## **Adquisición de señales:**
<p align="justify">Las señales sEMG son capturadas mediante electrodos de superficie. Estos pueden ser secos o húmedos, siendo los secos más adecuados para aplicaciones industriales por su facilidad de uso y mejor biocompatibilidad. Las señales capturadas incluyen la suma de los potenciales de acción de las unidades motoras, por lo que es necesario usar técnicas de filtrado y segmentación para mejorar su precisión[2][3] . </p>

## **Filtrado:**
<p align="justify">Una de las primeras etapas en el procesamiento de sEMG es el filtrado, que reduce el ruido no deseado. Los filtros más comunes son los pasa-bajas y pasa-altas, con frecuencias de corte alrededor de los 20 Hz (para eliminar ruido de baja frecuencia) y entre 400 y 500 Hz (para evitar ruido de alta frecuencia), respectivamente. El uso de filtros Butterworth es común en estos casos debido a su capacidad para eliminar eficazmente las componentes de ruido sin afectar las señales útiles [2][3].</p>

## **Denoising (eliminación de ruido):**
<p align="justify">El denoising es un paso crítico debido a la presencia de ruido de varias fuentes, como la interferencia de la red eléctrica o el movimiento. Los métodos más avanzados para eliminar ruido incluyen la Transformada Wavelet Discreta (DWT) y la transformada de componentes independientes (ICA), que permiten identificar y filtrar eficazmente el ruido manteniendo las características relevantes de la señal[2].</p>

## **Extracción de características:**
<p align="justify">Las señales sEMG deben ser convertidas a representaciones más manejables a través de la extracción de características. Estas características pueden clasificarse en tres dominios:</p>

- Dominio del tiempo: Métricas como la RMS (raíz cuadrada media), valor absoluto medio (MAV), o la integral del cuadrado simple (SSI).
- Dominio de la frecuencia: Características como la frecuencia media (MNF) y la frecuencia mediana (MDF) se usan a menudo para estudios de fatiga muscular [2][3].
- Dominio tiempo-frecuencia: Combinación de análisis temporal y frecuencial, ideal para señales no estacionarias como las sEMG. La transformada wavelet es ampliamente utilizada aquí [3].

## **Segmentación:**
<p align="justify">La segmentación implica dividir la señal en ventanas temporales para facilitar el análisis. Ventanas largas permiten una mejor extracción de características, pero a costa de aumentar el tiempo de procesamiento. En aplicaciones en tiempo real, es común usar ventanas de entre 200 y 300 milisegundos con cierto solapamiento para equilibrar precisión y velocidad [2][3].</p>

## **Clasificación:**
<p align="justify">Las características extraídas de las señales se utilizan para entrenar algoritmos de clasificación, como Máquinas de Soporte Vectorial (SVM), Análisis Discriminante Lineal (LDA), y redes neuronales (ANN). Estos algoritmos permiten identificar patrones en las señales sEMG y asociarlos a movimientos específicos o estados musculares, como la fatiga [3].</p>

<p align="justify">El procesamiento de señales sEMG, aunque potente, presenta desafíos debido a la variabilidad de las señales y la sensibilidad al ruido. Sin embargo, las mejoras en la tecnología de adquisición y en los algoritmos de procesamiento han aumentado su utilidad en aplicaciones industriales y clínicas[3].</p>
