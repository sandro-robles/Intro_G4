# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
## **Tabla de contenidos:**
1. [Objetivos](#t1)
2. [Señales adquiridas](#t2)
2. [Filtros](#t3)
3. [Metodología](#t4)
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
  <img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/Ventanas.PNG?raw=true" alt="Ventanas" >
</p>


## 3. Filtros  <a name = "t3"></a>
<p align="justify">En este laboratorio utilizaré tanto filtros FIR como IIR. Empezaremos con filtros FIR y para ello se debe elegir el tipo de ventana con la cual vamos a trabajar en nuestro filtro. Para ello, se presentan diferentes ventanas en la siguiente figura: 

<img src="https://github.com/sandro-robles/Intro_G4/blob/main/ISB/Laboratorios/Lab7_Filtros/LAB7_MauricioJuarez/Anexo/Ventanas.PNG?raw=true" alt="Ventanas" >

<p align="center"><i>Tabla 1. Especificaciones de ventanas</i></p>

<p align="justify">Como se puede observar, existen diferentes ventanas con las cuales se puede trabajar en los filtros FIR. En este laboratorio, utilizaré como primera ventana la ventana Hamming, ya que esta, como se puede ver en la 

<p align="justify">En este laboratorio, nos enfocamos en desarrollar e implementar filtros digitales FIR e IIR para reducir el ruido de alta frecuencia que afecta las señales de ECG y EMG adquiridas previamente con el Kit BITalino. La finalidad de aplicar estos filtros es limpiar las señales de interferencias no deseadas, mejorando su calidad y precisión para su análisis posterior.
