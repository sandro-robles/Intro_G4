# **LABORATORIO 5: – Uso de BITalino para ECG**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Introduccion](#Introduccion)
3. [Equipos y materiales utilizados](#Equipos)
4. [Resultados](#Resultados)
5. [Discusión](#Discusión)
6. [Bibliografia](#Bibliografia)
## **Objetivos:**<a id="Objetivos"></a>
- Adquirir señales biomédicas de ECG.
- Hacer una correcta configuración de BiTalino
- Extraer la información de las señales ECG del software OpenSignals (r)evolution
## **Introducción:**<a id="Introduccion"></a>
<p align="justify"> </p>

<p align="justify"> </p>

<p align="center"><img src="Anexos/EMG.jpg" width="400"></p>

<p align="center"><i>Figura 1: Aplicaciones de la electromiografía en asistencia y rehabilitación [2].</i></p>


## **Equipos y materiales utilizados:**<a id="Equipos"></a>
<div align="center">

## **Resultados:**<a id="Resultados"></a>
<a name="P1"></a>
### 1. Actividad muscular del tríceps según la literatura:
<p align="justify"> En el artículo de Villalba et al. (2024), el enfoque está en medir la actividad EMG del tríceps braquial (cabeza lateral y cabeza larga) durante un ejercicio de tríceps push-down en varias posiciones del antebrazo (supinada y pronada). También se menciona que la cabeza larga del tríceps muestra mayor actividad EMG cuando el antebrazo está en una posición supinada, lo que sugiere una mayor carga sobre este músculo en comparación con la posición pronada. Esto hace que sea importante medir la actividad EMG en ambas posiciones para entender cómo varía la activación muscular y mejorar la eficiencia del ejercicio [3] .

<p align="justify"> En el artículo de Hussain et al., se observa que la fatiga afecta las señales EMG de diferentes maneras, reduciendo las frecuencias medias de potencia (MPF) y mediana (MDF) a medida que se avanza hacia la fatiga. También se observa un aumento en la amplitud del RMS bajo condiciones de fatiga, lo que indica un mayor esfuerzo muscular a medida que el músculo se acerca al fallo [4]. </p>

<p align="center"><img src="Anexos/Tricep paper.png" width="400"></p>

<p align="center"><i>Figura 2: Posición de los electrodos según el protocolo seguido en el paper [4].</i></p>


#### <blockquote> Prueba 01: Tríceps

<p align="center"><img src="Anexos/IMG_tricep.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 3: La medición del EMG del tríceps se realizó con el participante de pie, manteniendo el brazo relajado al costado del cuerpo. Se colocaron electrodos de superficie en la región del tríceps para captar la actividad eléctrica del músculo durante la contracción y el reposo.
</i></p>

<p align="center">
   
|  **Actividad Muscular - Tríceps en reposo** | **Actividad Muscular - Tríceps ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|
|<video src="https://github.com/user-attachments/assets/b501a6a4-6002-4526-81b7-ce0dc513d36a"></video>|<video src="https://github.com/user-attachments/assets/8ff2246f-7f49-48b0-aa0b-53cf2bd35a6a">|
<p align="center"><i>Tabla 2. Videos de adquisición de la señal EMG según dos tomas: en reposo y con el músculo ejerciendo fuerza. </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo y ejerciendo fuerza**|<image src="Anexos/S_triceps.png">|
<p align="center"><i>Tabla 3. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

### 2. Actividad muscular del gastrocnemio según la literatura:
<p align="justify"> En el estudio de Wang et al. (2021), se centra en la medición de la actividad EMG del gastrocnemio durante varias inclinaciones y tipos de marcha (caminar en plano, cuesta arriba, cuesta abajo, y subir/bajar escaleras). Se observa que la actividad EMG del gastrocnemio aumenta progresivamente al caminar cuesta arriba, sugiriendo una mayor activación muscular debido a la mayor demanda de fuerza en comparación con caminar en plano o cuesta abajo. Es importante medir la actividad EMG en estas diferentes condiciones para entender cómo varía la activación muscular y cómo optimizar los movimientos en la rehabilitación o el entrenamiento [5]. </p>

<p align="center"><img src="Anexos/Gastrocnemio paper.png" width="400"></p>

<p align="center"><i>Figura 4: Posición de los electrodos según el protocolo seguido en el paper [5].</i></p>

### 2.1. Diferencias metodológicas:
<p align="justify"> Es importante mencionar que, para esta prueba, buscamos simplificar el análisis de la activación muscular del gastrocnemio imitando la marcha con un solo movimiento: la elevación de pantorrillas. A diferencia del estudio mencionado, nuestro enfoque se centró en capturar la actividad eléctrica del músculo gastrocnemio mediante la flexión plantar, utilizando una elevación controlada. Esta metodología nos permitió medir de manera eficiente la actividad muscular en un entorno controlado, manteniendo el tobillo en una posición neutral y relajada, con los electrodos colocados en la cabeza lateral del gastrocnemio para captar los datos durante el movimiento.</p>
<a name="P2"></a>

#### <blockquote> Prueba 02: Gastrocnemio

<p align="center"><img src="Anexos/IMG_pierna.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 5. La medición del EMG del gastrocnemio se realizó con el participante de pie, manteniendo el tobillo en una posición neutral y relajada. Se colocaron electrodos de superficie en la cabeza lateral del gastrocnemio para captar la actividad eléctrica del músculo durante la flexión plantar.</i></p>

<p align="center">
   
|  **Actividad muscular - Gastrocnemio en reposo** | **Actividad Muscular - Gastrocnemio en movimiento (flexión plantar)** | **Actividad Muscular - Gastrocnemio ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
|<video src="https://github.com/user-attachments/assets/69bd1254-6af8-402e-9ef5-aaed76e18859"></video>|<video src="https://github.com/user-attachments/assets/1bd88350-0676-4097-b603-db53ae502012"></video>|<video src="https://github.com/user-attachments/assets/b8c96a19-02b9-4811-9cc9-4b1174248aca"> | 
<p align="center"><i>
Tabla 4. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo, en movimiento y ejerciendo fuerza**|<image src="Anexos/S_gastro.png">|
<p align="center"><i>Tabla 5. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

<a name="P3"></a>
### 3. Actividad muscular de la mano según la literatura:
<p align="justify"> En el estudio de Dalkilic et al. (2017) se enfoca en la evaluación no invasiva de las ramas del nervio mediano en la mano mediante el método de seguimiento de umbral, una técnica avanzada para medir parámetros de excitabilidad neuronal. Los resultados indicaron alteraciones significativas en la excitabilidad del nervio mediano bajo distintas condiciones, lo que refleja cambios en la actividad neuromuscular que son de particular relevancia para el diagnóstico de neuropatías. Este enfoque es esencial para comprender cómo varía la respuesta electromiográfica (EMG) del nervio mediano durante movimientos funcionales de la mano, y proporciona una base sólida para optimizar estrategias terapéuticas y de rehabilitación. Al evaluar la actividad del nervio mediano, es posible identificar patrones específicos de activación muscular, lo que facilita el diseño de intervenciones más precisas en casos de disfunción neuromuscular [6].</p>

<p align="center"><img src="Anexos/Mano paper.png" width="400"></p>

<p align="center"><i>Figura 6: Posición de los electrodos según el protocolo seguido en el paper [6].</i></p>

#### <blockquote> Prueba 03: Mano / Nervio mediano

<p align="center"><img src="Anexos/IMG_mano.jpeg" width="450" height="300"></p>

<p align="center"><i>Figura 7: La medición del EMG del nervio mediano se realizó con el participante en una posición sentada, manteniendo una postura natural con los codos apoyados en los reposabrazos y la cabeza en una posición neutral para minimizar la interferencia de otros movimientos.</i></p>

<p align="center">
   
|  **Actividad Muscular - Mano/nervio mediano en reposo** | **Actividad Muscular - Mano/nervio mediano en movimiento** | **Actividad Muscular - Mano/nervio mediano ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
| <video src="https://github.com/user-attachments/assets/e188c019-ad6a-4d4c-baf0-48036068a712"> | <video src="https://github.com/user-attachments/assets/750503ff-88bb-4193-a935-c3d0a1321b8b"> | <video src="https://github.com/user-attachments/assets/84ebebe4-5c92-4557-954f-179f88f1f5e8"> | 
<p align="center"><i>Tabla 6. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo, en movimiento y ejerciendo fuerza**|<image src="Anexos/S_mano.png">|
<p align="center"><i>Tabla 7. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

### 4. Actividad muscular del bíceps según la literatura: <a id="P4"></a>
<p align="justify"> En el estudio de Robert W. Smith et al., se evaluaron los cambios en la fatiga muscular y las respuestas neuromusculares en el bíceps braquial después de realizar una contracción isométrica máxima (es decir, mantener una contracción sin mover el brazo) hasta el fallo muscular [7].</p>

<p align="center"><img src="Anexos/Bicep paper.png" width="400"></p>

<p align="center"><i>Figura 8: Posición de los electrodos según el protocolo seguido en el paper [7].</i></p>

#### <blockquote> Prueba 04: Bíceps

<p align="center"><img src="Anexos/IMG_bicep.PNG" width="450" height="300"></p>

<p align="center"><i>Figura 9: La medición del EMG se realizó con el brazo del participante apoyado sobre la mesa, mientras el resto del cuerpo permanecía en una posición sentada sin contacto con la superficie de apoyo, para evitar interferencias externas. Se utilizaron electrodos en el brazo para captar la actividad eléctrica del músculo bíceps durante la contracción.</i></p>

<p align="center">
   
|  **Actividad Muscular - Bíceps  en reposo** | **Actividad Muscular - Bíceps ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|
| <video src="https://github.com/user-attachments/assets/6d9c9523-7049-481b-8242-b2dfcaaf2958"> </video> | <video src="https://github.com/user-attachments/assets/33b24c40-c045-41c5-8eca-b7724281b103"> </video> |

<p align="center"><i>Tabla 8. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del músculo bíceps braquial </i></p>
</p>

<p align="center">
   
| **Posición** | **Señal** |
|:------------:|:---------------:|
| **En reposo y ejerciendo fuerza**|<image src="Anexos/S_biceps.png">|
<p align="center"><i>Tabla 9. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

### 5. Actividad muscular del trapecio según la literatura: <a id="P5"></a>
<p align="justify"> En el estudio de Ahmed et al. (2024), se examina la actividad EMG del trapecio durante pruebas cognitivas que inducen estrés, como el test Stroop y el cálculo mental, así como durante una sesión de meditación guiada. Los resultados muestran que la actividad EMG del trapecio aumenta significativamente durante el estrés en comparación con el reposo y la meditación, especialmente en las frecuencias bajas (0.5–4 Hz). Este estudio también introdujo un método novedoso para evaluar la asimetría en la activación del trapecio entre los lados izquierdo y derecho, encontrando que esta asimetría es útil para detectar estados de estrés y meditación [8].</p>

<p align="center"><img src="Anexos/Trap paper.png" width="400"></p>

<p align="center"><i>Figura 10: Posición de los electrodos según el protocolo seguido en el paper [8].</i></p>

### 5.1. Diferencias metodológicas: <a id="P5"></a>
<p align="justify"> En el estudio mencionado anteriormente, la medición del EMG del músculo trapecio se realizó con el participante en una posición sentada, manteniendo una postura relajada para minimizar interferencias de otros movimientos. Los electrodos de superficie se colocaron bilateralmente en la región del trapecio superior para medir la actividad durante situaciones de reposo, estrés mental y meditación [8]. Sin embargo, en nuestro caso decidimos modificar esta metodología para analizar la actividad eléctrica del músculo durante situaciones de estrés físico, específicamente al realizar ejercicios de elevación de trapecio (encogimiento de hombros).</p>

<p align="justify"> Para replicar esta condición de ejercicio en un entorno controlado, utilizamos una banca del laboratorio como si fuera una barra de gimnasio, permitiendo que los participantes imitaran el movimiento de elevación de trapecio. Esta variación en la metodología nos permitió enfocarnos en el comportamiento del músculo durante una actividad física intensa, a diferencia del estrés mental analizado en el estudio original. Esta modificación es crucial, ya que nuestro interés radica en entender la activación del trapecio en escenarios de esfuerzo físico, no solo en estados de relajación o estrés cognitivo.</p>

#### <blockquote> Prueba 05: Trapecio

<p align="center"><img src="Anexos/IMG_espalda.PNG" width="250" height="350"></p>

<p align="center"><i>Figura 11. La medición del EMG del trapecio se realizó con el participante de pie, imitando el ejercicio de elevación de trapecio (encogimiento de hombros) para analizar la actividad muscular durante situaciones de estrés físico. Se colocaron electrodos de superficie bilateralmente en la región del trapecio superior (izquierdo y derecho) para captar la actividad eléctrica del músculo durante el ejercicio. Los electrodos se posicionaron entre el acromion y la columna cervical (C7), siguiendo la ubicación estándar para estudiar el trapecio superior, un músculo clave en la elevación y estabilidad del hombro.</i></p>

<p align="center">
   
|  **Actividad Muscular - Trapecio en reposo** | **Actividad Muscular - Trapecio en movimiento** | **Actividad Muscular - Trapecio ejerciendo fuerza** |
|:-----------------------------------------------------:|:--------------------------------------------------------:|:---------------------------------------------------------:|
|<video src="https://github.com/user-attachments/assets/973a91c9-eab7-4e0c-b104-2dc0212b3720"></video>|<video src="https://github.com/user-attachments/assets/e402e19e-9ef5-4509-aa88-4fd0fd3adc89"></video>|<video src="https://github.com/user-attachments/assets/3e115637-f0ce-429d-8452-8b26524bb439"> | 
<p align="center"><i>Tabla 10. Videos de adquisición la señal EMG según las tres tomas: en reposo, sin oposición y con oposición del trapecio. </i></p>
<p align="center">
   
| **Posición** | **Seña** |
|:------------:|:---------------:|
| **En reposo, en movimiento y ejerciendo fuerza**|<image src="Anexos/S_trapecio.png">|
<p align="center"><i>Tabla 11. Señales adquiridas en reposo, sin oposición y con oposición graficadas en Python </i></p>

## **Discusión:**<a id="Discusión"></a>
<p align="justify">Para este laboratorio, se utilizó el sistema BITalino para la adquisición de señales EMG, capturando y analizando la actividad en distintos grupos musculares bajo diversas condiciones. La EMG de superficie ofrece una técnica no invasiva para medir la actividad eléctrica muscular, proporcionando información valiosa sobre la fisiología y función de los músculos. Al realizar las pruebas en cada músculo, se observó una variabilidad significativa en las características de activación y las respuestas, lo que demuestra que cada músculo tiene un comportamiento único frente a diferentes condiciones de esfuerzo. Además, cada señal obtenida fue graficada mediante un código en Python, permitiendo visualizar la señal a lo largo del tiempo y asi poder ver los distintos músculos. Estos resultados destacan la importancia de un análisis individual para comprender mejor la función de cada musculo.</p>

## **Bibliografia:**<a id="Bibliografia"></a>
<p align="justify">[1] R. H. Chowdhury, Mamun, Ali, A. Ashrif, Kalaivani Chellappan, and T. G. Chang, “Surface Electromyography Signal Processing and Classification Techniques,” Sensors, vol. 13, no. 9, pp. 12431–12466, Sep. 2013, doi: https://doi.org/10.3390/s130912431.</p>
