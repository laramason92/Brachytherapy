from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

file_F_0 = open("F_r_theta_0.txt", "r")
file_F_10 = open("F_r_theta_10.txt", "r")
file_F_20 = open("F_r_theta_20.txt", "r")
file_F_30 = open("F_r_theta_30.txt", "r")
file_F_40 = open("F_r_theta_40.txt", "r")
file_F_50 = open("F_r_theta_50.txt", "r")
file_F_60 = open("F_r_theta_60.txt", "r")
file_F_70 = open("F_r_theta_70.txt", "r")
file_F_80 = open("F_r_theta_80.txt", "r")
file_F_90 = open("F_r_theta_90.txt", "r")

r_F_0 = []
r_F_10 = []
r_F_20 = []
r_F_30 = []
r_F_40 = []
r_F_50 = []
r_F_60 = []
r_F_70 = []
r_F_80 = []
r_F_90 = []

F_0 = []
F_10 = []
F_20 = []
F_30 = []
F_40 = []
F_50 = []
F_60 = []
F_70 = []
F_80 = []
F_90 = []

U_F_0 = []
U_F_10 = []
U_F_20 = []
U_F_30 = []
U_F_40 = []
U_F_50 = []
U_F_60 = []
U_F_70 = []
U_F_80 = []
U_F_90 = []

ref_file_F_0 = open("Ballester_F_theta_0.txt", "r")
ref_file_F_10 = open("Ballester_F_theta_10.txt", "r")
ref_file_F_20 = open("Ballester_F_theta_20.txt", "r")
ref_file_F_30 = open("Ballester_F_theta_30.txt", "r")
ref_file_F_40 = open("Ballester_F_theta_40.txt", "r")
ref_file_F_50 = open("Ballester_F_theta_50.txt", "r")
ref_file_F_60 = open("Ballester_F_theta_60.txt", "r")
ref_file_F_70 = open("Ballester_F_theta_70.txt", "r")
ref_file_F_80 = open("Ballester_F_theta_80.txt", "r")
ref_file_F_90 = open("Ballester_F_theta_90.txt", "r")

ref_r_F_0 = []
ref_r_F_10 = []
ref_r_F_20 = []
ref_r_F_30 = []
ref_r_F_40 = []
ref_r_F_50 = []
ref_r_F_60 = []
ref_r_F_70 = []
ref_r_F_80 = []
ref_r_F_90 = []

ref_F_0 = []
ref_F_10 = []
ref_F_20 = []
ref_F_30 = []
ref_F_40 = []
ref_F_50 = []
ref_F_60 = []
ref_F_70 = []
ref_F_80 = []
ref_F_90 = []


r_plot = [0.4,0.5,0.7,1,1.5,2,3,4,5,6,7,8,9]
#************ theta = 0 ******************
r_0_plot = [0.4,0.5,0.7,1,1.5,2,3,4,5,6]

for l in ref_file_F_0:
    row = l.split()

    ref_r_F_0.append(float(row[0])) #/10 to get to cm
    ref_F_0.append(float(row[1]))

for l in file_F_0:
    row = l.split()

    r_F_0.append(float(row[0])) #/10 to get to cm
    F_0.append(float(row[1]))
    U_F_0.append(float(row[2]))

F_plot_0 = [0.]*10
F_plot_err_0 = [0.]*10

for l in range(len(F_0)):

 if r_F_0[l]==0.4: #if r_F_0[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_0[0] += F_0[l]
    F_plot_err_0[0] += U_F_0[l]

 if r_F_0[l]==0.5:   #if r_F_0[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_0[1] += F_0[l]
    F_plot_err_0[1] += U_F_0[l]

 if r_F_0[l]==0.7:     #if r_F_0[l]>=0.625 and r_F[l]<0.775: #0.75
    F_plot_0[2] += F_0[l]
    F_plot_err_0[2] += U_F_0[l]

 if r_F_0[l]==0.9: #if r_F_0[l]>=0.775 and r_F[l]<1.25: #1
    F_plot_0[3] += F_0[l]
    F_plot_err_0[3] += U_F_0[l]

 if r_F_0[l]==1.4: #if r_F_0[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_0[4] += F_0[l]
    F_plot_err_0[4] += U_F_0[l]

 if r_F_0[l]==2: #if r_F_0[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_0[5] += F_0[l]
    F_plot_err_0[5] += U_F_0[l]

 if r_F_0[l]==2.9: #if r_F_0[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_0[6] += F_0[l]
    F_plot_err_0[6] += U_F_0[l]

 if r_F_0[l]==4.2: #if r_F_0[l]>=3.5 and r_F[l]<4.5: #4
    F_plot_0[7] += F_0[l]
    F_plot_err_0[7] += U_F_0[l]


 if r_F_0[l]==5: #if r_F_0[l]>=4.5 and r_F[l]<5.5: #5
    F_plot_0[8] += F_0[l]
    F_plot_err_0[8] += U_F_0[l]

 if r_F_0[l]==5.9: #if r_F_0[l]>=5.5 and r_F[l]<6.5: #6
    F_plot_0[9] += F_0[l]
    F_plot_err_0[9] += U_F_0[l]

print r_plot
print F_plot_0
print F_plot_err_0

plt.errorbar(r_0_plot,F_plot_0,yerr=F_plot_err_0, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_0, ref_F_0,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlim([0,7])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 0$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_0_plot.eps')
plt.show()


#************ theta = 0 ******************
r_10_plot = [1.2,1.5,2,2.5,3,4,5,6]
for l in ref_file_F_10:
    row = l.split()

    ref_r_F_10.append(float(row[0])) #/10 to get to cm
    ref_F_10.append(float(row[1]))

for l in file_F_10:
    row = l.split()

    r_F_10.append(float(row[0])) #/10 to get to cm
    F_10.append(float(row[1]))
    U_F_10.append(float(row[2]))

F_plot_10 = [0.]*8
F_plot_err_10 = [0.]*8

for l in range(len(F_10)):

 if r_F_10[l]==1.2: #if r_F_10[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_10[0] += F_10[l]
    F_plot_err_10[0] += U_F_10[l]

 if r_F_10[l]==1.5:   #if r_F_10[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_10[1] += F_10[l]
    F_plot_err_10[1] += U_F_10[l]

 if r_F_10[l]==2.0:     #if r_F_10[l]>=0.625 and r_F[l]<0.775: #0.75
    F_plot_10[2] += F_10[l]
    F_plot_err_10[2] += U_F_10[l]

 if r_F_10[l]==2.3: #if r_F_10[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_10[3] += F_10[l]
    F_plot_err_10[3] += U_F_10[l]

 if r_F_10[l]==2.7: #if r_F_10[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_10[4] += F_10[l]
    F_plot_err_10[4] += U_F_10[l]

 if r_F_10[l]==3.8: #if r_F_10[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_10[5] += F_10[l]
    F_plot_err_10[5] += U_F_10[l]

 if r_F_10[l]==5: #if r_F_10[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_10[6] += F_10[l]
    F_plot_err_10[6] += U_F_10[l]

 if r_F_10[l]==5.9: #if r_F_10[l]>=3.5 and r_F[l]<4.5: #4
    F_plot_10[7] += F_10[l]
    F_plot_err_10[7] += U_F_10[l]


print r_plot
print F_plot_10
print F_plot_err_10

plt.errorbar(r_10_plot,F_plot_10,yerr=F_plot_err_10, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_10, ref_F_10,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.xlim([0,7])
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 10$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_10_plot.eps')
plt.show()


#************ theta = 20 ******************
r_20_plot = [0.3,0.8,1,2,4.1,5,6]

for l in ref_file_F_20:
    row = l.split()

    ref_r_F_20.append(float(row[0])) #/10 to get to cm
    ref_F_20.append(float(row[1]))

for l in file_F_20:
    row = l.split()

    r_F_20.append(float(row[0])) #/10 to get to cm
    F_20.append(float(row[1]))
    U_F_20.append(float(row[2]))

F_plot_20 = [0.]*7
F_plot_err_20 = [0.]*7

for l in range(len(F_20)):

 if r_F_20[l]==0.3: #if r_F_20[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_20[0] += F_20[l]
    F_plot_err_20[0] += U_F_20[l]

 if r_F_20[l]==0.8:   #if r_F_20[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_20[1] += F_20[l]
    F_plot_err_20[1] += U_F_20[l]

 if r_F_20[l]==1.2:     #if r_F_20[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_20[2] += F_20[l]
    F_plot_err_20[2] += U_F_20[l]

 if r_F_20[l]==2: #if r_F_20[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_20[3] += F_20[l]
    F_plot_err_20[3] += U_F_20[l]

 if r_F_20[l]==4.1: #if r_F_20[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_20[4] += F_20[l]
    F_plot_err_20[4] += U_F_20[l]

 if r_F_20[l]==5.1: #if r_F_20[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_20[5] += F_20[l]
    F_plot_err_20[5] += U_F_20[l]

 if r_F_20[l]==6: #if r_F_20[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_20[6] += F_20[l]
    F_plot_err_20[6] += U_F_20[l]


print r_plot
print F_plot_20
print F_plot_err_20

plt.errorbar(r_20_plot,F_plot_20,yerr=F_plot_err_20, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_20, ref_F_20,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.xlim([0,7])
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 20$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_20_plot.eps')
plt.show()


#************ theta = 30 ******************
r_30_plot = [0.2,0.6,0.8,2,3,4,5]
for l in ref_file_F_30:
    row = l.split()

    ref_r_F_30.append(float(row[0])) #/10 to get to cm
    ref_F_30.append(float(row[1]))

for l in file_F_30:
    row = l.split()

    r_F_30.append(float(row[0])) #/10 to get to cm
    F_30.append(float(row[1]))
    U_F_30.append(float(row[2]))

F_plot_30 = [0.]*7
F_plot_err_30 = [0.]*7

for l in range(len(F_30)):

 if r_F_30[l]==0.2: #if r_F_30[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_30[0] += F_30[l]
    F_plot_err_30[0] += U_F_30[l]

 if r_F_30[l]==0.6:   #if r_F_30[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_30[1] += F_30[l]
    F_plot_err_30[1] += U_F_30[l]

 if r_F_30[l]==0.8:     #if r_F_30[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_30[2] += F_30[l]
    F_plot_err_30[2] += U_F_30[l]

 if r_F_30[l]==2.1: #if r_F_30[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_30[3] += F_30[l]
    F_plot_err_30[3] += U_F_30[l]

 if r_F_30[l]==3: #if r_F_30[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_30[4] += F_30[l]
    F_plot_err_30[4] += U_F_30[l]

 if r_F_30[l]==4.1: #if r_F_30[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_30[5] += F_30[l]
    F_plot_err_30[5] += U_F_30[l]

 if r_F_30[l]==5.9: #if r_F_30[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_30[6] += F_30[l]
    F_plot_err_30[6] += U_F_30[l]

print r_plot
print F_plot_30
print F_plot_err_30

plt.errorbar(r_30_plot,F_plot_30,yerr=F_plot_err_30, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_30, ref_F_30,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.xlim([0,7])
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 30$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_30_plot.eps')
plt.show()


#************ theta = 0 ******************
r_40_plot = [0.4,1,1.2,1.6,2.7,3.9,5.8]
for l in ref_file_F_40:
    row = l.split()

    ref_r_F_40.append(float(row[0])) #/10 to get to cm
    ref_F_40.append(float(row[1]))

for l in file_F_40:
    row = l.split()

    r_F_40.append(float(row[0])) #/10 to get to cm
    F_40.append(float(row[1]))
    U_F_40.append(float(row[2]))

F_plot_40 = [0.]*7
F_plot_err_40 = [0.]*7

for l in range(len(F_40)):

 if r_F_40[l]==0.4: #if r_F_40[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_40[0] += F_40[l]
    F_plot_err_40[0] += U_F_40[l]

 if r_F_40[l]==1:   #if r_F_40[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_40[1] += F_40[l]
    F_plot_err_40[1] += U_F_40[l]

 if r_F_40[l]==1.2:     #if r_F_40[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_40[2] += F_40[l]
    F_plot_err_40[2] += U_F_40[l]

 if r_F_40[l]==1.6: #if r_F_40[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_40[3] += F_40[l]
    F_plot_err_40[3] += U_F_40[l]

 if r_F_40[l]==2.7: #if r_F_40[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_40[4] += F_40[l]
    F_plot_err_40[4] += U_F_40[l]

 if r_F_40[l]==3.9: #if r_F_40[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_40[5] += F_40[l]
    F_plot_err_40[5] += U_F_40[l]

 if r_F_40[l]==5.8: #if r_F_40[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_40[6] += F_40[l]
    F_plot_err_40[6] += U_F_40[l]

print r_plot
print F_plot_40
print F_plot_err_40

plt.errorbar(r_40_plot,F_plot_40,yerr=F_plot_err_40, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_40, ref_F_40,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.xlim([0,7])
plt.text(1, 1.75, r'$\theta = 40$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_40_plot.eps')
plt.show()


#************ theta = 0 ******************
r_50_plot = [0.2,1,2.6,3.1,3.7,5,6.1]
for l in ref_file_F_50:
    row = l.split()

    ref_r_F_50.append(float(row[0])) #/10 to get to cm
    ref_F_50.append(float(row[1]))

for l in file_F_50:
    row = l.split()

    r_F_50.append(float(row[0])) #/10 to get to cm
    F_50.append(float(row[1]))
    U_F_50.append(float(row[2]))

F_plot_50 = [0.]*7
F_plot_err_50 = [0.]*7

for l in range(len(F_50)):

 if r_F_50[l]==0.2: #if r_F_50[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_50[0] += F_50[l]
    F_plot_err_50[0] += U_F_50[l]

 if r_F_50[l]==1:   #if r_F_50[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_50[1] += F_50[l]
    F_plot_err_50[1] += U_F_50[l]

 if r_F_50[l]==2.6:     #if r_F_50[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_50[2] += F_50[l]
    F_plot_err_50[2] += U_F_50[l]

 if r_F_50[l]==3.1: #if r_F_50[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_50[3] += F_50[l]
    F_plot_err_50[3] += U_F_50[l]

 if r_F_50[l]==3.7: #if r_F_50[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_50[4] += F_50[l]
    F_plot_err_50[4] += U_F_50[l]

 if r_F_50[l]==5: #if r_F_50[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_50[5] += F_50[l]
    F_plot_err_50[5] += U_F_50[l]

 if r_F_50[l]==6.1: #if r_F_50[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_50[6] += F_50[l]
    F_plot_err_50[6] += U_F_50[l]


print r_plot
print F_plot_50
print F_plot_err_50

plt.errorbar(r_50_plot,F_plot_50,yerr=F_plot_err_50, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_50, ref_F_50,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlim([0,7])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 50$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_50_plot.eps')
plt.show()


#************ theta = 0 ******************
r_60_plot = [0.2,0.9,1.7,2.7,3.4,4,5]
for l in ref_file_F_60:
    row = l.split()

    ref_r_F_60.append(float(row[0])) #/10 to get to cm
    ref_F_60.append(float(row[1]))

for l in file_F_60:
    row = l.split()

    r_F_60.append(float(row[0])) #/10 to get to cm
    F_60.append(float(row[1]))
    U_F_60.append(float(row[2]))

F_plot_60 = [0.]*7
F_plot_err_60 = [0.]*7

for l in range(len(F_60)):

 if r_F_60[l]==0.2: #if r_F_60[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_60[0] += F_60[l]
    F_plot_err_60[0] += U_F_60[l]

 if r_F_60[l]==0.9:   #if r_F_60[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_60[1] += F_60[l]
    F_plot_err_60[1] += U_F_60[l]

 if r_F_60[l]==1.7:     #if r_F_60[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_60[2] += F_60[l]
    F_plot_err_60[2] += U_F_60[l]

 if r_F_60[l]==2.7: #if r_F_60[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_60[3] += F_60[l]
    F_plot_err_60[3] += U_F_60[l]

 if r_F_60[l]==3.4: #if r_F_60[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_60[4] += F_60[l]
    F_plot_err_60[4] += U_F_60[l]

 if r_F_60[l]==4: #if r_F_60[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_60[5] += F_60[l]
    F_plot_err_60[5] += U_F_60[l]

 if r_F_60[l]==5: #if r_F_60[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_60[6] += F_60[l]
    F_plot_err_60[6] += U_F_60[l]
print r_plot
print F_plot_60
print F_plot_err_60

plt.errorbar(r_60_plot,F_plot_60,yerr=F_plot_err_60, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_60, ref_F_60,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlim([0,7])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 60$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_60_plot.eps')
plt.show()


#************ theta = 0 ******************
r_70_plot = [0.8,1.1,1.4,2.2,3.9,4.1,5]
for l in ref_file_F_70:
    row = l.split()

    ref_r_F_70.append(float(row[0])) #/10 to get to cm
    ref_F_70.append(float(row[1]))

for l in file_F_70:
    row = l.split()

    r_F_70.append(float(row[0])) #/10 to get to cm
    F_70.append(float(row[1]))
    U_F_70.append(float(row[2]))

F_plot_70 = [0.]*7
F_plot_err_70 = [0.]*7

for l in range(len(F_70)):

 if r_F_70[l]==0.8: #if r_F_70[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_70[0] += F_70[l]
    F_plot_err_70[0] += U_F_70[l]

 if r_F_70[l]==1.1:   #if r_F_70[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_70[1] += F_70[l]
    F_plot_err_70[1] += U_F_70[l]

 if r_F_70[l]==1.4:     #if r_F_70[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_70[2] += F_70[l]
    F_plot_err_70[2] += U_F_70[l]

 if r_F_70[l]==2.2: #if r_F_70[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_70[3] += F_70[l]
    F_plot_err_70[3] += U_F_70[l]

 if r_F_70[l]==3.9: #if r_F_70[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_70[4] += F_70[l]
    F_plot_err_70[4] += U_F_70[l]

 if r_F_70[l]==4.1: #if r_F_70[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_70[5] += F_70[l]
    F_plot_err_70[5] += U_F_70[l]

 if r_F_70[l]==5: #if r_F_70[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_70[6] += F_70[l]
    F_plot_err_70[6] += U_F_70[l]

print r_plot
print F_plot_70
print F_plot_err_70

plt.errorbar(r_70_plot,F_plot_70,yerr=F_plot_err_70, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_70, ref_F_70,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.xlim([0,7])
plt.text(1, 1.75, r'$\theta = 70$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_70_plot.eps')
plt.show()


#************ theta = 0 ******************
r_80_plot = [0.7,1,1.2,1.8,2.2,2.5,3.3,4.1,5.1,6]

for l in ref_file_F_80:
    row = l.split()

    ref_r_F_80.append(float(row[0])) #/10 to get to cm
    ref_F_80.append(float(row[1]))

for l in file_F_80:
    row = l.split()

    r_F_80.append(float(row[0])) #/10 to get to cm
    F_80.append(float(row[1]))
    U_F_80.append(float(row[2]))

F_plot_80 = [0.]*10
F_plot_err_80 = [0.]*10

for l in range(len(F_80)):

 if r_F_80[l]==0.7: #if r_F_80[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_80[0] += F_80[l]
    F_plot_err_80[0] += U_F_80[l]

 if r_F_80[l]==1:   #if r_F_80[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_80[1] += F_80[l]
    F_plot_err_80[1] += U_F_80[l]

 if r_F_80[l]==1.2:     #if r_F_80[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_80[2] += F_80[l]
    F_plot_err_80[2] += U_F_80[l]

 if r_F_80[l]==1.8: #if r_F_80[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_80[3] += F_80[l]
    F_plot_err_80[3] += U_F_80[l]

 if r_F_80[l]==2.2: #if r_F_80[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_80[4] += F_80[l]
    F_plot_err_80[4] += U_F_80[l]

 if r_F_80[l]==2.5: #if r_F_80[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_80[5] += F_80[l]
    F_plot_err_80[5] += U_F_80[l]

 if r_F_80[l]==3.3: #if r_F_80[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_80[6] += F_80[l]
    F_plot_err_80[6] += U_F_80[l]

 if r_F_80[l]==4.1: #if r_F_80[l]>=3.5 and r_F[l]<4.5: #4
    F_plot_80[7] += F_80[l]
    F_plot_err_80[7] += U_F_80[l]


 if r_F_80[l]==5.1: #if r_F_80[l]>=4.5 and r_F[l]<5.5: #5
    F_plot_80[8] += F_80[l]
    F_plot_err_80[8] += U_F_80[l]

 if r_F_80[l]==6: #if r_F_80[l]>=5.5 and r_F[l]<6.5: #6
    F_plot_80[9] += F_80[l]
    F_plot_err_80[9] += U_F_80[l]

print r_plot
print F_plot_80
print F_plot_err_80

plt.errorbar(r_80_plot,F_plot_80,yerr=F_plot_err_80, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_80, ref_F_80,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.xlim([0,7])
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 80$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_80_plot.eps')
plt.show()


#************ theta = 90 ******************
r_90_plot = [0.4,0.5,0.7,1,1.5,2,3,4,5,6]
for l in ref_file_F_90:
    row = l.split()

    ref_r_F_90.append(float(row[0])) #/10 to get to cm
    ref_F_90.append(float(row[1]))

for l in file_F_90:
    row = l.split()

    r_F_90.append(float(row[0])) #/10 to get to cm
    F_90.append(float(row[1]))
    U_F_90.append(float(row[2]))

F_plot_90 = [0.]*10
F_plot_err_90 = [0.]*10

for l in range(len(F_90)):

 if r_F_90[l]==0.4: #if r_F_90[l]>=0 and r_F[l]<0.375: #0.45
    F_plot_90[0] += F_90[l]
    F_plot_err_90[0] += U_F_90[l]

 if r_F_90[l]==0.5:   #if r_F_90[l]>=0.375 and r_F[l]<0.625: #0.5
    F_plot_90[1] += F_90[l]
    F_plot_err_90[1] += U_F_90[l]

 if r_F_90[l]==0.7:     #if r_F_90[l]>=0.625 and r_F[l]<0.875: #0.75
    F_plot_90[2] += F_90[l]
    F_plot_err_90[2] += U_F_90[l]

 if r_F_90[l]==1: #if r_F_90[l]>=0.875 and r_F[l]<1.25: #1
    F_plot_90[3] += F_90[l]
    F_plot_err_90[3] += U_F_90[l]

 if r_F_90[l]==1.5: #if r_F_90[l]>=1.25 and r_F[l]<1.75: #1.5
    F_plot_90[4] += F_90[l]
    F_plot_err_90[4] += U_F_90[l]

 if r_F_90[l]==2: #if r_F_90[l]>=1.75 and r_F[l]<2.5: #2
    F_plot_90[5] += F_90[l]
    F_plot_err_90[5] += U_F_90[l]

 if r_F_90[l]==3: #if r_F_90[l]>=2.5 and r_F[l]<3.5: #3
    F_plot_90[6] += F_90[l]
    F_plot_err_90[6] += U_F_90[l]

 if r_F_90[l]==4.1: #if r_F_90[l]>=3.5 and r_F[l]<4.5: #4
    F_plot_90[7] += F_90[l]
    F_plot_err_90[7] += U_F_90[l]


 if r_F_90[l]==5: #if r_F_90[l]>=4.5 and r_F[l]<5.5: #5
    F_plot_90[8] += F_90[l]
    F_plot_err_90[8] += U_F_90[l]

 if r_F_90[l]==6.1: #if r_F_90[l]>=5.5 and r_F[l]<6.5: #6
    F_plot_90[9] += F_90[l]
    F_plot_err_90[9] += U_F_90[l]

print len(r_90_plot)
print len(F_plot_90)
print len(F_plot_err_90)

plt.errorbar(r_90_plot,F_plot_90,yerr=F_plot_err_90, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_90, ref_F_90,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.xlim([0,7])
plt.ylim([0,2])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 1.75, r'$\theta = 90$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_90_plot.eps')
plt.show()

