# **LABORATORIO 12: – Edge Impulse**
## **Create impulse:**
<p align="justify">Utilizo ventanas de 2000 ms en cada adquisición de EMG a una frecuencia de 1KHz (Frecuencia de muestreo del BITalino).</p>
<p align="center"><img src="Anexos/IM1.png"></p>
<p align="center"><i>Figura 2: Creacion del impulso.</i></p>

## **Spectral features:**
<p align="justify">El único parámetro que modifico para la obtención de features es la longitud de FFT que va a ser igual a 32. Se puede ver la ventana de 2000 ms en la ventana de raw data y los resultados del procesamiento digital en la parte derecha. </p>
<p align="center"><img src="Anexos/IM3.png"></p>
<p align="center"><i>Figura 3: Parametros para Spectral features.</i></p>
<p align="center"><img src="Anexos/IM2.png" ></p>
<p align="center"><i>Figura 4: Feature explorer.</i></p>

## **Classifier:**
<p align="justify">En la parte del classifier, dispongo de 100 ciclos de entrenamiento y un learning rate de 0.0005, con un validation size de 20.</p>
<p align="center"><img src="Anexos/IM4.png"></p>
<p align="center"><i>Figura 5: Configuraciones para la clasificacion.</i></p>
<p align="justify">Se pusieron 12o ciclos para ajustar mejor los datos del modelo y no tan grande para evitar el overfitting, un learning rate de 0.001 debido a que se obtubo mejores resultados comparado a uno con 0.0005 y por ultimo se aumqntaron enl numero de neuronas: +10 Dense layer para mejorar el rendimiento y un Dropout de 0.3 para evitar overfitting.</p>
<p align="justify">Con todas estas configuraciones el modelo obtubo las siguientes caracteristicas, aceptables aunque con mejora:</p>
<p align="center"><img src="Anexos/IM5.png"></p>
<p align="center"><i>Figura 6: Accuracy obtenido y matriz de confusion..</i></p>

## **Model testing:**
<p align="justify">Se obtuvieron los siguientes resultados del modelo entrenado, dando buenos scores para el modelo.</p>
<p align="center"><img src="Anexos/IM6.png"></p>
<p align="center"><i>Figura 1: Repositorio editado de las señales ECG.</i></p>
