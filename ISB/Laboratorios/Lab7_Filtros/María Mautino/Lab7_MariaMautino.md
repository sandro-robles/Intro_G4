# Laboratorio N°7 - Diseño de Filtros FIR y IIR 
1. [Introducción](#t2)
2. [Objetivos del laboratorio](#t3)
3. [Metodología](#t4)
4. [Resultados](#t5)\
   4.1 [Ejercicio ECG](#t6)\
   4.2 [Ejercicio EMG ](#t7)\
5. [Discusión](#t9)\
   5.1 [Señal ECG](#t10)\
   5.2 [Señal EMG](#t11)\
6. [Bibliografía](#t13)


## Resultados   <a name="t4"></a>

### **Ejercicio ECG** <a name="t6"></a>
| Campo | Señal Cruda | Filtro FIR | Filtro IIR |
|-----------|-----------|-----------|-----------|
| Basal D2  | <img src="Imagenes_L6/Imagenes_ECG/Basal_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_butter.png" alt="Electrodos de guía"  > | <img src="Imagenes_L6/Imagenes_ECG/basal_ECG_hanni.png" alt="Electrodos de guía" >|
| Respiración D1 | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_butt.png" alt="Electrodos de guía" >| <img src="Imagenes_L6/Imagenes_ECG/in_ex_ECG_hanni.png" alt="Electrodos de guía"> |
| Post Respiración D3  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_butt.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_ECG/post_ECG_hann.png" alt="Electrodos de guía"> |
| Post Ejercicio D2  |

<p align="center">
  <b>Tabla 2. Resumen de la señal filtrada con filtros FIR e IIR para la data ECG</b>
</p>


### **Ejercicio EMG** <a name="t7"></a>
| Campo | Señal Cruda | Filtro FIR | Filtro IIR |
|-----------|-----------|-----------|-----------|
| Bícep en Movimiento   | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_butt.png" alt="Electrodos de guía"  > | <img src="Imagenes_L6/Imagenes_EMG/bicep_EMG_black.png" alt="Electrodos de guía" >|
| Trícep en Movimiento | <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_butt.png" alt="Electrodos de guía" >| <img src="Imagenes_L6/Imagenes_EMG/antebrazo_EMG_black.png" alt="Electrodos de guía"> |
|Mano en reposo  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_butt.png" alt="Electrodos de guía">  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_black.png" alt="Electrodos de guía"> |
|Trapecio Movimiento/Fuerza  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_cruda.png" alt="Electrodos de guía" >  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_butt.png" alt="Electrodos de guía">  | <img src="Imagenes_L6/Imagenes_EMG/pulgar_EMG_black.png" alt="Electrodos de guía"> |
|Gastrocnemio Movimiento  |

<p align="center">
  <b>Tabla 3. Resumen de la señal filtrada con filtros FIR e IIR para la data EMG</b>
</p>

