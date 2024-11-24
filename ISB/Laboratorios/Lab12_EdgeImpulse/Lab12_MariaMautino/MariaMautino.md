# **LABORATORIO 12: – Mejora Edge Impulse**

Integrante: María Fernanda Mautino Rodríguez

<h2 style = "text-align: center;">Links de Edge Impulse:</h2>

1. [EDGE IMPULSE - ECG](https://studio.edgeimpulse.com/public/560002/live)</p>
2. [EDGE IMPULSE - EMG](https://studio.edgeimpulse.com/public/560374/live)</p>
3. [EDGE IMPULSE - EEG](https://studio.edgeimpulse.com/public/560380/live)</p>


## **Edge impluse:**
<p align="justify">Edge Impulse es una plataforma de inteligencia artificial especializada en el desarrollo y entrenamiento de modelos para dispositivos periféricos o de borde. Estos dispositivos incluyen sensores, microcontroladores y hardware de bajo consumo, permitiendo procesar datos localmente sin depender de conexiones constantes a la nube. Esto optimiza el rendimiento y la seguridad en aplicaciones que requieren análisis en tiempo real. </p>

<p align="center"><img src="Anexos Lab11/Captura de pantalla 2024-11-17 132251.png" width="400"></p>
<p align="center"><i>Figura 1: Página de Edge Impulse personal.</i></p>

## **Objetivos:**
- Crear un proyecto en Edge Impulse para cada tipo de señal procesada, como EMG, ECG y EEG, clasificándolas de manera adecuada.
- Implementar un código en Python para cargar las señales correspondientes a la plataforma Edge Impulse.

## **Metodología:**
<p align="justify">Los datos utilizados en este desarrollo fueron adquiridos en formato .txt, provenientes de los laboratorios de señales biológicas, específicamente de ECG, EMG y EEG. Dado que el entorno de Edge Impulse requiere archivos en formato .csv para su análisis, se desarrolló un script en Python que permite convertir automáticamente los archivos .txt en archivos .csv, adaptando su estructura al formato esperado. </p>
