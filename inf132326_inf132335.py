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
    # process_depth = 6
    # for i in range(2, 2+process_depth):
    #     decimated.append(decimate(signal, i))
    # 'decimate' function gives us twice smaller array than the one from input
    # we cut from the arrays all elements which index is greater than the length of last array 
    # signals_length = len(decimated[process_depth-1])
    # processed_signal = processed_signal[:signals_length]
    # for dec in decimated:
    #     processed_signal = processed_signal * dec[:signals_length]
    for i in range(2, 6):
        decimated.append(decimate(signal, i))
    for i in range(len(decimated[3])):
        processed_signal[i] = processed_signal[i] * decimated[0][i] * decimated[1][i] * decimated[2][i] * decimated[3][i]
    for i in range(len(decimated[3]), len(processed_signal)):
        processed_signal[i] = 0
    return processed_signal

def main():
    # wav_file = sys.argv[1]
    ##############################################################################
    czary = np.array([1,2,3,4])
    kobiety = []
    faceci = []
    correct_recognitions = 0
    for i in range(2,92):
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
        print('W pliku: '+correct_gender)
        if(len(signal.shape) != 1): # niektóre dźwięki mają dwa kanaly- wybieramy jeden
            signal = [ x[0] for x in signal ]
            # signal = [ x[1] for x in signal ]
            # signal = [ mean(x) for x in signal ]
        
        fft_signal = abs(fft(signal))
        main_signal = find_main_signal(fft_signal)
        amp_max = max(main_signal[200:])#odcinamy te początkowe, bo tam zazwyczaj są nieinteresujące nas wartości

        n = len(main_signal)
        for i in range(len(main_signal[200:])): 
            if amp_max == main_signal[i]:
                f = i/n*w
                if f < 150:
                    recognized_gender = 'M'
                else:
                    recognized_gender = 'K'
                print('Rozpoznana: '+recognized_gender)
                print('Index: '+repr(i)+' value: '+repr(f))

        if recognized_gender == correct_gender:
            correct_recognitions += 1

    print('Skuteczność: '+repr(correct_recognitions/89)) #89, bo sprawdzam wszystkie pliki z wyjątkiem 1 i 8
        # freqs = range(int(len(main_signal)))
        # freqs = [(x / len(main_signal)) * w for x in freqs]
        # plt.stem(freqs, main_signal, '-*')
    # print("################# kobiety #################")
    # print(kobiety)
    # print("################# faceci #################")
    # print(faceci)


main()