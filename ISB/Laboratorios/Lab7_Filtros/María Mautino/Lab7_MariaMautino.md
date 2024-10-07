# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Introducción](#t1)\
   1.1 [Filtros Digitales](#t2)\
   1.2 [Filtros FIR](#t3)
      - 1.2.1 [Método de las ventanas](#t4)\
   1.3 [Filtros IIR](#t5)
      - 1.3.1 [Métodos de Diseño de Filtros IIR](#t6)
2. [Objetivos del laboratorio](#t7)
3. [Metodología](#t8)\
   3.1 [Ejercicio ECG](#t9)
4. [Resultados](#t10)\
   4.1 [Ejercicio ECG](#t11)\
   4.2 [Ejercicio EMG](#t12)
5. [Discusión](#t13)\
   5.1 [Señal ECG](#t14)\
   5.2 [Señal EMG](#t15)
6. [Bibliografía](#t16)

## 1. Introducción  <a name = "t1"></a>
<p align="justify">El presente informe tiene como objetivo mostrar el uso de distintos tipos de filtros FIR (Filtro de Respuesta al Impulso Finita), IIR (Filtro de Respuesta al Impulso Infinita) en las señales bioeléctricas de ECG (Electrocardiograma) y EMG (Electromiograma) adquiridas durante las sesiones prácticas. Los filtros son herramientas esenciales que nos permiten modificar una señal con el fin de eliminar ruidos o interferencias y así obtener datos más precisos. En el caso del ECG, utilizado para medir la actividad eléctrica del corazón, y el EMG, que registra la actividad eléctrica generada por los músculos, los filtros juegan un papel importante para mejorar la calidad de las señales y facilitar su interpretación, eliminando perturbaciones como el ruido ambiental o el movimiento [1].</p>

### 1.1 Filtros Digitales:  <a name = "t2"></a>
<p align="justify">Un filtro digital es un sistema que procesa señales aplicando operaciones matemáticas sobre una señal previamente muestreada ,es decir, una señal continua convertida en una secuencia de valores discretos. Esta señal discreta no tiene un valor en todos los instantes de tiempo, ya que está cuantificada. Además, al ser una señal digital, representa físicamente una secuencia de valores discretos, como puede ser un flujo de bits o una señal analógica que ha sido digitalizada [2].</p>

### 1.2 Filtros FIR:  <a name = "t3"></a>
<p align="justify">Los filtros FIR, conocidos como filtros no recursivos, tienen una respuesta finita al impulso, lo que significa que su salida depende únicamente de las entradas actuales y no de las salidas anteriores. Este tipo de filtro es muy estable y garantiza una fase lineal, lo que los hace ideales para aplicaciones en las que la precisión de la fase es importante. Al aplicar la convolución, el filtro FIR realiza un promedio ponderado de las muestras de entrada, y su salida eventualmente desaparece cuando las entradas se reducen a cero. Debido a su estabilidad y predictibilidad, los filtros FIR son ampliamente utilizados en aplicaciones como procesamiento de audio, mejora de imágenes y sistemas de comunicación, donde se requiere un control preciso de la frecuencia [3].</p>
<p align="center"><img src="Anexo_Biceps/Filtro-FIR-estructura-basica.png" width="500"></p>
<p align="center"><i>Figura 1:Estructura básica de un filtro FIR [4].</i></p>

#### 1.2.1 Método de las ventanas:  <a name = "t4"></a>
<p align="justify">El diseño de filtros FIR mediante el método de ventanas se basa en modificar la respuesta al impulso de un filtro ideal para obtener un filtro realizable y causal. Primero, se obtiene la respuesta al impulso de un filtro ideal (como paso bajo o paso alto), que es infinita en el tiempo. Luego, se aplica una ventana para truncar esa respuesta y limitarla a una longitud finita. Las ventanas, como las de Hamming o Blackman, ayudan a suavizar los bordes de la señal truncada, mejorando la atenuación de frecuencias no deseadas. Finalmente, la respuesta al impulso se desplaza en el tiempo para hacerla causal, es decir, para garantizar que el filtro sea físicamente implementable en un sistema real. Este método es sencillo y permite diseñar filtros con características controlables, aunque no es tan preciso como otros métodos más avanzados [5].</p>
<p align="center"><img src="Anexo_Biceps/Captura de pantalla 2024-10-06 194845.png" width="500"></p>
<p align="center"><i>Figura 2: Respuesta en frecuencia y valores de ponderación de diferentes tipos de ventanas. [6].</i></p>

### 1.3 Filtros IIR:  <a name = "t5"></a>
<p align="justify">Por otro lado, los filtros IIR son recursivos y tienen una respuesta al impulso infinita, ya que la salida depende tanto de las entradas actuales como de las salidas previas. Esto les permite ser más eficientes en términos computacionales, ya que pueden lograr un filtrado similar a los FIR con menos coeficientes. Sin embargo, los filtros IIR pueden introducir distorsiones de fase y ser susceptibles a inestabilidad si no se diseñan adecuadamente. Estos filtros son preferidos en aplicaciones donde se requiere un procesamiento rápido y eficiente, como en el procesamiento de señales biomédicas (por ejemplo, ECG y EEG), sistemas de control y algoritmos de compresión de audio y voz, donde se necesita una respuesta rápida y eficaz [3].</p>
<p align="center"><img src="Anexo_Biceps/Esquema-general-de-un-sistema-de-filtro-IIR-con-estructura-Directa-tipo-I.png" width="500"></p>
<p align="center"><i>Figura 2:Esquema general de un filtro IIR [7].</i></p>

#### 1.3.1 Métodos de Diseño de Filtros IIR: <a name = "t6"></a> 
<p align="justify"> Los diferentes tipos de filtros IIR se utilizan según las necesidades de suavidad, selectividad y tolerancia a ondulaciones en las bandas de paso o de stop, dependiendo de la aplicación en la que se empleen [8].
   
* Butterworth: Ideal para una respuesta de frecuencia suave, sin ondulaciones, y cuando no se necesita alta selectividad.
* Chebyshev Tipo I: Alta selectividad con ondulaciones en la banda de paso, útil cuando las ondulaciones no son un problema.
* Chebyshev Tipo II: Alta selectividad con ondulaciones en la banda de stop, aplicable cuando se requiere una banda de paso suave.
* Elíptico: Alta selectividad con ondulaciones en ambas bandas, adecuado cuando se puede tolerar algo de distorsión a cambio de una transición rápida. </p>


| **Filtro**           | **Imagen**                                                                                             |
|----------------------|-------------------------------------------------------------------------------------------------------|
| Butterworth: Ideal para una respuesta de frecuencia suave, sin ondulaciones, y cuando no se necesita alta selectividad [8].  | <div align="center"><img src="Anexo_Biceps/Captura de pantalla 2024-10-06 203600.png" width="200" height="150"></div> |
| Chebyshev Tipo I:  Alta selectividad con ondulaciones en la banda de paso, útil cuando las ondulaciones no son un problema [8]. | <div align="center"><img src="Anexo_Biceps/Captura de pantalla 2024-10-06 203543.png" width="200" height="150"></div> |
| Chebyshev Tipo II:Alta selectividad con ondulaciones en la banda de stop, aplicable cuando se requiere una banda de paso suave [8].| <div align="center"><img src="Anexo_Biceps/Captura de pantalla 2024-10-06 203617.png" width="200" height="150"></div> |
| Elíptico: Alta selectividad con ondulaciones en ambas bandas, adecuado cuando se puede tolerar algo de distorsión a cambio de una transición rápida [8].      | <div align="center"><img src="Anexo_Biceps/Captura de pantalla 2024-10-06 203632.png" width="200" height="150"></div> |

## 2. Objetivos <a name = "t7"></a>
* Utilizar y filtrar señales de EMG y ECG obtenidas previamente, aplicando filtros FIR o IIR.
* Analizar cada señal (original y filtrada) en el dominio del tiempo y la frecuencia.
* Incluir los diagramas de polos y ceros, así como los Diagramas de Bode de los filtros utilizados.
* Justificar la selección de los filtros aplicados.

## 3. Metodología <a name = "t8"></a>
<p align="justify">En este laboratorio, nos enfocamos en desarrollar e implementar filtros digitales FIR e IIR para reducir el ruido de alta frecuencia que afecta las señales de ECG y EMG adquiridas previamente con el Kit BITalino. La finalidad de aplicar estos filtros es limpiar las señales de interferencias no deseadas, mejorando su calidad y precisión para su análisis posterior.
   
### 3.1 **Equipos y materiales utilizados:**<a name = "t9"></a>

<div align="center">
  
| **Modelo**    | **Descripción**          | **Cantidad** |
|---------------|--------------------------|--------------|
| (r)EVOLUTION  | Kit BITalino              | 1            |
| ASUS          | Laptop                    | 1            |
| -             | Electrodos superficiales  | 3            |

</div>

<p align="center"><i>Tabla 1. Equipos y materiales utilizados en este laboratorio.</i></p>


## Resultados   <a name="t10"></a>

### **Ejercicio ECG** <a name="t5"></a>
| Campo | Señal Cruda | Filtro FIR | Filtro IIR |
|-----------|-----------|-----------|-----------|
| Basal D2  | <img src="Imagenes_L6/Imagenes_ECG/Basal_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_butter.png" alt="Electrodos de guía"  > | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_hanni.png" alt="Electrodos de guía" >|
| Respiración D1 | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_butt.png" alt="Electrodos de guía" >| <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_hanni.png" alt="Electrodos de guía"> |
| Post Respiración D3  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_butt.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_hann.png" alt="Electrodos de guía"> |
| Post Ejercicio D2  |

<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG</b>
</p>


### **Ejercicio EMG** <a name="t6"></a>
| Campo | Señal Cruda vs Filtro FIR | Señal Cruda vs Filtro IIR |
|-----------|-----------|-----------|
| Bícep en Movimiento   | <img src="Anexo_Biceps/señalbicep movimiento(FIR).PNG">  | <img src="Anexo_Biceps/señal bicep movimiento (IIR).png"  > 
| Trícep en Movimiento | <img src="Anexo_Biceps/señal tricep en movimiento (FIR).PNG" > | <img src="Anexo_Biceps/Señal tricep en mov (IIR).png" >| 
|Mano en reposo  | <img src="Anexo_Biceps/señal mano reposo.png" > | <img src="Anexo_Biceps/mano reposo senañ (IIR).png" >| 
|Trapecio Movimiento/Fuerza  | <img src="Anexo_Biceps/señal trapecio en mov firr.png" > | <img src="Anexo_Biceps/señla trapecio movimiento fuerza (IIR).png" >| 
|Gastrocnemio Movimiento  |<img src="Anexo_Biceps/señal gastro.png" > | <img src="Anexo_Biceps/gastromov señal (IIR).png" >| 

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG</b>
</p>

### **Ejercicio EMG - FFT** <a name="t6"></a>
| Campo | FFT - Original | FFT - FIR | FFT - IIR |
|-----------|-----------|-----------|-----------|
| Bícep en Movimiento   | <img src="Anexo_Biceps/fft bicep movimiento.png">  | <img src="Anexo_Biceps/fft bicep movimiento (fir).png">  | <img src="Anexo_Biceps/fftbicepmovimiento_iir.png">  |
| Trícep en Movimiento | <img src="Anexo_Biceps/ftt tricep en movimiento.png">  | <img src="Anexo_Biceps/fft ftt tricep en movimiento (FIR).png">  | <img src="Anexo_Biceps/fft tricep en movimiento (IIR).png">  |
|Mano en reposo  |  <img src="Anexo_Biceps/fft mano reposo.png">  | <img src="Anexo_Biceps/fft mano reposo (FIR).png">  | <img src="Anexo_Biceps/fft mano reposo (IIR).png">  |
|Trapecio Movimiento/Fuerza  |  <img src="Anexo_Biceps/fft trapecio movimiento fuerza.png">  | <img src="Anexo_Biceps/fft trapecio movimiento fuerza (FIR).png">  | <img src="Anexo_Biceps/fft trapecio movimiento fuerza (IIR).png">  |
|Gastrocnemio Movimiento  | <img src="Anexo_Biceps/fft_gastro.png">  | <img src="Anexo_Biceps/fft_gastro (FIR).png">  | <img src="Anexo_Biceps/fft gastromov (IIR).png">  |

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG</b>
</p>

### **Análisis del Filtro** <a name="t11"></a>
| Filtro | Diagrama de Bode | Diagrama de Polos y Ceros |
|--------|------------------|--------------------------|
| FIR    | <img src="Anexo_Biceps/bode fir.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_Biceps/zeros y polos fir.png" width="400" height="300" style="display:block; margin:auto;"/> |
| IIR    | <img src="Anexo_Biceps/bode iir.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_Biceps/zeros y polos iir.png" width="400" height="300" style="display:block; margin:auto;"/> |

### **Bibliografía:** <a name="t12"></a>
<p align="justify">[1] L. Romero, “Análisis de señales electrocardiográficas usando técnicas de procesamiento digital,” Uoc.edu, 2015, doi: http://hdl.handle.net/10609/40186.</p>
<p align="justify">[2] DEWESoft d.o.o, “Signal filtering, Signal suppression, Signal processing | Dewesoft,” Dewesoft.com, 2023. https://training.dewesoft.com/online/course/filters (accessed Oct. 06, 2024).</p>
<p align="justify"> [3] Hardware, “Hardware and Systems Engineering Design - FIR vs IIR Digital Filter,” Hwe.design, 2024. https://www.hwe.design/theories-concepts/signal-processing/fir-vs-iir-digital-filter (accessed Oct. 06, 2024).</p>
<p align="justify"> [4] Figura 2-2. Filtro FIR, estructura básica,” ResearchGate, 2024. https://www.researchgate.net/figure/Figura-2-2-Filtro-FIR-estructura-basica_fig1_335241476 (accessed Oct. 06, 2024).</p
<p align="justify"> [5] “Jaime Ramirez Grupo 11-Tarea 4 - Tarea 4 - Realizar simulaciones de filtros aplicando herramientas - Studocu,” Studocu, 2020. https://www.studocu.com/co/document/universidad-nacional-abierta-y-a-distancia/tratamiento-de-imagenes/jaime-ramirez-grupo-11-tarea-4/39937696 (accessed Oct. 07, 2024).‌</p>
<p align="justify"> [6] “FIR Filters by Windowing - The Lab Book Pages,” Labbookpages.co.uk, 2024. http://www.labbookpages.co.uk/audio/firWindowing.html (accessed Oct. 07, 2024).‌</p>
<p align="justify"> [7] “Figura 5-7.: Esquema general de un sistema de filtro IIR con estructura...,” ResearchGate, 2016. https://www.researchgate.net/figure/Figura-5-7-Esquema-general-de-un-sistema-de-filtro-IIR-con-estructura-Directa-tipo-I_fig58_323019453 (accessed Oct. 06, 2024).‌</p>
‌<p align="justify"> [8] “Métodos de diseño filtros IIR,” SlideShare, 2023. https://es.slideshare.net/slideshow/mtodos-de-diseo-filtros-iir/257404855 (accessed Oct. 07, 2024).</p>
‌


