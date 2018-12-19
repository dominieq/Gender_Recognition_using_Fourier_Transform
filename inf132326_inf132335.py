from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import scipy.io.wavfile
import sys
from scipy.signal import decimate

def find_main_signal(signal):
    signals = []
    main_signal = []
    for i in range(2,5):
      #chyba nie ta funkcja
        czary = decimate(signal, i)
    return main_signal

def main():
    # wav_file = sys.argv[1]
    ##############################################################################
    for i in range(2,10,1):
        # w_m, signal_m = scipy.io.wavfile.read('trainall/002_M.wav')
        print(i)
        k_czy_m = ''
        if i < 10:
            try:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_K.wav')
                k_czy_m = 'K'
            except:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_M.wav')
                k_czy_m = 'M'
        else:
            try:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_K.wav')
                k_czy_m = 'K'
            except:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_M.wav')
                k_czy_m = 'M'
        print('W pliku: '+k_czy_m)
        if(len(signal.shape) != 1):
            print('To potem')
        else:
            fft_signal = fft(signal)
            fft_signal.shape
            main_signal = find_main_signal(fft_signal)

main()