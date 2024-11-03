# **LABORATORIO 10: – Procesamiento de ECG**
## **Tabla de contenidos:**
1. [Objetivos](#objetivos)
2. [Introducción](#introducción)
3. [Procesamiento y Preprocesamiento de las señales ECG](#procesamiento-y-preprocesamiento-de-las-señales-ecg)
4. [Equipos y materiales utilizados](#equipos)
5. [Metodología](#metodología)
6. [Resultados](#resultados)
7. [Bibliografía](#bibliografia)

   
## **Objetivos:**<a id="Objetivos"></a>

-Hallar los valores normales variabilidad de la frecuencia cardiaca (HRV), basados en un artículo base.

-Plotear los picos de la onda R de las señales de ECG antes tomadas y graficarlas utilizando python.

## **Introducción**<a id="Contexto"></a>

El electrocardiograma (ECG) permite medir la actividad eléctrica del corazón mediante la instalación de una serie de electrodos en el tórax del paciente. Este procedimiento, llevado a cabo con un electrocardiógrafo, registra los impulsos eléctricos emitidos por el corazón y posibilita la evaluación de su funcionamiento. No obstante, las fluctuaciones cardíacas están condicionadas por los procesos respiratorios de inspiración y espiración, además de ser reguladas por la actividad de los sistemas nerviosos simpático y parasimpático. Para el análisis de estas variaciones se utiliza la medición del intervalo R-R, cuya variabilidad temporal se conoce como Variabilidad de la Frecuencia Cardíaca (HRV). Estudios recientes han encontrado que una HRV elevada se asocia con mayores niveles de consumo de oxígeno, mientras que una HRV reducida se correlaciona con un incremento en la mortalidad y un mayor riesgo de desarrollar patologías cardíacas en individuos asintomáticos. Investigaciones adicionales han propuesto que la HRV depende del funcionamiento del Sistema Nervioso Autónomo (SNA) y de otros sistemas fisiológicos de regulación[1].

<p align="center"><img width="519" alt="representacion de " src="https://github.com/user-attachments/assets/f9f254c6-5ba7-47b7-9b3f-73423716fbe0">

<p align="center"><i>Figura 1.  Representación esquemática de un intervalo R­R [1] </i></div>

## **Equipos y materiales utilizados**<a id="Contexto"></a>
|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
|      Laptop      | Una laptop equipada con Python, un lenguaje de programación versátil y poderoso, es ideal para realizar tareas de programación y análisis de datos en entornos de laboratorio. |![compu](https://github.com/user-attachments/assets/a8b3848f-b1c6-488a-83de-f8afd5b9ca90)


</div>

## **Resultados**<a id="Resultados"></a>
### **Primera derivación:**
#### **Reposo:**
<p align="center"><img src="Anexos/D1_1.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D1_2.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D1_3.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D1_4.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>

#### **Post ejercicio:**
<p align="center"><img src="Anexos/D1_5.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D1_6.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D1_7.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D1_8.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>

### **Segunda derivación:**
#### **Reposo:**
<p align="center"><img src="Anexos/D2_1.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D2_2.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D2_3.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D2_4.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>

#### **Post ejercicio:**
<p align="center"><img src="Anexos/D2_5.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D2_6.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D2_7.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D2_8.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>

### **Tercera derivación:**
#### **Reposo:**
<p align="center"><img src="Anexos/D3_1.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D3_2.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D3_3.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D3_4.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>

#### **Post ejercicio:**
<p align="center"><img src="Anexos/D3_5.png"></p>
<p align="center"><i>Figura 2.Filtrado de la señal ECG.</i></p>

<p align="center"><img src="Anexos/D3_6.png"></p>
<p align="center"><i>Figura 3.Identifiación de picos R en la señal ECG. </i></p>

<p align="center"><img src="Anexos/D3_7.png"></p>
<p align="center"><i>Figura 4. Ploteo de la señal ECG con función ecg_plot().</i></p>

<p align="center"><img src="Anexos/D3_8.png"></p>
<p align="center"><i>Figura 5. Señal ECG en papel para electrocardiagrama.</i></p>



## **Bibliografía**<a id="Bibliografía"></a>
[1] J.-E. Ortiz-Guzman and D. Mendoza-Romero, “VARIABILIDAD DE LA FRECUENCIA CARDIACA. UNA HERRAMIENTA UTIL,” 2017. Accessed: Oct. 30, 2024. [Online]. Available: https://www.researchgate.net/profile/Dario-Mendoza Romero/publication/303926557_VARIABILIDAD_DE_LA_FRECUENCIA_CARDIACA_UNA_HERRAMIENTA_UTIL/links/58a0e015aca272046aad62c2/VARIABILIDAD-DE-LA-FRECUENCIA-CARDIACA-UNA-HERRAMIENTA-UTIL.pdf
‌
