# **LABORATORIO 5: – Uso de BITalino para EEG**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Introduccion](#Introduccion)
3. [Equipos y materiales utilizados](#Equipos)
4. [Metodología](#Metodología)
5. [Cronología de mediciones](#Cronologíademediciones)
6. [Posiciones de los electrodos](#Posicionesdeloselectrodos)
7. [Resultados](#Resultados)
8. [Discusión](#Discusión)
9. [Bibliografia](#Bibliografia)
## **Objetivos:**<a id="Objetivos"></a>
- Investigar técnicas de procesamiento de señales EEG, con énfasis en filtrado y eliminación de ruido.
- Configurar correctamente el dispositivo BiTalino para la adquisición de señales EEG.
- Extraer y analizar señales EEG utilizando el software OpenSignals (r)evolution.
  
## **Introducción:**<a id="Introduccion"></a>
<p align="justify"> El  </p>


## **Metodología:**<a id="Metodología"></a>
<p align="justify">En primer lugar, se realizaron tres registros para cada una de las tres derivaciones en reposo (derivaciones I, II y III). El participante debía estar en una posición cómoda, relajado y sin moverse para evitar interferencias en los registros. </p>

<p align="justify">A continuación, se procedió a la segunda fase de medición, en la cual se solicitó al participante que retuviera la respiración. Se realizó un solo registro para cada derivación bajo las siguientes condiciones: el participante retenía la respiración durante 20 segundos, y luego se le daba un tiempo de recuperación de 2 minutos, durante el cual se registraba la segunda parte de la toma. Este proceso se repitió para cada una de las tres derivaciones. </p>

<p align="justify">Para la última prueba, el participante realizó una actividad física moderada, que consistió en subir y bajar escaleras durante 5 minutos con el fin de aumentar su frecuencia cardíaca. Inmediatamente después de finalizar la actividad física, se realizó una toma única de cada derivación, registrando la actividad cardíaca durante un periodo de 20 minutos. </p>

<p align="justify"> Se recomienda seguir estrictamente la cronología de las mediciones, ya que es crucial que el paciente se encuentre en reposo absoluto al inicio, sin haber experimentado ningún tipo de estrés previo. Si se realizaran primero las mediciones con retención de la respiración o, especialmente, la prueba de actividad física, se afectarían de manera significativa los registros en reposo debido al incremento de la frecuencia cardíaca, lo que alteraría los resultados de manera irreversible.</p>

## **Cronología de mediciones:**<a id="Cronologíademediciones"></a>
1. **Mediciones en Reposo:** <br>
1.1. Primera toma de la primera derivación (20 segundos).<br>
1.2. Segunda toma de la primera derivación (20 segundos).<br>
1.3. Tercera toma de la primera derivación (20 segundos).<br>
1.4. Primera toma de la segunda derivación (20 segundos).<br>
1.5. Segunda toma de la segunda derivación (20 segundos).<br>
1.6. Tercera toma de la segunda derivación (20 segundos).<br>
1.7. Primera toma de la tercera derivación (20 segundos).<br>
1.8. Segunda toma de la tercera derivación (20 segundos).<br>
1.9. Tercera toma de la tercera derivación (20 segundos).<br>

2. **Mediciones con Retención de la Respiración:** <br>
2.1. Toma de la primera derivación durante retención de la respiración (20 segundos).<br>
2.2. Toma de la recuperación de 2 minutos tras la retención de la respiración para la primera derivación.<br>
2.3. Toma de la segunda derivación durante retención de la respiración (20 segundos).<br>
2.4. Toma de la recuperación de 2 minutos tras la retención de la respiración para la segunda derivación.<br>
2.5. Toma de la tercera derivación durante retención de la respiración (20 segundos).<br>
2.6. Toma de la recuperación de 2 minutos tras la retención de la respiración para la tercera derivación.<br>

3. **Mediciones Posteriores a la Actividad Física:** <br>
3.1. Toma de la primera derivación tras 5 minutos de actividad física.<br>
3.2. Toma de la segunda derivación tras 5 minutos de actividad física.<br>
3.3. Toma de la tercera derivación tras 5 minutos de actividad física.<br>

## **Posiciones de los electrodos:**<a id="Posicionesdeloselectrodos"></a>

<p align="center"><img src="Anexos/posicionguia.png" width="400"></p>

<p align="center"><i>Figura 4: Colocación de electrodos para la derivación I: IN+ (rojo) e IN- (negro) en las muñecas y REF (blanco) en la cresta ilíaca [1].</i></p>

<p align="center"><img src="Anexos/tablaposiciones.png" width="400"></p>

<p align="center"><i>Figura 5: Tabla de posiciones de los electrodos de acuerdo a la derivación analizada. Elaboración propia.</i></p>


<p align="center"><img src="Anexos/posicionnosotros.png" width="400"></p>

<p align="center"><i>Figura 6: Imagen referencial de las posiciones en donde deben colocarse los electrodos, para una mejor precisión al hacer los cambios. Elaboración propia.</i></p>

## **Equipos y materiales utilizados:**<a id="Equipos"></a>
<div align="center">
   
|  **Modelo**  | **Descripción** | **Cantidad** |
|:------------:|:---------------:|:------------:|
| (r)EVOLUTION |   Kit BITalino  |       1      |
|     ASUS     |      Laptop     |       1      |
|       -      |    Electrodos superficiales   |       3      |
|    FLUKE ProSim 4    |   Vital Signs Simulators   |       1      |
</div>
<p align="center"><i>Tabla 2. Equipos y materiales utilizados en este laboratorio. </i></p>

<p align="center"><img src="Anexos/BITalino.jpeg" width="300" height="300"><img src="Anexos/FLUKE.jpeg" width="300" height="300"></p>
<p align="center"><i>Figura 7 y 8: Kit BITalino y ProSim 4 conectados a los electrodos. </i></p>

## **Resultados:**<a id="Resultados"></a>
### 1. Señales captadas con la 1era derivación en diferentes estados:
#### <blockquote> Estado: En reposo </blockquote>
<p align="center">
   

| **Video 1.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/9a4cd9f0-1357-4051-9b22-9e2d5093ba85"> | <img src="Anexos/D1.1.png" > |
<p align="center"><i>Tabla 3. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Respiración prolongada </blockquote>
<p align="center">
   
| **Video 2.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/c4a0b0ad-e645-43a5-aa94-9c123bf638d5"> | <img src="Anexos/D1.2.png" > |
<p align="center"><i>Tabla 4. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Post - Respiración </blockquote>
<p align="center">
   
| **Video 3.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/0e6106c2-046d-48a6-badc-7b3202e11244"> | <img src="Anexos/D1.3.png" > |
<p align="center"><i>Tabla 5. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Luego de actividad física </blockquote>
<p align="center">
   
| **Video 4.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/da7f9b48-1053-486f-b1d1-562d4cdd4ed0"> | <img src="Anexos/D1.4.png" > |
<p align="center"><i>Tabla 6. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

### 2. Señales captadas con la 2da derivación en diferentes estados:
#### <blockquote> Estado: En reposo </blockquote>
<p align="center">
   

| **Video 5.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/462f440b-884a-473e-b0df-c56687fc3926"> | <img src="Anexos/D2.1.png" > |
<p align="center"><i>Tabla 7. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Respiración prolongada </blockquote>
<p align="center">

| **Video 6.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/71c4112d-03f1-428e-ad27-a58b2fef82f0"> | <img src="Anexos/D2.2.png" > |
<p align="center"><i>Tabla 8. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Post - Respiración </blockquote>
<p align="center">

| **Video 7.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/7b176a56-6062-483a-aa1b-311ee33d1bd8"> |  <img src="Anexos/D2.3.png" > |
<p align="center"><i>Tabla 9. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Luego de actividad física </blockquote>
<p align="center">

| **Video 8.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/54c1ac73-5691-4f6e-80d0-187b3e229f20"> | <img src="Anexos/D2.4.png" > |
<p align="center"><i>Tabla 10. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>


### 3. Señales captadas con la 3ra derivación en diferentes estados:
#### <blockquote> Estado: En reposo </blockquote>
<p align="center">
   
| **Video 9.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/546a74f9-e64d-4848-bed0-1276e0c198a6"> | <img src="Anexos/D3.1.png" > |
<p align="center"><i>Tabla 11. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Respiración prolongada </blockquote>
<p align="center">
   
| **Video 10.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/604ec57c-67ca-4fcf-bc85-77f125c48e7f"> | <img src="Anexos/D3.2.png" > |
<p align="center"><i>Tabla 12. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Post - Respiración </blockquote>
<p align="center">

| **Video 11.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/2959df29-7fec-4bf8-a91b-4fa707863bfe"> |  <img src="Anexos/D3.3.png" > |
<p align="center"><i>Tabla 13. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>


#### <blockquote> Estado: Luego de actividad física </blockquote>
<p align="center">
   
| **Video 12.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/2a476837-b060-45b9-a28e-e6cc87c3e201"> |  <img src="Anexos/D3.4.png" > |
<p align="center"><i>Tabla 14. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

## **Ejercicio realizado:**<a id="Ejercicio"></a>
<p align="center">
<p align="center"><video src="https://github.com/user-attachments/assets/028cd25f-daeb-482f-b897-e39af0cbee37" width="400"></p>
<p align="center"><i>  Video del ejercicio realizado. </i></p>
</p>

### 4. Señal del Promsim4 (dispositivo de metrología que genera una señal patrón)
El **ProMSim4** es un simulador de ECG (electrocardiograma) diseñado para evaluar y calibrar dispositivos de monitoreo y diagnóstico cardíaco, como electrocardiógrafos, monitores cardíacos y sistemas de telemetría. Este tipo de simulador genera señales de ECG artificiales con patrones que imitan las señales del corazón en diversas condiciones, incluyendo ritmos cardíacos normales y arritmias[12].
#### <blockquote> Estado: En reposo (60 lpm)  </blockquote>
<p align="center">
   
| **Video 13.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/3a9e6d41-2c13-4a77-8595-d0bcd2dd8751"> |  <img src="Anexos/PRO1.png" > |
<p align="center"><i>Tabla 15. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Reponiéndose (90 lpm)  </blockquote>
<p align="center">
   
| **Video 16.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/fec886a4-b7b2-41b8-beef-de6fa97c5bf1"> |  <img src="Anexos/PRO4.png" > |
<p align="center"><i>Tabla 18. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Comienza a agitarse (120 lpm)  </blockquote>
<p align="center">
   
| **Video 14.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/f1310b2e-73b3-4d66-a538-d2f69ed7e474"> |  <img src="Anexos/PRO2.png" > |
<p align="center"><i>Tabla 16. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>

#### <blockquote> Estado: Haciendo ejercicio (150 lpm)  </blockquote>
<p align="center">
   
| **Video 15.** | **Señal obtenida** |
|:------------:|:---------------:|
| <video src="https://github.com/user-attachments/assets/d76f7100-9bc3-4378-93e1-0e02289eaa54"> |  <img src="Anexos/PRO3.png" > |
<p align="center"><i>Tabla 17. Video de la adquisición de la señal ECG y la señal obtenida. </i></p>
</p>



## **Discusión:**<a id="Discusión"></a>
<p align="justify"> </p>

## **Bibliografia:**<a id="Bibliografia"></a>
<p align="justify">[1]</p>

