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


plt.plot(ref_r_GL_0,ref_GL_0,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_0,GL_0,yerr=U_GL_0, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
#plt.xlim([0.3,10])
plt.ylim([0,5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 4.5, r'$\theta = 0$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_0_plot.eps')
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


plt.plot(ref_r_GL_10,ref_GL_10,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_10,GL_10,yerr=U_GL_10, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 10$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_10_plot.eps')
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


plt.plot(ref_r_GL_20,ref_GL_20,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_20,GL_20,yerr=U_GL_20, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 20$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_20_plot.eps')
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


plt.plot(ref_r_GL_30,ref_GL_30,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_30,GL_30,yerr=U_GL_30, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 30$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_30_plot.eps')
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



plt.plot(ref_r_GL_40,ref_GL_40,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_40,GL_40,yerr=U_GL_40, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.legend()
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 40$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_40_plot.eps')
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


plt.plot(ref_r_GL_50,ref_GL_50,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_50,GL_50,yerr=U_GL_50, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 50$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_50_plot.eps')
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



plt.plot(ref_r_GL_60,ref_GL_60,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_60,GL_60,yerr=U_GL_60, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.legend()
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 60$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_60_plot.eps')
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
            

plt.errorbar(r_GL_70,GL_70,yerr=U_GL_70, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 70$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_70_plot.eps')
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
            

plt.errorbar(r_GL_80,GL_80,yerr=U_GL_80, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.legend()
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 80$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_80_plot.eps')
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


plt.plot(ref_r_GL_90,ref_GL_90,color='red',label='Ref. Data',linestyle='--', marker='o')
plt.errorbar(r_GL_90,GL_90,yerr=U_GL_90, color='green',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='green')
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$r^2G(r,\theta)/G(r_0,\theta_0)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 1.75, r'$\theta = 90$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('GL_theta_90_plot.eps')
plt.show()





