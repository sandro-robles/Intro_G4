# **LABORATORIO 10: – Procesamiento de ECG**
## **Tabla de contenidos:**
1. [Objetivos](#objetivos)
2. [Contexto](#contexto)
3. [Procesamiento y Preprocesamiento de las señales sEMG](#procesamiento-y-preprocesamiento-de-las-señales-semg)
   1. [Adquisición de señales](#1-adquisicion-de-senales)
   2. [Filtrado](#2-filtrado)
   3. [Denoising (eliminación de ruido)](#3-denoising)
   4. [Extracción de características](#4-extraccion-de-caracteristicas)
   5. [Segmentación](#5-segmentacion)
   6. [Clasificación](#6-clasificacion)
4. [Equipos y materiales utilizados](#equipos)
5. [Metodología](#metodología)
6. [Características del dominio del tiempo](#caracteristicas)
7. [Código](#codigo)
   1. [Reposo](#reposo)
   2. [Fuerza](#fuerza)
   3. [Movimiento](#movimiento)
8. [Resultados](#resultados)
9. [Discusión](#discusion)
10. [Bibliografía](#bibliografia)

   
## **Objetivos:**<a id="Objetivos"></a>

-Hallar los valores normales variabilidad de la frecuencia cardiaca (HRV), basados en un artículo base.

-Plotear los picos de la onda R de las señales de ECG antes tomadas y graficarlas utilizando python.

## **Contexto**<a id="Contexto"></a>

El electrocardiograma (ECG) permite medir la actividad eléctrica del corazón mediante la instalación de una serie de electrodos en el tórax del paciente. Este procedimiento, llevado a cabo con un electrocardiógrafo, registra los impulsos eléctricos emitidos por el corazón y posibilita la evaluación de su funcionamiento. No obstante, las fluctuaciones cardíacas están condicionadas por los procesos respiratorios de inspiración y espiración, además de ser reguladas por la actividad de los sistemas nerviosos simpático y parasimpático. Para el análisis de estas variaciones se utiliza la medición del intervalo R-R, cuya variabilidad temporal se conoce como Variabilidad de la Frecuencia Cardíaca (HRV). Estudios recientes han encontrado que una HRV elevada se asocia con mayores niveles de consumo de oxígeno, mientras que una HRV reducida se correlaciona con un incremento en la mortalidad y un mayor riesgo de desarrollar patologías cardíacas en individuos asintomáticos. Investigaciones adicionales han propuesto que la HRV depende del funcionamiento del Sistema Nervioso Autónomo (SNA) y de otros sistemas fisiológicos de regulación[1].

<p align="center"><img width="519" alt="representacion de " src="https://github.com/user-attachments/assets/f9f254c6-5ba7-47b7-9b3f-73423716fbe0">

<p align="center"><i>Figura 1.  Representación esquemática de un intervalo R­R [1] </i></div>


## **Bibliografía**<a id="Bibliografía"></a>
[1] J.-E. Ortiz-Guzman and D. Mendoza-Romero, “VARIABILIDAD DE LA FRECUENCIA CARDIACA. UNA HERRAMIENTA UTIL,” 2017. Accessed: Oct. 30, 2024. [Online]. Available: https://www.researchgate.net/profile/Dario-Mendoza Romero/publication/303926557_VARIABILIDAD_DE_LA_FRECUENCIA_CARDIACA_UNA_HERRAMIENTA_UTIL/links/58a0e015aca272046aad62c2/VARIABILIDAD-DE-LA-FRECUENCIA-CARDIACA-UNA-HERRAMIENTA-UTIL.pdf
‌
