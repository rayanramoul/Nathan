import os
import librosa
import glob 
import numpy as np
from sklearn import metrics 
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal
import soundfile as sf
from python_speech_features import mfcc
from python_speech_features import logfbank
import scipy.io.wavfile as wav
from tqdm import tqdm

def join_features(mfcc, fbank):
    features = np.concatenate((mfcc, fbank), axis=1)
    return features


def transform_mfcc(path):
    #plt.figure(figsize=(12, 4))
    (data, sample_rate) = sf.read(path)   
    mfcc_feat = mfcc(data, sample_rate)
    fbank_feat = logfbank(data, sample_rate)
    return join_features(mfcc_feat, fbank_feat) # time_stamp x n_features

def fft(path): # Fourier
    data, sample_rate = sf.read(path)
    return fft(data)
    
def spectrogram(path):
    data, sample_rate = sf.read(path)
    frequencies, times, spectrogram = signal.spectrogram(data, sample_rate)
    return spectrogram


