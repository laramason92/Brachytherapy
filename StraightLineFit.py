from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_kerma = open("Kerma.txt", "r")
y,K = [],[]
for l in file_kerma:
    row = l.split()
    #print row[0], row[1]
    y.append(float(row[0]))
    K.append(float(row[1]))

ky2 = []
for i in range(len(K)):
    val = y[i]**2*K[i]
    ky2.append(val)
plt.plot(y,ky2,'ro')
plt.show()

def f(x, A, B): # this is your 'straight line' y=f(x)
    return A*x + B

A,B = curve_fit(f, y, ky2)[0] # your data x, y to fit
print "A", A
print "B", B
