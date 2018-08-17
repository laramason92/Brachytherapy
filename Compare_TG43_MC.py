from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

Sk = 40716
Lambda = 1.117

file_GL_0 = open("GL_r_theta_0.txt", "r")
file_GL_10 = open("GL_r_theta_10.txt", "r")
file_GL_20 = open("GL_r_theta_20.txt", "r")
file_GL_30 = open("GL_r_theta_30.txt", "r")
file_GL_40 = open("GL_r_theta_40.txt", "r")
file_GL_50 = open("GL_r_theta_50.txt", "r")
file_GL_60 = open("GL_r_theta_60.txt", "r")
file_GL_70 = open("GL_r_theta_70.txt", "r")
file_GL_80 = open("GL_r_theta_80.txt", "r")
file_GL_90 = open("GL_r_theta_90.txt", "r")

file_F_0 = open("estro_FL_0.txt")
file_F_10 = open("estro_FL_10.txt")
file_F_20 = open("estro_FL_20.txt")
file_F_30 = open("estro_FL_30.txt")
file_F_40 = open("estro_FL_40.txt")
file_F_50 = open("estro_FL_50.txt")
file_F_60 = open("estro_FL_60.txt")
file_F_70 = open("estro_FL_70.txt")
file_F_80 = open("estro_FL_80.txt")
file_F_90 = open("estro_FL_90.txt")

file_gL = open("estro_gL.txt")

r_0 = []
r_10 = []
r_20 = []
r_30 = []
r_40 = []
r_50 = []
r_60 = []
r_70 = []
r_80 = []
r_90 = []

FL_0 = []
FL_10 = []
FL_20 = []
FL_30 = []
FL_40 = []
FL_50 = []
FL_60 = []
FL_70 = []
FL_80 = []
FL_90 = []

GL_0 = []
GL_10 = []
GL_20 = []
GL_30 = []
GL_40 = []
GL_50 = []
GL_60 = []
GL_70 = []
GL_80 = []
GL_90 = []

gL = []

dose_TG43_0 = []
dose_TG43_10 = []
dose_TG43_20 = []
dose_TG43_30 = []
dose_TG43_40 = []
dose_TG43_50 = []
dose_TG43_60 = []
dose_TG43_70 = []
dose_TG43_80 = []
dose_TG43_90 = []

#**************************************

for l in file_gL:
    row = l.split()

    gL.append(float(row[1]))


#************ theta = 0 ******************
for l in file_F_0:
    row = l.split()

    FL_0.append(float(row[1]))


#************ theta = 10 ******************
for l in file_F_10:
    row = l.split()

    FL_10.append(float(row[1]))


#************ theta = 20 ******************
for l in file_F_20:
    row = l.split()

    FL_20.append(float(row[1]))


#************ theta = 30 ******************
for l in file_F_30:
    row = l.split()

    FL_30.append(float(row[1]))


#************ theta = 40 ******************
for l in file_F_40:
    row = l.split()

    FL_40.append(float(row[1]))


#************ theta = 50 ******************
for l in file_F_50:
    row = l.split()

    FL_50.append(float(row[1]))


#************ theta = 60 ******************
for l in file_F_60:
    row = l.split()

    FL_60.append(float(row[1]))


#************ theta = 70 ******************
for l in file_F_70:
    row = l.split()

    FL_70.append(float(row[1]))


#************ theta = 80 ******************
for l in file_F_80:
    row = l.split()

    FL_80.append(float(row[1]))


#************ theta = 90 ******************
for l in file_F_90:
    row = l.split()

    FL_90.append(float(row[1]))

#************ theta = 0 ******************
for l in file_GL_0:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_0.append(float(row[0])) #/10 to get to cm
		    GL_0.append(float(row[1]))

#************ theta = 10 ******************
for l in file_GL_10:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_10.append(float(row[0])) #/10 to get to cm
		    GL_10.append(float(row[1]))

#************ theta = 20 ******************
for l in file_GL_20:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_20.append(float(row[0])) #/10 to get to cm
		    GL_20.append(float(row[1]))

#************ theta = 30 ******************
for l in file_GL_30:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_30.append(float(row[0])) #/10 to get to cm
		    GL_30.append(float(row[1]))

#************ theta = 40 ******************
for l in file_GL_40:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_40.append(float(row[0])) #/10 to get to cm
		    GL_40.append(float(row[1]))

#************ theta = 50 ******************
for l in file_GL_50:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_50.append(float(row[0])) #/10 to get to cm
		    GL_50.append(float(row[1]))

#************ theta = 60 ******************
for l in file_GL_60:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
		    r_60.append(float(row[0])) #/10 to get to cm
		    GL_60.append(float(row[1]))

#************ theta = 70 ******************
for l in file_GL_70:
    row = l.split()

    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:

	    if float(row[0]) == int(float(row[0])):
		    r_70.append(float(row[0])) #/10 to get to cm
		    GL_70.append(float(row[1]))

#************ theta = 80 ******************
for l in file_GL_80:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:


	    if float(row[0]) == int(float(row[0])):
                 
		    r_80.append(float(row[0])) #/10 to get to cm
		    GL_80.append(float(row[1]))

#************ theta = 90 ******************
for l in file_GL_90:
    row = l.split()

    #if float(row[1])>0:
    if float(row[0])>0:
	if float(row[0])!=7:
	  if float(row[0])!=9:

	    if float(row[0]) == int(float(row[0])):
		    r_90.append(float(row[0])) #/10 to get to cm
		    GL_90.append(float(row[1]))

#********************************************

for i in range(len(r_0)):

  dose_TG43 = Sk * Lambda * (GL_0[i]/(r_0[i]*r_0[i])) * gL[i] * FL_0[i]
  dose_TG43_0.append(dose_TG43)

#********************************************

for i in range(len(r_10)):

  dose_TG43 = Sk * Lambda * (GL_10[i]/(r_10[i]*r_10[i])) * gL[i] * FL_10[i]
  dose_TG43_10.append(dose_TG43)

#********************************************

for i in range(len(r_20)):

  dose_TG43 = Sk * Lambda * (GL_20[i]/(r_20[i]*r_20[i])) * gL[i] * FL_20[i]
  dose_TG43_20.append(dose_TG43)

#********************************************

for i in range(len(r_30)):

  dose_TG43 = Sk * Lambda * (GL_30[i]/(r_30[i]*r_30[i])) * gL[i] * FL_30[i]
  dose_TG43_30.append(dose_TG43)

#********************************************

for i in range(len(r_40)):

  dose_TG43 = Sk * Lambda * (GL_40[i]/(r_40[i]*r_40[i])) * gL[i] * FL_40[i]
  dose_TG43_40.append(dose_TG43)

#********************************************

for i in range(len(r_50)):

  dose_TG43 = Sk * Lambda * (GL_50[i]/(r_50[i]*r_50[i])) * gL[i] * FL_50[i]
  dose_TG43_50.append(dose_TG43)

#********************************************

for i in range(len(r_60)):

  dose_TG43 = Sk * Lambda * (GL_60[i]/(r_60[i]*r_60[i])) * gL[i] * FL_60[i]
  dose_TG43_60.append(dose_TG43)

#********************************************

for i in range(len(r_70)):

  dose_TG43 = Sk * Lambda * (GL_70[i]/(r_70[i]*r_70[i])) * gL[i] * FL_70[i]
  dose_TG43_70.append(dose_TG43)

#********************************************

for i in range(len(r_80)):

  dose_TG43 = Sk * Lambda * (GL_80[i]/(r_80[i]*r_80[i])) * gL[i] * FL_80[i]
  dose_TG43_80.append(dose_TG43)

#********************************************

for i in range(len(r_90)):

  dose_TG43 = Sk * Lambda * (GL_90[i]/(r_90[i]*r_90[i])) * gL[i] * FL_90[i]
  dose_TG43_90.append(dose_TG43)

print dose_TG43_90




