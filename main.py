import processing
from data import signalData; 
from matplotlib import pyplot as plt
from processing import image_process

# Data directory
folder_path = './data/04142020'


# Configuration
data_rows = 40
data_cols = 40
frequency = 4 # 4MHz - 25 usec period: 25 entries = signal data during 25 usec
mode = "batch"
data_type = "amplitude"
x = 9
y = 3
signal_data = signalData(folder_path)



if mode == 'batch':
    image_data = processing.image_process(signal_data, data_rows, data_cols, frequency, mode, data_type, x, y)
    plt.figure(figsize=(20,20))

    #use imshow to plot the array
    plt.subplot(131)
    plt.imshow(image_data,                         #numpy array generating the image
            cmap = 'gray',             #color map used to specify colors
            interpolation='nearest'    #algorithm used to blend square colors; with 'nearest' colors will not be blended
            )
    plt.xticks(range(data_cols))
    plt.yticks(range(data_rows))
    plt.title('Gray color map, no blending', y=1.02, fontsize=12)

    plt.show()
elif mode == 'sample':
    # sample process
    time, ch1, avg, process, envelop  = processing.image_process(signal_data, data_rows, data_cols, frequency, mode, x, y)


    fig = plt.figure()

    plt.title('original data')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(time, ch1)

    plt.show()

    plt.title('average data')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(avg)

    plt.show()

    plt.title('diff_filter data')
    plt.xlabel('time')
    plt.ylabel('amplitude')
    plt.plot(process)
    plt.plot(envelop)

    plt.show()

else:
    print("Error: specify mode")


'''print(time)
print(ch1)
print(ch2)'''


'''

'''

'''
    dataset assumption
    each time difference is approximately 10 nsec

'''




    

    