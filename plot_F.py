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

#************ theta = 0 ******************
for l in file_F_0:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_F_0.append(float(row[0])) #/10 to get to cm
    F_0.append(float(row[1]))
    U_F_0.append(float(row[2]))

F_rounded_0 = [0.]*11
F_rounded_err_0 = [0.]*11
bins_0 = [0.]*11

for s in range(len(r_F_0)):

  nint = int(round(r_F_0[s]))
  if F_0[s]>0:
    F_rounded_0[nint] += float(F_0[s])
    F_rounded_err_0[nint] += float(U_F_0[s])
    bins_0[nint] += float(1)

F_plot_0 = [0.]*11
F_plot_err_0 = [0.]*11

r_0 = [i for i in range(len(F_rounded_0))]
for m in range(len(F_rounded_0)):
  F_plot_0[m] = F_rounded_0[m]/bins_0[m]
  F_plot_err_0[m] = F_rounded_err_0[m]/bins_0[m]
  r_0[m] = float(r_0[m])

for l in ref_file_F_0:
    row = l.split()

    ref_r_F_0.append(float(row[0])) #/10 to get to cm
    ref_F_0.append(float(row[1]))

#print r_0
#print F_plot_0
#print F_plot_err

plt.errorbar(r_0,F_plot_0,yerr=F_plot_err_0, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_0, ref_F_0,color='black', marker='o', label='Ref. Data',linestyle='dashed')
plt.legend()
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 3, r'$\theta = 0$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_0_plot.eps')
plt.show()


#************ theta = 10 ******************
for l in file_F_10:
    row = l.split()

    r_F_10.append(float(row[0])) #/10 to get to cm
    F_10.append(float(row[1]))
    U_F_10.append(float(row[2]))

F_rounded_10 = [0.]*11
F_rounded_err_10 = [0.]*11
bins_10 = [0.]*11

for s in range(len(r_F_10)):

  nint = int(round(r_F_10[s]))
  if F_10[s]>0:
    F_rounded_10[nint] += float(F_10[s])
    F_rounded_err_10[nint] += float(U_F_10[s])
    bins_10[nint] += float(1)

F_plot_10 = [0.]*11
F_plot_err_10 = [0.]*11

r_10 = [i for i in range(len(F_rounded_10))]
for m in range(len(F_rounded_10)):
 if bins_10[m]>0:
  F_plot_10[m] = F_rounded_10[m]/bins_10[m]
  F_plot_err_10[m] = F_rounded_err_10[m]/bins_10[m]
 else:
  F_plot_10[m] = 0
  F_plot_err_10[m] = 0
  r_10[m] = float(r_10[m])
 
for l in ref_file_F_10:
    row = l.split()

    ref_r_F_10.append(float(row[0])) #/10 to get to cm
    ref_F_10.append(float(row[1]))


#print F_plot_10
plt.errorbar(r_10,F_plot_10,yerr=F_plot_err_10, label='Geant4',color='red', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_10, ref_F_10,color='black',label='Ref. Data', marker='o', linestyle='dashed')
plt.legend()
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.ylim([0,3.5])
plt.text(1, 3, r'$\theta = 10$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_10_plot.eps')
plt.show()


#************ theta = 20 ******************
for l in file_F_20:
    row = l.split()

    r_F_20.append(float(row[0])) #/10 to get to cm
    F_20.append(float(row[1]))
    U_F_20.append(float(row[2]))

F_rounded_20 = [0.]*11
F_rounded_err_20 = [0.]*11
bins_20 = [0.]*11

for s in range(len(r_F_20)):

  nint = int(round(r_F_20[s]))
  if F_20[s]>0:
    F_rounded_20[nint] += float(F_20[s])
    F_rounded_err_20[nint] += float(U_F_20[s])
    bins_20[nint] += float(1)

F_plot_20 = [0.]*11
F_plot_err_20 = [0.]*11

r_20 = [i for i in range(len(F_rounded_20))]
for m in range(len(F_rounded_20)):
  F_plot_20[m] = F_rounded_20[m]/bins_20[m]
  F_plot_err_20[m] = F_rounded_err_20[m]/bins_20[m]
  r_20[m] = float(r_20[m])

for l in ref_file_F_20:
    row = l.split()

    ref_r_F_20.append(float(row[0])) #/10 to get to cm
    ref_F_20.append(float(row[1]))


#print F_plot_20
plt.errorbar(r_20,F_plot_20,yerr=F_plot_err_20, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_20, ref_F_20,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 20$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_20_plot.eps')
plt.show()


#************ theta = 30 ******************
for l in file_F_30:
    row = l.split()

    r_F_30.append(float(row[0])) #/10 to get to cm
    F_30.append(float(row[1]))
    U_F_30.append(float(row[2]))

F_rounded_30 = [0.]*11
F_rounded_err_30 = [0.]*11
bins_30 = [0.]*11

for s in range(len(r_F_30)):

  nint = int(round(r_F_30[s]))
  if F_30[s]>0:
    F_rounded_30[nint] += float(F_30[s])
    F_rounded_err_30[nint] += float(U_F_30[s])
    bins_30[nint] += float(1)

F_plot_30 = [0.]*11
F_plot_err_30 = [0.]*11

r_30 = [i for i in range(len(F_rounded_30))]
for m in range(len(F_rounded_30)):
  F_plot_30[m] = F_rounded_30[m]/bins_30[m]
  F_plot_err_30[m] = F_rounded_err_30[m]/bins_30[m]
  r_30[m] = float(r_30[m])

for l in ref_file_F_30:
    row = l.split()

    ref_r_F_30.append(float(row[0])) #/10 to get to cm
    ref_F_30.append(float(row[1]))


#print F_plot_30
plt.errorbar(r_30,F_plot_30,yerr=F_plot_err_30, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_30, ref_F_30,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 30$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_30_plot.eps')
plt.show()


#************ theta = 40 ******************
for l in file_F_40:
    row = l.split()

    r_F_40.append(float(row[0])) #/10 to get to cm
    F_40.append(float(row[1]))
    U_F_40.append(float(row[2]))

F_rounded_40 = [0.]*11
F_rounded_err_40 = [0.]*11
bins_40 = [0.]*11

for s in range(len(r_F_40)):

  nint = int(round(r_F_40[s]))
  if F_40[s]>0:
    F_rounded_40[nint] += float(F_40[s])
    F_rounded_err_40[nint] += float(U_F_40[s])
    bins_40[nint] += float(1)

F_plot_40 = [0.]*11
F_plot_err_40 = [0.]*11

r_40 = [i for i in range(len(F_rounded_40))]
for m in range(len(F_rounded_40)):
  F_plot_40[m] = F_rounded_40[m]/bins_40[m]
  F_plot_err_40[m] = F_rounded_err_40[m]/bins_40[m]
  r_40[m] = float(r_40[m])

for l in ref_file_F_40:
    row = l.split()

    ref_r_F_40.append(float(row[0])) #/10 to get to cm
    ref_F_40.append(float(row[1]))


#print F_plot_40
plt.errorbar(r_40,F_plot_40,yerr=F_plot_err_40, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_40, ref_F_40,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.legend()
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 3, r'$\theta = 40$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_40_plot.eps')
plt.show()



#************ theta = 50 ******************
for l in file_F_50:
    row = l.split()

    r_F_50.append(float(row[0])) #/10 to get to cm
    F_50.append(float(row[1]))
    U_F_50.append(float(row[2]))

F_rounded_50 = [0.]*11
F_rounded_err_50 = [0.]*11
bins_50 = [0.]*11

for s in range(len(r_F_50)):

  nint = int(round(r_F_50[s]))
  if F_50[s]>0:
    F_rounded_50[nint] += float(F_50[s])
    F_rounded_err_50[nint] += float(U_F_50[s])
    bins_50[nint] += float(1)

F_plot_50 = [0.]*11
F_plot_err_50 = [0.]*11

r_50 = [i for i in range(len(F_rounded_50))]
for m in range(len(F_rounded_50)):
  F_plot_50[m] = F_rounded_50[m]/bins_50[m]
  F_plot_err_50[m] = F_rounded_err_50[m]/bins_50[m]
  r_50[m] = float(r_50[m])

for l in ref_file_F_50:
    row = l.split()

    ref_r_F_50.append(float(row[0])) #/10 to get to cm
    ref_F_50.append(float(row[1]))


#print F_plot_50
plt.errorbar(r_50,F_plot_50,yerr=F_plot_err_50, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_50, ref_F_50,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 50$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_50_plot.eps')
plt.show()


#************ theta = 60 ******************
for l in file_F_60:
    row = l.split()

    r_F_60.append(float(row[0])) #/10 to get to cm
    F_60.append(float(row[1]))
    U_F_60.append(float(row[2]))

F_rounded_60 = [0.]*11
F_rounded_err_60 = [0.]*11
bins_60 = [0.]*11

for s in range(len(r_F_60)):

  nint = int(round(r_F_60[s]))
  if F_60[s]>0:
    F_rounded_60[nint] += float(F_60[s])
    F_rounded_err_60[nint] += float(U_F_60[s])
    bins_60[nint] += float(1)

F_plot_60 = [0.]*11
F_plot_err_60 = [0.]*11

r_60 = [i for i in range(len(F_rounded_60))]
for m in range(len(F_rounded_60)):
  F_plot_60[m] = F_rounded_60[m]/bins_60[m]
  F_plot_err_60[m] = F_rounded_err_60[m]/bins_60[m]
  r_60[m] = float(r_60[m])

for l in ref_file_F_60:
    row = l.split()

    ref_r_F_60.append(float(row[0])) #/10 to get to cm
    ref_F_60.append(float(row[1]))


#print F_plot_60
plt.errorbar(r_60,F_plot_60,yerr=F_plot_err_60, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_60, ref_F_60,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 60$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_60_plot.eps')
plt.show()


#************ theta = 70 ******************
for l in file_F_70:
    row = l.split()

    r_F_70.append(float(row[0])) #/10 to get to cm
    F_70.append(float(row[1]))
    U_F_70.append(float(row[2]))

F_rounded_70 = [0.]*11
F_rounded_err_70 = [0.]*11
bins_70 = [0.]*11

for s in range(len(r_F_70)):

  nint = int(round(r_F_70[s]))
  if F_70[s]>0:
    F_rounded_70[nint] += float(F_70[s])
    F_rounded_err_70[nint] += float(U_F_70[s])
    bins_70[nint] += float(1)

F_plot_70 = [0.]*11
F_plot_err_70 = [0.]*11

r_70 = [i for i in range(len(F_rounded_70))]
for m in range(len(F_rounded_70)):
  F_plot_70[m] = F_rounded_70[m]/bins_70[m]
  F_plot_err_70[m] = F_rounded_err_70[m]/bins_70[m]
  r_70[m] = float(r_70[m])

for l in ref_file_F_70:
    row = l.split()

    ref_r_F_70.append(float(row[0])) #/10 to get to cm
    ref_F_70.append(float(row[1]))


#print F_plot_70
plt.errorbar(r_70,F_plot_70,yerr=F_plot_err_70, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_70, ref_F_70,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.legend()
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.text(1, 3, r'$\theta = 70$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_70_plot.eps')
plt.show()


#************ theta = 80 ******************
for l in file_F_80:
    row = l.split()

    r_F_80.append(float(row[0])) #/10 to get to cm
    F_80.append(float(row[1]))
    U_F_80.append(float(row[2]))

F_rounded_80 = [0.]*11
F_rounded_err_80 = [0.]*11
bins_80 = [0.]*11

for s in range(len(r_F_80)):

  nint = int(round(r_F_80[s]))
  if F_80[s]>0:
    F_rounded_80[nint] += float(F_80[s])
    F_rounded_err_80[nint] += float(U_F_80[s])
    bins_80[nint] += float(1)

F_plot_80 = [0.]*11
F_plot_err_80 = [0.]*11

r_80 = [i for i in range(len(F_rounded_80))]
for m in range(len(F_rounded_80)):
 if bins_80[m]>0:
  F_plot_80[m] = F_rounded_80[m]/bins_80[m]
  F_plot_err_80[m] = F_rounded_err_80[m]/bins_80[m]
 else:
  F_plot_80[m] = 0
  F_plot_err_80[m] = 0
  r_80[m] = float(r_80[m])

for l in ref_file_F_80:
    row = l.split()

    ref_r_F_80.append(float(row[0])) #/10 to get to cm
    ref_F_80.append(float(row[1]))


#print F_plot_80
plt.errorbar(r_80,F_plot_80,yerr=F_plot_err_80, color='red', label='Geant4',ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_80, ref_F_80,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 80$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_80_plot.eps')
plt.show()


#************ theta = 90 ******************
for l in file_F_90:
    row = l.split()

    r_F_90.append(float(row[0])) #/10 to get to cm
    F_90.append(float(row[1]))
    U_F_90.append(float(row[2]))

F_rounded_90 = [0.]*11
F_rounded_err_90 = [0.]*11
bins_90 = [0.]*11

for s in range(len(r_F_90)):

  nint = int(round(r_F_90[s]))
  if F_90[s]>0:
    F_rounded_90[nint] += float(F_90[s])
    F_rounded_err_90[nint] += float(U_F_90[s])
    bins_90[nint] += float(1)

F_plot_90 = [0.]*11
F_plot_err_90 = [0.]*11

r_90 = [i for i in range(len(F_rounded_90))]
for m in range(len(F_rounded_90)):
  F_plot_90[m] = F_rounded_90[m]/bins_90[m]
  F_plot_err_90[m] = F_rounded_err_90[m]/bins_90[m]
  r_90[m] = float(r_90[m])

for l in ref_file_F_90:
    row = l.split()

    ref_r_F_90.append(float(row[0])) #/10 to get to cm
    ref_F_90.append(float(row[1]))


#print F_plot_90
plt.errorbar(r_90,F_plot_90,yerr=F_plot_err_90, color='red',label='Geant4', ls='--', marker='o', capsize=5, capthick=1, ecolor='red')
plt.plot(ref_r_F_90, ref_F_90,color='black',label='Ref. Data', marker='o', linestyle='dashed')
#plt.xlim([0.4,10])
plt.ylim([0,3.5])
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$F(r,\theta)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.legend()
plt.text(1, 3, r'$\theta = 90$', family='sans-serif', fontsize=18, fontweight='heavy')
plt.savefig('F_theta_90_plot.eps')
plt.show()
