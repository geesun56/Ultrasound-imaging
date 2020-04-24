import csv

points = 350

def data_load(path):
    time = []
    ch1 = []
    ch2 = []

    with open(path, encoding='windows-1252') as csvfile:
        reader = csv.DictReader(csvfile)
        i = 0
        for row in reader:
            i+=1
            #print(row)
            if i > 19 and None in row:
                #wave_data.append([float(row['#Digilent WaveForms Oscilloscope Acquisition']), float(row[None][0])])
                ch1.append(float(row[None][0]))
                ch2.append(float(row[None][1]))

    # truncate data points
    
    ch1 = ch1[points:]
    ch2 = ch2[points:]

    for i in range(len(ch1)):
        time.append(i)
    
    return time, ch1, ch2
