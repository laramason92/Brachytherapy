from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

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

ref_file_GL_0 = open("ref_GL_TG43_orig_0.txt", "r")
ref_file_GL_10 = open("ref_GL_TG43_orig_10.txt", "r")
ref_file_GL_20 = open("ref_GL_TG43_orig_20.txt", "r")
ref_file_GL_30 = open("ref_GL_TG43_orig_30.txt", "r")
ref_file_GL_40 = open("ref_GL_TG43_orig_40.txt", "r")
ref_file_GL_50 = open("ref_GL_TG43_orig_50.txt", "r")
ref_file_GL_60 = open("ref_GL_TG43_orig_60.txt", "r")
ref_file_GL_90 = open("ref_GL_TG43_orig_90.txt", "r")

r_GL_0 = []
r_GL_10 = []
r_GL_20 = []
r_GL_30 = []
r_GL_40 = []
r_GL_50 = []
r_GL_60 = []
r_GL_70 = []
r_GL_80 = []
r_GL_90 = []

ref_r_GL_0 = []
ref_r_GL_10 = []
ref_r_GL_20 = []
ref_r_GL_30 = []
ref_r_GL_40 = []
ref_r_GL_50 = []
ref_r_GL_60 = []
ref_r_GL_90 = []

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

ref_GL_0 = []
ref_GL_10 = []
ref_GL_20 = []
ref_GL_30 = []
ref_GL_40 = []
ref_GL_50 = []
ref_GL_60 = []
ref_GL_90 = []

U_GL_0 = []
U_GL_10 = []
U_GL_20 = []
U_GL_30 = []
U_GL_40 = []
U_GL_50 = []
U_GL_60 = []
U_GL_70 = []
U_GL_80 = []
U_GL_90 = []

#************ theta = 0 ******************
for l in file_GL_0:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
	    r_GL_0.append(float(row[0])) #/10 to get to cm
	    GL_0.append(float(row[1]))
	    U_GL_0.append(float(row[2]))

     elif float(row[0])<=0.5:
	    r_GL_0.append(float(row[0])) #/10 to get to cm
	    GL_0.append(float(row[1]))
	    U_GL_0.append(float(row[2]))

for m in ref_file_GL_0:
    row = m.split()
    ref_r_GL_0.append(float(row[0]))
    ref_GL_0.append(float(row[1]))


plt.plot(ref_r_GL_0,ref_GL_0,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_0,GL_0,yerr=U_GL_0, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.xlim([0.3,10])
plt.ylim([0,3.5])
plt.show()


#************ theta = 10 ******************
for l in file_GL_10:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
	    r_GL_10.append(float(row[0])) #/10 to get to cm
	    GL_10.append(float(row[1]))
	    U_GL_10.append(float(row[2]))

     elif float(row[0])<=0.5:
	    r_GL_10.append(float(row[0])) #/10 to get to cm
	    GL_10.append(float(row[1]))
	    U_GL_10.append(float(row[2]))

for m in ref_file_GL_10:
    row = m.split()
    ref_r_GL_10.append(float(row[0]))
    ref_GL_10.append(float(row[1]))


plt.plot(ref_r_GL_10,ref_GL_10,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_10,GL_10,yerr=U_GL_10, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 20 ******************
for l in file_GL_20:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_20.append(float(row[0])) #/10 to get to cm
            GL_20.append(float(row[1]))
            U_GL_20.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_20.append(float(row[0])) #/10 to get to cm
            GL_20.append(float(row[1]))
            U_GL_20.append(float(row[2]))
            
for m in ref_file_GL_20:
    row = m.split()
    ref_r_GL_20.append(float(row[0]))
    ref_GL_20.append(float(row[1]))


plt.plot(ref_r_GL_20,ref_GL_20,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_20,GL_20,yerr=U_GL_20, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 30 ******************
for l in file_GL_30:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_30.append(float(row[0])) #/10 to get to cm
            GL_30.append(float(row[1]))
            U_GL_30.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_30.append(float(row[0])) #/10 to get to cm
            GL_30.append(float(row[1]))
            U_GL_30.append(float(row[2]))
            
for m in ref_file_GL_30:
    row = m.split()
    ref_r_GL_30.append(float(row[0]))
    ref_GL_30.append(float(row[1]))


plt.plot(ref_r_GL_30,ref_GL_30,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_30,GL_30,yerr=U_GL_30, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 40 ******************
for l in file_GL_40:

    row = l.split()
    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_40.append(float(row[0])) #/10 to get to cm
            GL_40.append(float(row[1]))
            U_GL_40.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_40.append(float(row[0])) #/10 to get to cm
            GL_40.append(float(row[1]))
            U_GL_40.append(float(row[2]))
            
for m in ref_file_GL_40:
    row = m.split()
    ref_r_GL_40.append(float(row[0]))
    ref_GL_40.append(float(row[1]))



plt.plot(ref_r_GL_40,ref_GL_40,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_40,GL_40,yerr=U_GL_40, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()


#************ theta = 50 ******************
for l in file_GL_50:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_50.append(float(row[0])) #/10 to get to cm
            GL_50.append(float(row[1]))
            U_GL_50.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_50.append(float(row[0])) #/10 to get to cm
            GL_50.append(float(row[1]))
            U_GL_50.append(float(row[2]))
            
for m in ref_file_GL_50:
    row = m.split()
    ref_r_GL_50.append(float(row[0]))
    ref_GL_50.append(float(row[1]))


plt.plot(ref_r_GL_50,ref_GL_50,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_50,GL_50,yerr=U_GL_50, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()


#************ theta = 60 ******************
for l in file_GL_60:
    row = l.split()
    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_60.append(float(row[0])) #/10 to get to cm
            GL_60.append(float(row[1]))
            U_GL_60.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_60.append(float(row[0])) #/10 to get to cm
            GL_60.append(float(row[1]))
            U_GL_60.append(float(row[2]))
            
for m in ref_file_GL_60:
    row = m.split()
    ref_r_GL_60.append(float(row[0]))
    ref_GL_60.append(float(row[1]))



plt.plot(ref_r_GL_60,ref_GL_60,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_60,GL_60,yerr=U_GL_60, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 70 ******************
for l in file_GL_70:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_70.append(float(row[0])) #/10 to get to cm
            GL_70.append(float(row[1]))
            U_GL_70.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_70.append(float(row[0])) #/10 to get to cm
            GL_70.append(float(row[1]))
            U_GL_70.append(float(row[2]))
            

plt.errorbar(r_GL_70,GL_70,yerr=U_GL_70, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 80 ******************
for l in file_GL_80:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_80.append(float(row[0])) #/10 to get to cm
            GL_80.append(float(row[1]))
            U_GL_80.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_80.append(float(row[0])) #/10 to get to cm
            GL_80.append(float(row[1]))
            U_GL_80.append(float(row[2]))
            

plt.errorbar(r_GL_80,GL_80,yerr=U_GL_80, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()



#************ theta = 90 ******************
for l in file_GL_90:
    row = l.split()

    if float(row[1])>0:

     if float(row[0])>0.5:
       if float(row[0]) == int(float(row[0])):
            r_GL_90.append(float(row[0])) #/10 to get to cm
            GL_90.append(float(row[1]))
            U_GL_90.append(float(row[2]))

     elif float(row[0])<=0.5:
            r_GL_90.append(float(row[0])) #/10 to get to cm
            GL_90.append(float(row[1]))
            U_GL_90.append(float(row[2]))
            
for m in ref_file_GL_90:
    row = m.split()
    ref_r_GL_90.append(float(row[0]))
    ref_GL_90.append(float(row[1]))


plt.plot(ref_r_GL_90,ref_GL_90,color='red',linestyle='--', marker='o')
plt.errorbar(r_GL_90,GL_90,yerr=U_GL_90, color='green', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,3.5])
plt.show()





