import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.signal import iirnotch, butter, lfilter, freqz, tf2zpk

# Función para leer el archivo txt
def read_signal_from_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Saltar líneas de cabecera
                values = line.split()
                data.append(int(values[-1]))  # Última columna es la señal A1
    return np.array(data)

# Función para aplicar el filtro IIR notch para remover ruido de 60Hz
def apply_iir_notch_filter(signal, fs, f0, Q):
    # Crear el filtro notch
    b, a = iirnotch(f0, Q, fs)
    # Aplicar el filtro a la señal
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal, b, a

# Función para aplicar un filtro IIR de paso de banda
def apply_iir_bandpass_filter(signal, fs, lowcut, highcut):
    # Calcular la frecuencia de Nyquist
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    order = 4  # Orden del filtro
    b, a = butter(order, [low, high], btype='band')
    filtered_signal = lfilter(b, a, signal)
    return filtered_signal, b, a

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
def plot_pole_zero(b, a):
    z, p, k = tf2zpk(b, a)
    plt.figure()
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), marker='x', label='Polos')
    plt.title('Diagrama de Polos y Ceros')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    plt.show()

# Función para graficar el diagrama de Bode
def plot_bode(b, a, fs):
    w, h = freqz(b, a, worN=8000)
    plt.figure(figsize=(10, 6))

    # Magnitud
    plt.subplot(2, 1, 1)
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.title('Diagrama de Bode - Magnitud')
    plt.ylabel('Amplitud')
    plt.grid()

    # Fase
    plt.subplot(2, 1, 2)
    plt.plot(0.5 * fs * w / np.pi, np.angle(h), 'b')
    plt.title('Diagrama de Bode - Fase')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [radianes]')
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Leer la señal de un archivo txt
    file_path = 'trapecio movimiento fuerza.txt'  # Reemplazar con la ruta de tu archivo
    signal = read_signal_from_txt(file_path)

    # Parámetros
    fs = 1000  # Frecuencia de muestreo
    n = len(signal)  # Número de puntos en la señal

    # Parámetros del filtro
    f0 = 60.0  # Frecuencia del ruido a eliminar (en Hz)
    Q = 30.0   # Factor de calidad (afina la amplitud del notch)
    
    # Parámetros del filtro de paso de banda
    lowcut = 1.0  # Frecuencia inferior (en Hz)
    highcut = 100.0  # Frecuencia superior (en Hz)

    # Calcular la FFT
    Y = fft(signal) / n  # Transformada normalizada
    frq = fftfreq(n, 1/fs)  # Frecuencias correspondientes

    # Graficar la magnitud de la FFT
    plt.figure(figsize=(10, 6))
    plt.plot(frq[:n // 2], np.abs(Y[:n // 2]))  # Solo frecuencias positivas
    plt.ylim(0, 4)
    plt.xlim(0, 200)
    plt.title('Magnitud de la FFT de la señal ORIGINAL')
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('|$Y(f)$|')
    plt.grid()
    plt.show()

    # Aplicar el filtro notch
    filtered_signal_notch, b_notch, a_notch = apply_iir_notch_filter(signal, fs, f0, Q)

    # Aplicar el filtro de paso de banda
    filtered_signal_band, b_band, a_band = apply_iir_bandpass_filter(filtered_signal_notch, fs, lowcut, highcut)

    # Rango de tiempo deseado para mostrar los gráficos
    time_range = (7, 15)  # Definir el rango de tiempo (en segundos)

    # Graficar las señales con ylim ajustado a los máximos y mínimos en el rango de tiempo
    plot_signals(signal, filtered_signal_band, fs, time_range)

    # Calcular la FFT de la señal filtrada
    Y_filtered = fft(filtered_signal_band) / n  # Transformada normalizada
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

    # Graficar polos y ceros del filtro IIR
    print("Diagrama de Polos y Ceros del filtro notch IIR:")
    plot_pole_zero(b_notch, a_notch)

    print("Diagrama de Polos y Ceros del filtro de paso de banda IIR:")
    plot_pole_zero(b_band, a_band)

    # Graficar el diagrama de Bode del filtro IIR
    print("Diagrama de Bode del filtro notch IIR:")
    plot_bode(b_notch, a_notch, fs)

    print("Diagrama de Bode del filtro de paso de banda IIR:")
    plot_bode(b_band, a_band, fs)
