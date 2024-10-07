import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz, tf2zpk
from scipy.fft import fft, fftfreq

# Función para leer el archivo txt
def read_signal_from_txt(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith('#'):  # Saltar líneas de cabecera
                values = line.split()
                data.append(float(values[-1]))  # Última columna es la señal A1
    return np.array(data)

# Diseño del filtro FIR notch (para eliminar 60 Hz con ventana Blackman)
def design_notch_filter_blackman(fs, notch_freq=60, bandwidth=5, numtaps=251):
    nyquist = 0.5 * fs
    low = (notch_freq - bandwidth / 2) / nyquist
    high = (notch_freq + bandwidth / 2) / nyquist
    return firwin(numtaps, [low, high], window='blackman', pass_zero=False)

# Diseño del filtro FIR pasa-banda (0.5 Hz - 80 Hz) con ventana Blackman
def design_bandpass_filter_blackman(fs, lowcut=0.5, highcut=80, numtaps=251):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    return firwin(numtaps, [low, high], window='blackman', pass_zero=False)

# Aplicación del filtro FIR
def apply_fir_filter(signal, fir_coeff):
    return lfilter(fir_coeff, 1.0, signal)

# Función para obtener los límites de Y (amplitud) en el rango de tiempo dado
def get_ylim_for_time_range(signal, fs, time_range):
    start_sample = int(time_range[0] * fs)
    end_sample = int(time_range[1] * fs)
    signal_in_range = signal[start_sample:end_sample]
    return np.min(signal_in_range), np.max(signal_in_range)

# Graficar la señal original y filtrada
def plot_signals_separated(original_signal, filtered_signal, fs, time_range):
    t = np.arange(len(original_signal)) / fs

    original_ylim = get_ylim_for_time_range(original_signal, fs, time_range)
    filtered_ylim = get_ylim_for_time_range(filtered_signal, fs, time_range)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(t, original_signal, label='Señal Original', color='b')
    plt.title('Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)
    plt.ylim(original_ylim)
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(t, filtered_signal, label='Señal Filtrada (FIR)', color='orange')
    plt.title('Señal Filtrada (FIR)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.xlim(time_range)
    plt.ylim(filtered_ylim)
    plt.grid()

    plt.tight_layout()
    plt.show()

# Graficar FFT de las señales
def plot_fft(original_signal, filtered_signal, fs):
    n = len(original_signal)

    Y_original = fft(original_signal) / n
    frq = fftfreq(n, 1/fs)

    Y_filtered = fft(filtered_signal) / n

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(frq[:n // 2], np.abs(Y_original[:n // 2]), 'b')
    plt.title('FFT de la Señal Original')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|Y(f)|')
    plt.ylim(0, 5)
    plt.xlim(0, 150)
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(frq[:n // 2], np.abs(Y_filtered[:n // 2]), 'orange')
    plt.title('FFT de la Señal Filtrada (FIR - BLACKMAN)')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('|Y(f)|')
    plt.ylim(0, 5)
    plt.xlim(0, 150)
    plt.grid()

    plt.tight_layout()
    plt.show()

# Graficar polos y ceros
def plot_pole_zero(fir_coeff):
    z, p, k = tf2zpk(fir_coeff, [1.0])
    plt.figure()
    plt.scatter(np.real(z), np.imag(z), marker='o', label='Ceros')
    plt.title('Diagrama de Polos y Ceros (FIR - BLACKMAN)')
    plt.xlabel('Parte Real')
    plt.ylabel('Parte Imaginaria')
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.legend()
    plt.show()

# Graficar el diagrama de Bode
def plot_bode(fir_coeff, fs):
    w, h = freqz(fir_coeff, worN=8000)
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
    plt.title('Diagrama de Bode - Magnitud (FIR - BLACKMAN)')
    plt.ylabel('Amplitud')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(0.5 * fs * w / np.pi, np.angle(h), 'b')
    plt.title('Diagrama de Bode - Fase (FIR)')
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Fase [radianes]')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Main
if __name__ == "__main__":
    file_path = 'RESPIRACON D1.txt'
    signal = read_signal_from_txt(file_path)

    fs = 1000

    notch_fir = design_notch_filter_blackman(fs)
    bandpass_fir = design_bandpass_filter_blackman(fs)

    signal_notch_filtered = apply_fir_filter(signal, notch_fir)
    filtered_signal = apply_fir_filter(signal_notch_filtered, bandpass_fir)

    time_range = (0, 5)

    plot_signals_separated(signal, filtered_signal, fs, time_range)
    plot_fft(signal, filtered_signal, fs)
    plot_pole_zero(bandpass_fir)
    plot_bode(bandpass_fir, fs)
