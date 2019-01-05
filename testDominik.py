from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import scipy.io.wavfile
from scipy.signal import decimate

NUMBER_OF_DECIMATIONS = 8

def importMusic(i):
    w = 44100
    signal = np.array([])
    gender = 'None'
    if i < 10:
        try:
            # Try with suffix K for one number
            w, signal = scipy.io.wavfile.read('trainall/00'+ str(i) + '_K.wav')
            gender = 'K'
        except:
            pass
        try:
            #Try with suffix M for one number
            w, signal = scipy.io.wavfile.read('trainall/00'+ str(i) + '_M.wav')
            gender = 'M'
        except:
            pass
    else:
        try:
            # Try with suffix K for two numbers
            w, signal = scipy.io.wavfile.read('trainall/0'+ str(i) + '_K.wav')
            gender = 'K'
        except:
            pass
        try:
            #Try with suffix M for two numbers
            w, signal = scipy.io.wavfile.read('trainall/0'+ str(i) + '_M.wav')
            gender = 'M'
        except:
            pass
    return w, signal, gender


def processMusic(w, signal, index):
    spectrum = np.array([])
    multiplied = np.array([])

    if len(signal.shape) != 1:
        signal = [s[0] for s in signal]
    spectrum = abs(fft(signal))

    multiplied = spectrum
    for i in range(2, NUMBER_OF_DECIMATIONS):
        temp = decimate(spectrum, i)
        multiplied = temp * multiplied[ : len(temp)]

    
    freqs = [x / (len(signal) * w) for x in range(len(signal))]

    n = list(multiplied).index(max(multiplied))

    probe = freqs[n]


    # for i in range(len(multiplied)):
    #     if max(multiplied) == multiplied[i]:
    #         probe = freqs[i]

    if probe < 165:
        print('    Number ' + str(index) + ' is a man with frequency ' + str(probe))
        return(1) 
    else:
        print('    Number ' + str(index) + ' is a woman with frequency ' + str(probe))
        return(2)
    

def main():
    print('Starting')
    correct, answer = [0, 0]
    for i in range(1, 92):
        frequency, signal, gender = importMusic(i)
        if gender != 'None':
            answer = processMusic(frequency, signal, i)

        if answer == 1 and gender == 'M':
            correct = correct + 1
        elif answer == 2 and gender == 'K':
            correct = correct + 1
    print(str(correct) + ' out of 91 files are correct')

if __name__== "__main__":
    main()