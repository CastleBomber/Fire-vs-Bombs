from samplebase import SampleBase
import pyaudio
import re
import os
import time
from struct import unpack
import numpy as np


no_channels = 1
sample_rate = 44100
chunk = 4000
device = 2
p = pyaudio.PyAudio()
global stream
stream = p.open(format = pyaudio.paInt16,
                channels = no_channels,
                rate = sample_rate,
                input = True,
                frames_per_buffer = chunk,
                input_device_index = 2) # 2 || 4 hmm


'''
    returns height
            dictionary containing (freq perh.)

    piff(9000)  = 1632
    piff(16000) = 2902

    power[piff(9000):piff(16000):1]
'''
def calculate_levels(data, chunk, sample_rate):
    data = unpack("%dh"%(len(data)/2),data)
    data = np.array(data, dtype='h')

    # Apply FFT - real data
    fourier = np.fft.rfft(data)
    # Remove last element in array to make it the same size as chunk
    fourier = np.delete(fourier, len(fourier)-1)
    # Find average 'amplitude' for specific frequency ranges in Hz
    power = np.abs(fourier)



    height[0] = int(np.mean(power[piff(9000):piff(16000):1])/1)
    height[1] = int(np.mean(power[piff(9000):piff(16000):1])/10)
    height[2] = int(np.mean(power[piff(9000):piff(16000):1])/100)
    height[3] = int(np.mean(power[piff(9000):piff(16000):1])/1000)
    height[4] = int(np.mean(power[piff(9000):piff(16000):1])/10000)
    height[5] = int(np.mean(power[piff(9000):piff(16000):1])/100000)
    height[6] = int(np.mean(power[piff(9000):piff(16000):1])/1000000)
    height[7] = int(np.mean(power[piff(9000):piff(16000):1])/10000000)
    height[8] = int(np.mean(power[piff(9000):piff(16000):1])/100000000)
    height[9] = int(np.mean(power[piff(9000):piff(16000):1])/1000000000)




    print(height)
    print("testing for the goods::  ")
    print(power[piff(9000):piff(16000):1])
    return height

height = {9:0,8:0,7:0,6:0,5:0,4:0,3:0,2:0,1:0,0:0}

def red(y):
    if(y < 2): return 0
    if(y > 13): return 255
    return 255/16*y

def green(y):
    if(y > 13): return 0
    if(y < 2): return 255
    return 19*(19/y)

def piff(val):
    return int(2*chunk*val/sample_rate)

'''

'''

class SoundManager(SampleBase):
    def __init__(self, *args, **kwargs):
        super(SoundManager, self).__init__(*args, **kwargs)
