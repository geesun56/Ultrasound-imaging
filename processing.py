import numpy as np
import math
from scipy.signal import hilbert

debug = True

def period_cal(freq):
    return 1/freq

def averaging(data, avg_size):
    avg_data = []
    for i in range(0, len(data)-avg_size):
        avg_data.append(math.fsum(data[i:i+avg_size])/avg_size)
    
    return avg_data

def diff_filter(data, avg_data):
    diff_data = []
    for i in range(len(avg_data)):
        diff_data.append(avg_data[i] - data[i])
    
    return diff_data

def hilbert_trans(data):
    envelop = hilbert(data)
    envelop = abs(envelop)

    return envelop 

def argmax(data):
    max_point = np.argmax(data, axis=0)

    return max_point

def imaging(preprocess):
    max_val = np.argmax(preprocess, axis=0)
    print(max_val)

    return max_val

def convertion_to_pixel(data):
    base = 2600
    max_point = np.argmax(data, axis=0)
    ratio = max_point/base
    if ratio > 1:
        ratio = 1
    pixel_data = np.round(ratio*255)
    
    if debug :
        print("Convertion test: ", max_point, ratio, pixel_data)

    return pixel_data
    
def batch_process1(data, avg_size):
    average_data = averaging(data, avg_size)
    process_data = diff_filter(data, average_data)
    envelop_data = hilbert_trans(process_data)
    pixel_data = convertion_to_pixel(envelop_data)

    return pixel_data

def batch_process2(data, avg_size):
    average_data = averaging(data, avg_size)
    process_data = diff_filter(data, average_data)
    envelop_data = hilbert_trans(process_data)
    argmax_data = argmax(envelop_data)

    return argmax_data


def sample_convertion(data, avg_size):
    average_data = averaging(data, avg_size)
    process_data = diff_filter(data, average_data)
    envelop_data = hilbert_trans(process_data)
    pixel_data = convertion_to_pixel(envelop_data)

    return average_data, process_data, envelop_data, pixel_data

def image_process(obj):
    print(obj.folder, obj.prefix, obj.suffix)