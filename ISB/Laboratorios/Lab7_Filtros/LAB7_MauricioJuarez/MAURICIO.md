# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Objetivos](#t1)
2. [Señales adquiridas](#t2)
2. [Filtros](#t3)
3. [Implementación](#t4)
4. [Resultados](#t5)\
   4.1 [Ejercicio ECG](#t6)\
   4.2 [Ejercicio EMG ](#t7)
5. [Discusión](#t8)\
   5.1 [Señal ECG](#t9)\
   5.2 [Señal EMG](#t10)

## 1. Objetivos  <a name = "t1"></a>
* Analizar las señales obtenidas
* Diseñar filtros para disminuir el ruido de señales adquiridas en laboratorios anteriores de acuerdo a lo analizado
* Filtrar las señales
* Justificar los filtros utilizados

## 2. Señales adquiridas  <a name = "t2"></a>

<p align="justify">En los laboratorios pasados, tuvimos la oportunidad de capturar y adquirir señales de Electromiografía y Electrocardiografía. Dichas señales se pueden observar a continuación

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/EMG/Se%C3%B1alesOriginalesEMG.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 1. Señales adquiridas de electromiografía</i></p>
</p>

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/ECG/Se%C3%B1alesOriginalesECG.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 2. Señales adquiridas de electrocardiograma</i></p>
</p>

<p align="justify">Dadas las imágenes anteriores, se puede observar que la señal cuenta con una cantidad de ruido considerable. Además, de las gráficas de las transformadas de furier (FFT y STFT) podemos ver que la frecuencia del ruido se encuentra muy cercana a la frecuencia de la señal de interés. De las gráficas podemos intentar llegar a un valor intermedio el cual sería una frecuencia de corte que utilizaremos para diseñar los filtros. Dichos filtros ayudarán de manera efectiva la cancelación de gran parte del ruido, lo cual mejorará el display de la señal y diferentes características de la señal podrán ser mejor reconocidas para un análisis fisiológico posterior.

## 3. Filtros  <a name = "t3"></a>
<p align="justify">En este laboratorio utilizaré tanto filtros FIR como IIR. Empezaremos con filtros FIR, por lo tanto se debe elegir el tipo de ventana con la cual vamos a trabajar en nuestro filtro. Para ello, se presentan diferentes ventanas en la siguiente figura: 

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/Ventanas.PNG?raw=true" alt="Ventanas" >
   <p align="center"><i>Tabla 1. Especificaciones de ventanas</i></p>
</p>


<p align="justify">Como se puede observar, existen diferentes ventanas con las cuales se puede trabajar en los filtros FIR. En este laboratorio, utilizaré como primera ventana la ventana Hamming, ya que esta, como se puede ver en la figura, cuenta con una ganancia considerable para pasar las frecuencias de interés, no obstante, cuenta con un ancho de transición un poco elevado, lo que se traduce a que las frecuencias cercanas pasarán sin perder mucho su amplitud. Dicho esto, defino mi frecuencia de corte que será 0.01*pi (wn=0.01pi). Definidos los parámetros, elaboramos el filtro

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/BodeHamming.png?raw=true" alt="Ventanas" >
</p>
<p align="center">
   <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/ZplaneHamming.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 3. Diagrama de Bode y diagrama de ceros y polos del filtro FIR ventana Hamming</i></p>
</p>

<p align="justify">Por otro lado, diseñaremos otro filtro FIR con otra ventana para ver el impacto que esta tiene en nuestras señales. Para ello, utilizaremos una ventana tipo Barlett, la cual cuenta con una menor ganancia para las frecuencias de interés, pero tiene un menor ancho de transición (comparándola con la ventana Hamming. Definimos la misma frecuencia de corte que en el anterior filtro (wn=0.01*pi). Obtenemos lo siguiente:

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/BodeBartlett.png?raw=true" alt="Ventanas" >
</p>

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/ZplaneBartlett.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 4. Diagrama de Bode y diagrama de ceros y polos del filtro FIR ventana Bartlett</i></p>
</p>

<p align="justify">Como último filtro que implementaremos en este laboratorio será un filtro IIR. Estos filtros son más eficientes computacionalmente ya que no cuentan con tantos coeficientes como lo tiene un filtro FIR, lo cual optimiza el espacio de memoria, pero si no se diseñan bien pueden llegar a ser inestables. Utilizo dos frecuencias las cuales serán la passband edge frequency (wp=0.01) y la stopband edge frequencies (ws=0.15). Con ello podemos diseñar nuestro filtro IIR como se muestra en la siguiente figura

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/BodeIIR.png?raw=true" alt="Ventanas" >
</p>

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/ZplaneIIR.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 4. Diagrama de Bode y diagrama de ceros y polos del filtro IIR</i></p>
</p>

## 4. Implementación  <a name = "t4"></a>

<p align="justify">Con la ayuda de los filtros diseñados ya podemos utilizarlos para mejorar nuestra señal adquirida y disminuir el ruido que se haya obtenido para EMG y ECG

<p align="center">
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/EMG/EMG_filtrada.png?raw=true" alt="Ventanas" >
   <p align="center"><i>Figura 5. Señal de EMG filtrada con </i></p>
</p>
