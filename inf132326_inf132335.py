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
    warnings.filterwarnings('ignore')
    
    wavPath = sys.argv[1]    

    try:
        w, signal = scipy.io.wavfile.read(wavPath)
    except:
        print('    Error while opening file.')
        sys.exit(1)

    if len(signal.shape) != 1:
        signal = [ x[0] for x in signal ]

    signal = signal * scipy.signal.kaiser(len(signal), 14)

    fft_signal = abs(fft(signal))
    main_signal = find_main_signal(fft_signal)
    amp_max = max(main_signal[200:])

    n = len(main_signal)
    for i in range(len(main_signal[200:])): 
        if amp_max == main_signal[i]:
            f = i/n*w
            if f < 160:
                recognized_gender = 'M'
            else:
                recognized_gender = 'K'
            print(recognized_gender)

if __name__== "__main__":
    main()