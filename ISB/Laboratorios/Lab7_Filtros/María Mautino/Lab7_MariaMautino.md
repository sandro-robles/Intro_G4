

## 4. Resultados   <a name="t10"></a>

### **Señales ECG** <a name="t5"></a>
| Campo |  Señal Cruda vs Filtro FIR  |  Señal Cruda vs Filtro IIR |
|-----------|-----------|-----------|
| Basal D2  |  <img src="Anexo_ECG/señal REPOSO ECG D2 fir.png">  | <img src="Anexo_ECG/señal REPOSO ECG D2 iir.png"  > |
| Respiración D1 |  <img src="Anexo_ECG/señal RESPIRACON D1 fir.png">  | <img src="Anexo_ECG/señal RESPIRACON D1 iir.png"  > |
| Post Respiración D3  |  <img src="Anexo_ECG/POST RESPIRACION D3 señal fir.png">  | <img src="Anexo_ECG/señal POST RESPIRACION D3 iir.png"  > |
| Post Ejercicio D2  |  <img src="Anexo_ECG/señal EJERCICIO D2 fir.png">  | <img src="Anexo_ECG/señal EJERCICIO D2 iiir.png"  > |

<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG.</b>
</p>

### **Señales EMG - FFT** <a name="t6"></a>
| Campo | FFT - Original vs FIR| FFT - Original vs IIR |
|-----------|-----------|-----------|
| Basal D2  |  <img src="Anexo_ECG/fft REPOSO ECG D2 fir.png">  | <img src="Anexo_ECG/fft REPOSO ECG D2 iir.png"  > |
| Respiración D1 |  <img src="Anexo_ECG/fft RESPIRACON D1 fir.png">  | <img src="Anexo_ECG/fft RESPIRACON D1 iir.png"  > |
| Post Respiración D3  |  <img src="Anexo_ECG/fft POST RESPIRACION D3 fir.png">  | <img src="Anexo_ECG/fft POST RESPIRACION D3 iir.png"  > |
| Post Ejercicio D2  |  <img src="Anexo_ECG/fft EJERCICIO D2 fir.png">  | <img src="Anexo_ECG/fft EJERCICIO D2 iir.png"  > |

### **Análisis del Filtro - ECG** <a name="t11"></a>
| Filtro | Diagrama de Bode | Diagrama de Polos y Ceros |
|--------|------------------|--------------------------|
| FIR    | <img src="Anexo_ECG/bode.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_ECG/462244521_554943407211659_5770730214108742256_n.png" width="400" height="300" style="display:block; margin:auto;"/> |
| IIR    | <img src="Anexo_ECG/Bode iir (2).png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_ECG/Polos y zeros iir.png" width="400" height="300" style="display:block; margin:auto;"/> |


### **Señales EMG** <a name="t6"></a>
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

### **Señales EMG - FFT** <a name="t6"></a>
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

### **Análisis del Filtro - EMG** <a name="t11"></a>
| Filtro | Diagrama de Bode | Diagrama de Polos y Ceros |
|--------|------------------|--------------------------|
| FIR    | <img src="Anexo_ECG/bodefiremg.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_ECG/zerosfiremg.png" width="400" height="300" style="display:block; margin:auto;"/> |
| IIR    | <img src="Anexo_ECG/bodeiiremg.png" width="400" height="300" style="display:block; margin:auto;"/> | <img src="Anexo_ECG/zerosiiremg.png.png" width="400" height="300" style="display:block; margin:auto;"/> |

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


