import numpy as np
import math
from scipy.signal import hilbert

debug = True

def period_cal(freq):
    return int(1/freq*100)

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

def convertion_to_pixel(data, base=0):
    data = np.array(data)

    if base==0:
        base = np.amax(data)
        
    ind = np.unravel_index(np.argmax(data, axis=None), data.shape)    
    print('# Process base is ', base,ind[0]+1,ind[1]+1)        

    ratio_data = np.true_divide(data, base)
    log_data = np.log(ratio_data)*(-1)
    process_data = log_data/np.amax(log_data)
    
    print("**Log data**")
    print(log_data)

    print("**process data**")
    print(process_data)
    pixel_data = process_data*255
    
    return pixel_data
    
def batch_process_timefly(data, avg_size, times=1):
    pre_data = data

    for i in range(times):
        average_data = averaging(pre_data, avg_size)
        process_data = diff_filter(pre_data, average_data)

        pre_data = process_data
    
    envelop_data = hilbert_trans(process_data)
    argmax_data = argmax(envelop_data)

    return argmax_data

def batch_process_amplitude(data, avg_size, times=1):
    pre_data = data

    for i in range(times):
        average_data = averaging(pre_data, avg_size)
        process_data = diff_filter(pre_data, average_data)

        pre_data = process_data
    
    envelop_data = hilbert_trans(process_data)
    amp_data = max(envelop_data)

    return amp_data

def batch_process2(data, avg_size):
    average_data = averaging(data, avg_size)
    process_data = diff_filter(data, average_data)
    envelop_data = hilbert_trans(process_data)
    argmax_data = argmax(envelop_data)

    return argmax_data


def sample_convertion(data, avg_size, times=1):
    pre_data = data

    for i in range(times):
        average_data = averaging(pre_data, avg_size)
        process_data = diff_filter(pre_data, average_data)

        pre_data = process_data
        
    envelop_data = hilbert_trans(process_data)
    
    return average_data, process_data, envelop_data, max(envelop_data)

def image_process(signal_data, row, col, freq, mode, data_type, avg_level=1, x=1, y=1):
    process_data = []
    period = period_cal(freq)
    image_data = []

    if mode == 'batch':
        print('# Processing Info #')
        print('- Mode: ', mode)
        print('- Data type: ', data_type)
        print('- Size: ', row, 'x', col)
        print('- Average level: ', avg_level)
        print('===============================')
        print('Image Processing ( 0 /',row,')')

        for i in range(1,(row+1)):
            if i%2 == 0:
              print('Image Processing (',i,'/',row,')',)
            row_arr = []
            for j in range(1, (col+1)):
                file_path = signal_data.folder+signal_data.prefix+str(i)+'c'+str(j)+signal_data.suffix
                time, ch1, ch2 = signal_data.data_load(file_path)
                if data_type == 'time':
                    result = batch_process_timefly(ch1, period, avg_level) 
                else:
                    result = batch_process_amplitude(ch1, period, avg_level) 
                #print(file_path)
                
                row_arr.append(result)

            process_data.append(row_arr)
            
        print('===============================')
        print('processData result:')
        print(process_data)
        np.savetxt('process_data.txt',process_data)

        #used 2600 for previous experiment

        image_data = convertion_to_pixel(process_data)    
        np.savetxt('image_data.txt',image_data)
        return image_data

    elif mode == 'sample':
        print("# Start sample process of point (", x,',', y,')')
        file_path = signal_data.folder+signal_data.prefix+str(x)+'c'+str(y)+signal_data.suffix
        time, ch1, ch2 = signal_data.data_load(file_path)
        print(file_path)
        avg, pro, env, maxVal = sample_convertion(ch1, period, 8)
        
        return time, ch1, avg, pro, env, print(maxVal)
    else:
        return print('ERROR: select mode for image processing') 