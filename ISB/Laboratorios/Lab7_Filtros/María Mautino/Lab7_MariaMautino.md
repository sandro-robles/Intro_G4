# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Introducción](#t1)
2. [Objetivos del laboratorio](#t2)
3. [Metodología](#t3)
4. [Resultados](#t4)\
   4.1 [Ejercicio ECG](#t5)\
   4.2 [Ejercicio EMG ](#t6)
5. [Discusión](#t7)\
   5.1 [Señal ECG](#t8)\
   5.2 [Señal EMG](#t9)
6. [Bibliografía](#t10)

## Introducción  <a name = "t1"></a>

## Resultados   <a name="t4"></a>

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
| Filtro | Diagrama de Bode | Diagrama de Polos y Zeros |
|-----------|-----------|-----------|
| FIR   | <img src="Anexo_Biceps/bode fir.png" width="400"/>  | <img src="Anexo_Biceps/zeros y polos fir.png" width="400"/>  |
| IIR   | <img src="Anexo_Biceps/bode iir.png" width="400"/>  | <img src="Anexo_Biceps/zeros y polos iir.png" width="400"/>  | 

