import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, tf2zpk
from scipy.fft import fft, fftfreq

# Función para leer el archivo txt
def read_signal_from_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Saltar líneas de cabecera
                values = line.split()
                data.append(int(values[-1]))  # Última columna es la señal A1
    return np.array(data)

# Diseño del filtro IIR Butterworth pasa banda
def design_butterworth_bandpass_filter(lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs  # Frecuencia de Nyquist
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a

# Aplicación del filtro pasa banda
def apply_bandpass_filter(signal, b, a):
    return lfilter(b, a, signal)

# Función para obtener los límites de Y (amplitud) en el rango de tiempo dado
def get_ylim_for_time_range(signal, fs, time_range):
    start_sample = int(time_range[0] * fs)
    end_sample = int(time_range[1] * fs)
    signal_in_range = signal[start_sample:end_sample]
    return np.min(signal_in_range), np.max(signal_in_range)

# Función para graficar la señal original y filtrada en gráficos separados
def plot_signals_separated(original_signal, filtered_signal, fs, time_range):
    t = np.arange(len(original_signal)) / fs

    # Obtener los límites de Y en el rango de tiempo especificado
    original_ylim = get_ylim_for_time_range(original_signal, fs, time_range)
    filtered_ylim = get_ylim_for_time_range(filtered_signal, fs, time_range)

    plt.figure(figsize=(12, 6))

    # Señal original
    plt.subplot(2, 1, 1)
    plt.plot(t, original_signal, label='Señal Original', color='b')
    plt.title('Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)
    plt.ylim(original_ylim)
    plt.grid()

    # Señal filtrada
    plt.subplot(2, 1, 2)
    plt.plot(t, filtered_signal, label='Señal Filtrada (IIR)', color='orange')
    plt.title('Señal Filtrada (IIR)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)
    plt.ylim(filtered_ylim)
    plt.grid()

    plt.tight_layout()
    plt.show()

# Función para graficar la FFT de las señales
def plot_fft(original_signal, filtered_signal, fs):
    n = len(original_signal)

    # Calcular la FFT de la señal original
    Y_original = fft(original_signal) / n  # Transformada normalizada
    frq = fftfreq(n, 1/fs)  # Frecuencias correspondientes

    # Calcular la FFT de la señal filtrada
    Y_filtered = fft(filtered_signal) / n  # Transformada normalizada
    frq_filtered = fftfreq(n, 1/fs)  # Frecuencias correspondientes

    plt.figure(figsize=(12, 6))

    # Graficar la FFT original
    plt.subplot(2, 1, 1)
    plt.plot(frq[:n // 2], np.abs(Y_original[:n // 2]), 'b')
    plt.title('FFT de la Señal Original')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|Y(f)|')
    plt.xlim(0, 150)
    plt.ylim(0, 5)
    plt.grid()

    # Graficar la FFT filtrada
    plt.subplot(2, 1, 2)
    plt.plot(frq_filtered[:n // 2], np.abs(Y_filtered[:n // 2]), 'orange')
    plt.title('FFT de la Señal Filtrada (IIR Butterworth)')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|Y(f)|')
    plt.xlim(0, 150)
    plt.ylim(0, 5)
    plt.grid()

    plt.tight_layout()
    plt.show()

# Función para graficar el diagrama de polos y ceros
def plot_pole_zero(b, a):
    z, p, k = tf2zpk(b, a)
    plt.figure()
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
    plt.title('Diagrama de Polos y Ceros (IIR Butterworth)')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()

# Función para graficar el diagrama de Bode
def plot_bode(b, a, fs):
    w, h = freqz(b, a, worN=8000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.title('Diagrama de Bode - Magnitud (IIR Butterworth)')
    plt.ylabel('Amplitud')
    plt.grid()

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(0.5 * fs * w / np.pi, np.angle(h), 'b')
    plt.title('Diagrama de Bode - Fase (IIR Butterworth)')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [radianes]')
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Leer la señal de un archivo txt
    file_path = 'EJERCICIO D2.txt'  # Reemplazar con la ruta de tu archivo
    signal = read_signal_from_txt(file_path)

    # Parámetros del filtro pasa banda
    fs = 1000  # Frecuencia de muestreo (en Hz)
    lowcut = 0.5  # Frecuencia de corte baja (en Hz)
    highcut = 40.0  # Frecuencia de corte alta (en Hz)
    order = 4  # Orden del filtro Butterworth

    # Diseño del filtro pasa banda
    b, a = design_butterworth_bandpass_filter(lowcut, highcut, fs, order)

    # Aplicar el filtro pasa banda
    filtered_signal = apply_bandpass_filter(signal, b, a)

    # Rango de tiempo deseado (ajustar aquí)
    time_range = (5, 10)  # Especificar el rango de tiempo (en segundos)

    # Graficar la señal original y filtrada en gráficos separados con ajuste de límites
    plot_signals_separated(signal, filtered_signal, fs, time_range)

    # Graficar la FFT de la señal original y filtrada
    plot_fft(signal, filtered_signal, fs)

    # Graficar polos y ceros del filtro IIR
    plot_pole_zero(b, a)

    # Graficar el diagrama de Bode del filtro IIR
    plot_bode(b, a, fs)
