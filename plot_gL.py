from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_gL = open("gL_r.txt", "r")

r_gL = []
gL = []
U_gL = []

for l in file_gL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_gL.append(float(row[0]))
    gL.append(float(row[1]))
    U_gL.append(float(row[2]))

plt.plot(r_gL, gL,'ro')
plt.show()

