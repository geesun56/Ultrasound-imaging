import processing
from data import data_load 
from matplotlib import pyplot as plt

# Data directory
folder = './data/04142020'
sample_file = '/data_r1c1.csv'
prefix = '/data_r'
suffix = '.csv'

# Configuration
data_rows = 40
data_cols = 40
average_size = 25 # 4MHz - 25 usec period: 25 entries = signal data during 25 usec

sample_path = folder + sample_file 
time, ch1, ch2 = data_load(sample_path)
avg, process, envelop, pixel = processing.sample_convertion(ch1, average_size)

'''
    dataset assumption
    each time difference is approximately 1 usec

'''


'''
batch_process
image_data = []

for i in range(1,data_rows+1):
    row = []
    for j in range(1, data_cols+1):
        file_path = folder+prefix+str(i)+'c'+str(j)+suffix
        print(file_path)
        time, ch1, ch2 = data_load(file_path)
        row.append(processing.oneshot_convertion(ch1, average_size))
    image_data.append(row)


print(image_data)

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

'''

'''print(time)
print(ch1)
print(ch2)'''




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


plt.title('diff_filter data')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.plot(process)

plt.show()


    

    