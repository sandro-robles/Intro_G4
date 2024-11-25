# **LABORATORIO 12: – Edge Impulse**
## **Create impulse:**
<p align="justify">Utilizo ventanas de 2000 ms en cada adquisición de EMG a una frecuencia de 1KHz (Frecuencia de muestreo del BITalino).</p>
<p align="center"><img src="Anexos/Creation1.PNG"></p>
<p align="center"><i>Figura 1: Creacion del impulso</i></p>

## **Spectral features:**
<p align="justify">El único parámetro que modifico para la obtención de features es la longitud de FFT que va a ser igual a 32. Se puede ver la ventana de 2000 ms en la ventana de raw data y los resultados del procesamiento digital en la parte derecha. </p>
<p align="center"><img src="Anexos/Features2.PNG"></p>

## **Classifier:**
<p align="justify">En la parte del classifier, dispongo de 100 ciclos de entrenamiento y un learning rate de 0.0005, con un validation size de 20.</p>
<p align="center"><img src="Anexos/CLassifier.PNG"></p>
<p align="center"><i>Figura 2: Configuraciones para la clasificacion.</i></p>

## **Model results:**
<p align="justify">Se obtuvieron los siguientes resultados del modelo entrenado, dando buenos scores para el modelo.</p>
<p align="center"><img src="Anexos/Score4.PNG"></p>
<p align="center"><i>Figura 3: Resultados</i></p>
