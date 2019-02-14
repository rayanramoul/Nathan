import os
import librosa
import glob 
import numpy as np
from sklearn import metrics 
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal
import soundfile as sf

def transform_mfcc(path):
    label="nathan"
    #plt.figure(figsize=(12, 4))
    data, sample_rate = sf.read(path)
    librosa.display.waveplot(data, sr=sample_rate)
    return np.mean(librosa.feature.mfcc(y=data, sr=sample_rate, n_mfcc=40).T,axis=0)

def fft(path): # Fourier
    data, sample_rate = sf.read(path)
    return fft(data)
    
def spectrogram(path):
    data, sample_rate = sf.read(path)
    frequencies, times, spectrogram = signal.spectrogram(data, sample_rate)
    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    print(str(frequencies))
    print("len  frequencies: "+str(len(frequencies)))
    print(str(times))
    print(" len times : "+str(len(times)))
    print(str(spectrogram))
    print("len spectrogram : "+str(len(spectrogram)))
    plt.show()
    
spectrogram("./Audios/train/train-clean-100/4362/15663/4362-15663-0085.flac")

