from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_kerma = open("geant4_dose_280M.txt", "r")
y,K = [],[]

for l in file_kerma:
    row = l.split()

    #print row[1]
    y.append(float(row[0])) #/10 to get to cm
    K.append(float(row[1]))

#print K


ky2 = []
yplot = []
for i in range(len(K)):
    #if (y[i]).is_integer():
    yplot.append(y[i])
    val = y[i]*y[i]*K[i]
    ky2.append(val)
    print "y   ", y[i],"   K   ",K[i],"   y^2   ", y[i]*y[i], "   Ky^2   ", K[i]*y[i]*y[i] 
plt.plot(y,ky2,'ro')

#plt.plot(y,K,'x')
plt.show()

def f(x, A, B): # this is your 'straight line' y=f(x)
    return A*x + B

A,B = curve_fit(f, y, ky2)[0] # your data x, y to fit
print "A", A
print "B", B
