from __future__ import division
from pylab import *
from numpy import *
from scipy import *
from ipywidgets import *
import math as mt
import scipy.io.wavfile

w_k, signal_k = scipy.io.wavfile.read('trainall/001_K.wav')
w_m, signal_m = scipy.io.wavfile.read('trainall/002_M.wav')

print(w_k)

