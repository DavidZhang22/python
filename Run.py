import csv
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as ss
things = []

with open('Sheet7.csv') as file:
    reader = csv.reader(file)
    arr = []
    y = []
    for row in reader:
        arr.append([float(row[0]), float(row[1])])
        y.append(float(row[1]))

    prev = [0,0]
    '''for i in range(1, len(arr) - 1):
        if (arr[i - 1][1] <= arr[i][1] and arr[i][1] >= arr[i + 1][1] and arr[i][1]>0.4):
            if (prev != arr[i][1] and arr[i][0]-prev[0]>=1 ):
                things.append(arr[i])
                prev[0][1] = arr[i];


    print('Time,Value')
    for row in things:
        print(str(row[0]) + ',' + str(row[1]))
    '''
    
    y = np.asarray(y)
    a = ss.argrelmax(y, order = 3)
    x = np.arange(0, 60, 0.02);
    a = np.asarray(a)

    for i in range(len(a[0]-1)):        
        print(str(x[a[0][i]] ))
    for i in range(len(a[0]-1)):  
        print(str(y[a[0][i]] ))
