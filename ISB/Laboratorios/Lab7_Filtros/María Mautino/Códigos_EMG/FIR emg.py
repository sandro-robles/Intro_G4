import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import firwin, lfilter, freqz, tf2zpk

# Función para leer el archivo txt
def read_signal_from_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Saltar líneas de cabecera
                values = line.split()
                data.append(int(values[-1]))  # Última columna es la señal A1
    return np.array(data)

# Diseño del filtro FIR notch (Notch de 60 Hz con un ancho de banda de 10 Hz)
def design_notch_filter(fs, notch_freq=60, bandwidth=10, numtaps=251):
    nyquist = 0.5 * fs
    low = (notch_freq - bandwidth / 2) / nyquist
    high = (notch_freq + bandwidth / 2) / nyquist
    return firwin(numtaps, [low, high], pass_zero=True)

# Diseño del filtro FIR bandpass (Paso banda 6 Hz - 450 Hz)
def design_bandpass_filter(fs, lowcut=6, highcut=450, numtaps=101):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    return firwin(numtaps, [low, high], pass_zero=False)

# Aplicación del filtro
def apply_fir_filter(signal, fir_coeff):
    return lfilter(fir_coeff, 1.0, signal)

# Función para obtener límites del eje y (ylim) entre un rango de tiempo
def get_ylim_for_time_range(signal, time_range, fs):
    start_sample = int(time_range[0] * fs)
    end_sample = int(time_range[1] * fs)
    signal_in_range = signal[start_sample:end_sample]
    return np.min(signal_in_range), np.max(signal_in_range)

# Función para graficar señales con ylim ajustado a un rango de tiempo
def plot_signals(original_signal, filtered_signal, fs, time_range):
    t = np.arange(len(original_signal)) / fs

    # Obtener límites de ylim para ambas señales dentro del rango de tiempo especificado
    original_ylim = get_ylim_for_time_range(original_signal, time_range, fs)
    filtered_ylim = get_ylim_for_time_range(filtered_signal, time_range, fs)

    plt.figure(figsize=(12, 6))

    # Señal original
    plt.subplot(2, 1, 1)
    plt.plot(t, original_signal, label='Señal Original')
    plt.title('Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)  # Ajustar límites de tiempo
    plt.ylim(original_ylim)  # Ajustar límites de amplitud a los máximos y mínimos en el rango

    # Señal filtrada
    plt.subplot(2, 1, 2)
    plt.plot(t, filtered_signal, label='Señal Filtrada', color='orange')
    plt.title('Señal Filtrada')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)  # Ajustar límites de tiempo
    plt.ylim(filtered_ylim)  # Ajustar límites de amplitud a los máximos y mínimos en el rango

    plt.tight_layout()
    plt.show()

# Función para graficar el diagrama de polos y ceros
def plot_pole_zero(fir_coeff):
    z, p, k = tf2zpk(fir_coeff, [1.0])  # Los filtros FIR solo tienen ceros
    plt.figure()
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.title('Diagrama de Polos y Ceros (FIR)')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()

# Función para graficar el diagrama de Bode
def plot_bode(fir_coeff, fs):
    w, h = freqz(fir_coeff, worN=8000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.title('Diagrama de Bode - Magnitud (FIR)')
    plt.ylabel('Amplitud')
    plt.grid()

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(0.5 * fs * w / np.pi, np.angle(h), 'b')
    plt.title('Diagrama de Bode - Fase (FIR)')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [radianes]')
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Leer la señal de un archivo txt
    file_path = 'gastromov.txt'  # Reemplazar con la ruta de tu archivo
    signal = read_signal_from_txt(file_path)

    # Parámetros
    fs = 1000  # Frecuencia de muestreo
    n = len(signal)  # Número de puntos en la señal

    # Calcular la FFT
    Y = fft(signal) / n  # Transformada normalizada
    frq = fftfreq(n, 1/fs)  # Frecuencias correspondientes

    # Graficar la magnitud de la FFT de la señal original
    plt.figure(figsize=(10, 6))
    plt.plot(frq[:n // 2], np.abs(Y[:n // 2]))  # Solo frecuencias positivas
    plt.ylim(0, 4)
    plt.xlim(0, 200)
    plt.title('Magnitud de la FFT de la señal ORIGINAL')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|$Y(f)$|')
    plt.grid()
    plt.show()

    # Diseño de los filtros
    notch_fir = design_notch_filter(fs)
    bandpass_fir = design_bandpass_filter(fs)

    # Aplicar los filtros
    signal_notch_filtered = apply_fir_filter(signal, notch_fir)
    signal_bandpass_filtered = apply_fir_filter(signal_notch_filtered, bandpass_fir)

    # Rango de tiempo deseado para mostrar los gráficos
    time_range = (4, 6)  # Definir el rango de tiempo (en segundos)

    # Graficar las señales con ylim ajustado a los máximos y mínimos en el rango de tiempo
    plot_signals(signal, signal_bandpass_filtered, fs, time_range)

    # Graficar el diagrama de polos y ceros del filtro FIR notch
    print("Diagrama de Polos y Ceros del filtro FIR Notch:")
    plot_pole_zero(notch_fir)

    # Graficar el diagrama de Bode del filtro FIR notch
    print("Diagrama de Bode del filtro FIR Notch:")
    plot_bode(notch_fir, fs)

    # Graficar el diagrama de polos y ceros del filtro FIR bandpass
    print("Diagrama de Polos y Ceros del filtro FIR Bandpass:")
    plot_pole_zero(bandpass_fir)

    # Graficar el diagrama de Bode del filtro FIR bandpass
    print("Diagrama de Bode del filtro FIR Bandpass:")
    plot_bode(bandpass_fir, fs)

    # Calcular la FFT de la señal filtrada
    Y_filtered = fft(signal_bandpass_filtered) / n  # Transformada normalizada
    frq_filtered = fftfreq(n, 1/fs)  # Frecuencias correspondientes

    # Graficar la magnitud de la FFT de la señal filtrada
    plt.figure(figsize=(10, 6))
    plt.plot(frq_filtered[:n // 2], np.abs(Y_filtered[:n // 2]))  # Solo frecuencias positivas
    plt.ylim(0, 4)
    plt.xlim(0, 200)
    plt.title('Magnitud de la FFT de la señal filtrada')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|$Y(f)$|')
    plt.grid()
    plt.show()
