# **LABORATORIO 9: – Procesamiento de EMG**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Contexto](#Contexto)
3. [Equipos y materiales utilizados](#Equipos)
4. [Resultados](#Resultados)
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
