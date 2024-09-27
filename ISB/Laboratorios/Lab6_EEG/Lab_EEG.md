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
### 1. Señales EEG captadas con eL Kit BITalino:
#### <blockquote> Caso 1: Linea base sin movimientos y ojos cerrados durante 30 segundos. </blockquote>
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


## **Discusión:**<a id="Discusión"></a>
<p align="justify"> </p>

## **Bibliografia:**<a id="Bibliografia"></a>
<p align="justify">[1]</p>

