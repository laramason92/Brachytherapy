from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_dose = open("geant4_dose_with_theta.txt", "r")
file_GL = open("geant4_dose_with_theta.txt", "r")
file_gL = open("geant4_dose_with_theta.txt", "r")
file_F = open("geant4_dose_with_theta.txt", "r")

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


