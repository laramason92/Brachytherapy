from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_dose = open("geant4_dose_with_theta.txt", "r")
file_GL = open("GL_r_theta.txt", "r")
file_gL = open("gL_r.txt", "r")
file_F = open("F_r_theta.txt", "r")

r_dose = []
r_F = []
r_gL = []
r_GL = []

theta_dose = []
theta_F = []
theta_GL = []

D = []
GL = []
gL = []
F = []

U_D = []
U_GL = []
U_gL = []
U_F = []

for l in file_dose:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_dose.append(float(row[0])) #/10 to get to cm
    theta_dose.append(float(row[1]))
    D.append(float(row[2]))    
    U_D.append(float(row[3]))

GL_theta_0 = []
r_GL_theta_0 = []

for l in file_GL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_GL.append(float(row[0])) #/10 to get to cm
    theta_GL.append(float(row[1]))
    GL.append(float(row[2]))    
    U_GL.append(float(row[3]))

    if float(row[1]) == 45:
      GL_theta_0.append(float(row[2]))
      r_GL_theta_0.append(float(row[0]))

plt.plot(r_GL_theta_0,GL_theta_0)
plt.show() 

for l in file_F:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_F.append(float(row[0])) #/10 to get to cm
    theta_F.append(float(row[1]))
    F.append(float(row[2]))    
    U_F.append(float(row[3]))


for l in file_gL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_gL.append(float(row[0])) #/10 to get to cm
    gL.append(float(row[1]))    
    U_gL.append(float(row[2]))

#plt.plot(r_gL, gL,'ro')
#plt.show()
