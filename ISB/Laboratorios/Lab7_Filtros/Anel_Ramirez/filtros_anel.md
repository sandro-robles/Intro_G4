# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Introducción](#t1)
1. [Objetivos del laboratorio](#t2)
4. [Resultados](#t3)\
   3.1 [Ejercicio EMG](#t4)\
   3.2 [Ejercicio ECG ](#t5)
5. [Discusión](#t6)\
   4.1 [Señal ECG](#t7)\
   4.2 [Señal EMG](#t8)
## Introducción <a name= "t1"></a>
<p align="justify">En este informe se presentará un análisis detallado de señales bioeléctricas utilizando filtros digitales. Se trabajará con señales de EMG (Electromiograma) y ECG (Electrocardiograma) obtenidas en las sesiones anteriores. Las señales serán procesadas mediante filtros FIR (Filtro de Respuesta al Impulso Finita) o IIR (Filtro de Respuesta al Impulso Infinita), y se incluirán gráficas que representen tanto la señal original como la filtrada en el dominio del tiempo y la frecuencia, así como la transformada corta de Fourier.Estos filtros son importantes para procesar las señales y suprimir ruidos o interferencias, lo que permite obtener mediciones más precisas. En el caso del ECG, que registra la actividad eléctrica del corazón, y del EMG, que mide la actividad eléctrica de los músculos, los filtros cumplen una función esencial al optimizar la calidad de las señales y facilitar su interpretación, eliminando perturbaciones como el ruido de fondo o el movimiento.
   
## Objetivos  <a name = "t2"></a>
- Utilizar las señales EMG y ECG obtenidas en las sesiones anteriores
- Seleccionar una señal de cada actividad realizada para EMG y ECG
- Las señales deben ser filtradas utilizando filtros FIR o IIR
- Incluir diagramas de polos y zeros

## Resultados <a name="t3"></a>
### **Ejercicio - EMG** <a name="t4"></a>
| Campo | FFT - STFT- FIR - IIR |
|-----------|-----------------------------|
| Bícep fuerza   |<img width="1064" alt="BICEP_fuerza" src="https://github.com/user-attachments/assets/bebe8da1-1001-4a63-a435-bf4c94b6a920">

| Gastro en Movimiento | <img src="Anexo_Biceps/ftt tricep en movimiento.png">  | <img src="Anexo_Biceps/fft ftt tricep en movimiento (FIR).png">  | <img src="Anexo_Biceps/fft tricep en movimiento (IIR).png">  |
|Mano en reposo  |  <img src="Anexo_Biceps/fft mano reposo.png">  | <img src="Anexo_Biceps/fft mano reposo (FIR).png">  | <img src="Anexo_Biceps/fft mano reposo (IIR).png">  |
|Trapecio reposo |  <img src="Anexo_Biceps/fft trapecio movimiento fuerza.png">  | <img src="Anexo_Biceps/fft trapecio movimiento fuerza (FIR).png">  | <img src="Anexo_Biceps/fft trapecio movimiento fuerza (IIR).png">  |
|Tricep con fuerza | <img src="Anexo_Biceps/fft_gastro.png">  | <img src="Anexo_Biceps/fft_gastro (FIR).png">  | <img src="Anexo_Biceps/fft gastromov (IIR).png">  |


