import matplotlib.pyplot as plt
import numpy as np

file_kerma = open("Kerma_newtry.txt","r")
x= []
y = []
K = []
r = []

for l in file_kerma:
    row = l.split()

    #print row[1]
    x.append(float(row[0]))
    y.append(float(row[1]))

    r = float(np.sqrt(row[0]*row[0] + row[1]*row[1]))

    K.append(float(row[2]))

plt.plot(r,K,'o')
