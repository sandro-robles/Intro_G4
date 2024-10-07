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
| Gastro en Movimiento |<img width="1064" alt="gastro_mov" src="https://github.com/user-attachments/assets/af5d86d8-f80a-4fd6-b604-73c628ebe227">
|Mano en reposo  | <img width="1064" alt="mano_reposo" src="https://github.com/user-attachments/assets/7b909034-5317-4f81-ab25-5bdee76185d2">

|Trapecio reposo |<img width="1064" alt="trapecio norma" src="https://github.com/user-attachments/assets/c8a05060-d428-465e-b622-38ce31085144">

|Tricep con fuerza | <img width="1064" alt="tricep_fuerza" src="https://github.com/user-attachments/assets/daa0e8ce-e591-455d-a25c-f044b49ec73a">



