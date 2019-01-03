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
    processed_signal = signal
    decimated = []
    for i in range(2, 6):
        decimated.append(decimate(signal, i))

    for i in range( len(decimated)):
        for j in range( len(decimated[-1]) ):
            processed_signal[j] = processed_signal[j] * decimated[i][j]

    for i in range(len(decimated[-1]), len(processed_signal)):
        processed_signal[i] = 0
    return processed_signal

def main():

    correct_recognitions = 0
    for i in range(2, 92):
        if i == 8:
            continue
        print(i)
        correct_gender = ''
        if i < 10:
            try:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_K.wav')
                correct_gender = 'K'
            except:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_M.wav')
                correct_gender = 'M'
        else:
            try:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_K.wav')
                correct_gender = 'K'
            except:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_M.wav')
                correct_gender = 'M'
        
        print('W pliku: ' + correct_gender)
        if(len(signal.shape) != 1): # niektóre dźwięki mają dwa kanaly- wybieramy jeden
            signal = [ x[0] for x in signal ]

        signal = signal * scipy.signal.kaiser(len(signal), 14)

        fft_signal = abs(fft(signal))
        main_signal = find_main_signal(fft_signal)
        amp_max = max(main_signal[200:]) # odcinamy te początkowe, bo tam zazwyczaj są nieinteresujące nas wartości

        n = len(main_signal)
        for i in range(len(main_signal[200:])): 
            if amp_max == main_signal[i]:
                f = i/n*w
                if f < 150:
                    recognized_gender = 'M'
                else:
                    recognized_gender = 'K'
                print('Rozpoznana: ' + recognized_gender)
                print('Index: ' + repr(i) + ' value: ' +repr(f))

        if recognized_gender == correct_gender:
            correct_recognitions += 1

    print('Skuteczność ' + repr(correct_recognitions) + '/89: ' + repr(correct_recognitions / 89)) # 89, bo sprawdzam wszystkie pliki z wyjątkiem 1 i 8


main()