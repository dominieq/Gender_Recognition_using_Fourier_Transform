from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import scipy.io.wavfile
import sys
from scipy.signal import decimate

def main():
    # wav_file = sys.argv[1]
    for i in range(2,10,1):
        # w_m, signal_m = scipy.io.wavfile.read('trainall/002_M.wav')
        print(i)
        k_czy_m = ''
        if i < 10:
            try:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_K.wav')
            except:
                w, signal = scipy.io.wavfile.read('trainall/00'+repr(i)+'_M.wav')
        else:
            try:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_K.wav')
            except:
                w, signal = scipy.io.wavfile.read('trainall/0'+repr(i)+'_M.wav')


    # print(w_k)

main()