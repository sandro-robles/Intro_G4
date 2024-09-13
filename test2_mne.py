import mne

# Crear un objeto de datos vacíos para verificar la instalación
info = mne.create_info(ch_names=['MEG 1'], sfreq=1000, ch_types=['mag'])

# Imprimir la información básica del objeto
print(info)