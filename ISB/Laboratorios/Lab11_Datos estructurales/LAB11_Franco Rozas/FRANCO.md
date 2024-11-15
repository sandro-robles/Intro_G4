# **LABORATORIO 8: – Filtro Wavelet**
## **Tabla de contenidos:**
1. [Objetivos](#Objetivos)
2. [Introduccion](#Introduccion)
3. [Equipos y materiales utilizados](#Equipos)
4. [Transformada Wavelet](#TransformadaWavelet)
5. [Transformada Wavelet Continua](#TransformadaWaveletContinua)
6. [Transformada Wavelet Discreta](#TransformadaWaveletDiscreta)
7. [Metodología](#Metodología)
8. [Equipos y materiales utilizados](#Equipos)
9. [Posiciones de los electrodos](#Posicionesdeloselectrodos)
10. [Procedimiento](#Procedimiento)
11. [Discusión](#Discusión)
12. [Bibliografia](#Bibliografia)
    
## **Objetivos:**<a id="Objetivos"></a>
- Desarrollar filtros basados en la Transformada Wavelet Discreta (DWT) para eliminar ruido en señales ECG, EMG y EEG.
- Comparar la eficiencia de diferentes wavelets en la reducción de ruido en señales biomédicas.
- Extraer y analizar características clave de señales filtradas para su aplicación clínica.
  
## **Introducción:**<a id="Introduccion"></a>
<p align="justify"> En el campo de la ingeniería biomédica, la obtención y correcta interpretación de señales médicas como el electrocardiograma (ECG), electromiograma (EMG) y electroencefalograma (EEG) son fundamentales tanto para el diagnóstico de enfermedades como para la investigación. En este contexto, la transformada Wavelet ha demostrado ser una herramienta matemática altamente eficaz para el procesamiento y análisis de estas señales, permitiendo descomponerlas en diferentes niveles de resolución para un análisis más preciso y adaptable. A diferencia de métodos tradicionales como la transformada de Fourier, la transformada Wavelet es especialmente útil para señales no estacionarias, cuyas características varían en el tiempo. Esto la convierte en una técnica ideal para aplicaciones biomédicas, donde las señales suelen estar contaminadas por ruido. La Discrete Wavelet Transform (DWT), en particular, facilita la selección de diferentes familias de wavelets que optimizan el procesamiento al reducir el ruido sin comprometer las características clave de las señales, mejorando la calidad y confiabilidad del análisis diagnóstico [1]​.‌ </p>

### **Transformada Wavelet**<a id="TransformadaWavelet"></a>
<p align="justify"> La transformada wavelet proporciona una técnica avanzada de análisis de señales que, a diferencia de la Transformada de Fourier, permite realizar un análisis multiresolución, lo que significa que puede descomponer una señal en diferentes niveles de frecuencia, manteniendo tanto la información temporal como la de frecuencia. Es especialmente útil en el análisis de señales no estacionarias o que presentan cambios abruptos, como muchas señales biomédicas, porque permite examinar diferentes escalas de tiempo. La principal ventaja es su capacidad para ajustar la resolución en función de la frecuencia: usa intervalos de tiempo grandes para baja frecuencia y pequeños para alta frecuencia, mejorando el detalle en las zonas donde es necesario.</p>

<p align="justify"> El proceso básico de la transformada wavelet implica pasar la señal por filtros pasaaltos y pasabajos para dividirla en sus componentes de alta y baja frecuencia. Esto se puede repetir, dividiendo aún más la señal en distintas bandas de frecuencia. Este enfoque produce una representación multiresolución, donde cada nivel corresponde a una banda específica de frecuencia, permitiendo observar qué frecuencias están presentes en qué momento de la señal. La transformada wavelet puede ser continua o discreta [2]. </p>

<p align="center"><img src="Anexos/Wavelet1.png" width="400"></p>

<p align="center"><i>Figura 1: Transformada Wavelet [3].</i></p>

#### **Transformada Wavelet Continua**<a id="TransformadaWaveletContinua"></a>
<p align="justify">La Transformada Wavelet Continua (CWT) permite analizar una señal en segmentos localizados del tiempo y consiste en expresar la señal como una expansión de coeficientes obtenidos a partir del producto interno entre la señal y una Wavelet Madre. Esta wavelet madre es una función de energía finita, que se dilata y se traslada en el tiempo para generar una familia de funciones conocidas como wavelets hijas. La CWT es especialmente útil para obtener información en baja frecuencia a través de intervalos grandes de tiempo, o en alta frecuencia utilizando intervalos pequeños de tiempo. Aunque la transformada maneja principalmente un plano de tiempo-escala, también puede trabajar en el dominio de tiempo-frecuencia mediante el teorema de Parseval, lo que la hace versátil para diferentes aplicaciones de análisis de señales [4].</p>

#### **Transformada Wavelet Discreta**<a id="TransformadaWaveletDiscreta"></a>
<p align="justify">La Transformada Wavelet Discreta (DWT) es una versión discretizada de la CWT que permite realizar el análisis numérico de señales. Para ello, se discretizan los parámetros de escala y traslación, transformando la señal en una serie de funciones elementales con sus respectivos coeficientes. En este proceso, la Wavelet Madre y las funciones de escala son fundamentales, donde las wavelets se encargan de captar los detalles finos de la señal (alta frecuencia), mientras que las funciones de escala se encargan de las aproximaciones más generales (baja frecuencia). Esta transformada permite representar una señal como una sumatoria de wavelets discretizadas, lo que facilita su análisis y reconstrucción. La DWT es una opción altamente eficiente para sistemas digitales, proporcionando una base ortonormal que asegura una buena precisión en el procesamiento de señales no estacionarias [4].</p>
