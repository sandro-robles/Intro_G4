## **Metodologia:**<a id="Objetivos"></a>
<p align="justify">De la data obtenido en los laboratorios anteriores ahora pasamos a la parte de preosesrla mediante la implemtacion de diferentes filtros y asi eliminar el ruido que puede haber en ella.</p>

### **EMG:**<a id="EMG"></a>
<p align="center"><img src="Anexos/IMG_mano.jpeg" width="400"></p>
<p align="center"><i>Figura 1: Imagen de la adquision de la señal EMG.</i></p>

| **Descripcion de la señal** | **Señal obtenida y su FFT** |
|:------------:|:---------------:|
|Señal EMG del biceps | <img src="Anexos/L1.png" > |
|Señal EMG del gastrocnemio | <img src="Anexos/L2.png" > |
|Señal EMG de la mano | <img src="Anexos/L3.png" > |
|Señal EMG del trapecio | <img src="Anexos/L4.png" > |
|Señal EMG del triceps | <img src="Anexos/L5.png" > |
<p align="center"><i>Tabla 1. Señales EMG adquiridas en el laboratorio 4. </i></p>
</p>

### **ECG:**<a id="ECG"></a>
<p align="center"><img src="Anexos/IMG_mano.png" width="400"></p>
<p align="center"><i>Figura 2: Imagen de la adquision de la señal ECG.</i></p>

| **Descripcion de la señal** | **Señal obtenida y su FFT** |
|:------------:|:---------------:|
|Señal ECG en estado de reposo | <img src="Anexos/L6.png" > |
|Señal ECG en estado de respiración prolongada | <img src="Anexos/L7.png" > |
|Señal ECG en estado de dost - Respiración | <img src="Anexos/L8.png" > |
|Señal ECG en estado luego de actividad física | <img src="Anexos/L9.png" > |
<p align="center"><i>Tabla 2. Señales ECG adquiridas en el laboratorio 5. </i></p>
</p>

## **Resultados:**<a id="Resultados"></a>
<p align="justify">Se aplicaron tres diferentes filtros a las señales EMG como para las señales ECG obtenidas.</p>

### **EMG:**<a id="EMG"></a>

| **Descripcion de la señal** | **Filtro IIR** | **Filtro FIR** | **Filtro FIR** |
|:------------:|:---------------:|:---------------:|:---------------:|
|Señal EMG del biceps | <img src="Anexos/F1_1.png" > | <img src="Anexos/F1_2.png" > | <img src="Anexos/F1_3.png" > |
|Señal EMG del gastrocnemio | <img src="Anexos/F2_1.png" > | <img src="Anexos/F2_2.png" > | <img src="Anexos/F2_3.png" > |
|Señal EMG de la mano | <img src="Anexos/F3_1.png" > | <img src="Anexos/F3_2.png" > | <img src="Anexos/F3_3.png" > |
|Señal EMG del trapecio | <img src="Anexos/F4_1.png" > | <img src="Anexos/F4_2.png" > | <img src="Anexos/F4_3.png" > |
|Señal EMG del triceps | <img src="Anexos/F5_1.png" > | <img src="Anexos/F5_2.png" > | <img src="Anexos/F5_3.png" > |
<p align="center"><i>Tabla 3. Señales EMG filtradas por tres tipos de filtros. </i></p>
</p>

### **ECG:**<a id="ECG"></a>

| **Descripcion de la señal** | **Filtro IIR** | **Filtro FIR** | **Filtro FIR** |
|:------------:|:---------------:|:---------------:|:---------------:|
|Señal ECG en estado de reposo | <img src="Anexos/F6_1.png" > | <img src="Anexos/F6_2.png" > | <img src="Anexos/F6_3.png" > |
|Señal ECG en estado de respiración prolongada | <img src="Anexos/F7_1.png" > | <img src="Anexos/F7_1.png" > | <img src="Anexos/F7_1.png" > |
|Señal ECG en estado de post - Respiración | <img src="Anexos/F8_1.png" > | <img src="Anexos/F8_2.png" > | <img src="Anexos/F8_3.png" > |
|Señal ECG en estado luego de actividad física | <img src="Anexos/F9_1.png" > | <img src="Anexos/F9_2.png" > | <img src="Anexos/F9_3.png" > |
<p align="center"><i>Tabla 4. Señales ECG filtradas por tres tipos de filtros. </i></p>
</p>

## **Conclusion**<a id="conclu"></a>
<p align="justify">El filtrado es un aspecto fundamental en el procesamiento de señales. A menudo, una señal de entrada a un sistema puede contener información innecesaria o ruido que degrada la calidad de la señal deseada. Por lo tanto, el filtrado se convierte en un proceso esencial para eliminar o atenuar muestras no relevantes. Para ello se etilzan normalmete diferentes tipos de filtros que se clasifican en dos categorías principales: filtros de respuesta de impulso finito (FIR) y filtros de respuesta de impulso infinito (IIR). Cada tipo tiene sus características.</p>

### **Filtros IIR**<a id="IIR"></a>
<p align="justify">Los filtros IIR son conocidos por su similitud con los filtros analógicos, lo que les permite ser más eficientes en términos de recursos computacionales. Contienen una retroalimentacion en su diseño, lo que puede llevar a respuestas de fase no lineales. Aunque los filtros IIR pueden llegar a no ser  estables, ofrecen ventajas en términos de eficiencia y respuesta rápida. [1]</p>
<p align="center"><img src="Anexos/D3.png" width="400" height="400"> <img src="Anexos/D4.png" width="400" height="400">
<i>Figura 3 Y 4: Diagrama de Bode y de polos y ceros del filtro IIR</i></p>

### **Filtros FIR - Ventana rectangular**<a id="FIR"></a>
<p align="justify">En cambio los filtros FIR si son mas estables y generan respuestas mas precisas y sus funciones de ventana se utilizan para determinar los coeficientes del filtro, y estas funciones pueden variar en forma y características.[2] </p>
<p align="center"><img src="Anexos/D1.png" width="400" height="400"> <img src="Anexos/D2.png" width="400" height="400">
<i>Figura 5 Y 6: Diagrama de Bode y de polos y ceros del filtro FIR- Ventana rectangular</i></p>

### **Filtros FIR - Ventana kaiser**<a id="FIR"></a>
<p align="justify">En comparacion al primer filtero FIR aqui se uso una ventan KAISER un tipo de filtro que emplea una función de ventana ajustable. Generando en una mejor respuesta en la banda de paso y una mayor atenuación en la banda de detención.La flexibilidad de la ventana de Kaiser permite ajustar parámetros para optimizar el rendimiento del filtro, lo que resulta especialmente útil en aplicaciones de procesamiento de señales, como la eliminación de ruido en señales de ECG.[2] </p>
<p align="center"><img src="Anexos/D5.png" width="400" height="400"> <img src="Anexos/D6.png" width="400" height="400">
<i>Figura 7 Y 8: Diagrama de Bode y de polos y ceros del filtro FIR- Ventana kaiser</i></p>

## **Bibliografia:**<a id="Bibliografia"></a>
<p align="justify">[1] N. Agrawal, A. Kumar, Varun Bajaj, G.K. Singh, "Design of digital IIR filter: A research survey," Applied Acoustics, vol. 172, 2021, Art. no. 107669, doi: 10.1016/j.apacoust.2020.107669.</p>
<p align="justify">[2] T. K. Roy and M. Morshed, "Performance analysis of low pass FIR filters design using Kaiser, Gaussian and Tukey window function methods," 2013 2nd International Conference on Advances in Electrical Engineering (ICAEE), Dkaka, Bangladesh, 2013, pp. 1-6, doi: 10.1109/ICAEE.2013.6750294. </p>
