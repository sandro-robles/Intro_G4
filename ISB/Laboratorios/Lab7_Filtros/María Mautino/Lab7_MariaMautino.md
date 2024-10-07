# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Introducción](#t1)
2. [Objetivos del laboratorio](#t2)
3. [Metodología](#t3)\
   3.1 [Ejercicio ECG](#t4)\
5. [Resultados](#t5)\
   4.1 [Ejercicio ECG](#t6)\
   4.2 [Ejercicio EMG ](#t7)
6. [Discusión](#t8)\
   5.1 [Señal ECG](#t9)\
   5.2 [Señal EMG](#t10)
7. [Bibliografía](#t11)

## 1. Introducción  <a name = "t1"></a>
<p align="justify">El presente informe tiene como objetivo mostrar el uso de distintos tipos de filtros FIR (Filtro de Respuesta al Impulso Finita), IIR (Filtro de Respuesta al Impulso Infinita) en las señales bioeléctricas de ECG (Electrocardiograma) y EMG (Electromiograma) adquiridas durante las sesiones prácticas. Los filtros son herramientas esenciales que nos permiten modificar una señal con el fin de eliminar ruidos o interferencias y así obtener datos más precisos. En el caso del ECG, utilizado para medir la actividad eléctrica del corazón, y el EMG, que registra la actividad eléctrica generada por los músculos, los filtros juegan un papel importante para mejorar la calidad de las señales y facilitar su interpretación, eliminando perturbaciones como el ruido ambiental o el movimiento [1].</p>

## 2. Objetivos <a name = "t2"></a>
* Utilizar y filtrar señales de EMG y ECG obtenidas previamente, aplicando filtros FIR o IIR.
* Analizar cada señal (original y filtrada) en el dominio del tiempo y la frecuencia.
* Incluir los diagramas de polos y ceros, así como los Diagramas de Bode de los filtros utilizados.
* Justificar la selección de los filtros aplicados.

## 3. Metodología <a name = "t3"></a>
<p align="justify">En este laboratorio, nos enfocamos en desarrollar e implementar filtros digitales FIR e IIR para reducir el ruido de alta frecuencia que afecta las señales de ECG y EMG adquiridas previamente con el Kit BITalino. La finalidad de aplicar estos filtros es limpiar las señales de interferencias no deseadas, mejorando su calidad y precisión para su análisis posterior.
   
### 3.1 **Equipos y materiales utilizados:**<a name = "t4"></a>

<div align="center">
  
| **Modelo**    | **Descripción**          | **Cantidad** |
|---------------|--------------------------|--------------|
| (r)EVOLUTION  | Kit BITalino              | 1            |
| ASUS          | Laptop                    | 1            |
| -             | Electrodos superficiales  | 3            |

</div>

<p align="center"><i>Tabla 1. Equipos y materiales utilizados en este laboratorio.</i></p>


## Resultados   <a name="t5"></a>

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

### **Análisis del Filtro** <a name="t6"></a>
| Filtro | Diagrama de Bode | Diagrama de Polos y Ceros |
|--------|------------------|--------------------------|
| FIR    | <img src="Anexo_Biceps/bode fir.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_Biceps/zeros y polos fir.png" width="400" height="300" style="display:block; margin:auto;"/> |
| IIR    | <img src="Anexo_Biceps/bode iir.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_Biceps/zeros y polos iir.png" width="400" height="300" style="display:block; margin:auto;"/> |

### **Bibliografía:** <a name="t10"></a>
<p align="justify">[1] L. Romero, “Análisis de señales electrocardiográficas usando técnicas de procesamiento digital,” Uoc.edu, 2015, doi: http://hdl.handle.net/10609/40186.</p>
‌


