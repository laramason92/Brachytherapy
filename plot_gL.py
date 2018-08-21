from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

file_gL = open("gL_r.txt", "r")
ref1_file_gL = open("ref_gL_Alcalde.txt", "r")
ref2_file_gL = open("ref_gL_estro8.txt", "r")

r_gL = []
gL = []
U_gL = []

ref1_r_gL = []
ref1_gL = []

ref2_r_gL = []
ref2_gL = []

for l in file_gL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_gL.append(float(row[0]))
    gL.append(float(row[1]))
    U_gL.append(float(row[2]))

for l in ref1_file_gL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    ref1_r_gL.append(float(row[0]))
    ref1_gL.append(float(row[1]))

for l in ref2_file_gL:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    ref2_r_gL.append(float(row[0]))
    ref2_gL.append(float(row[1]))

#r_plot = [0.25,0.5,0.75,1,1.5,2,3,4,5,6,7,8,9,10]
r_plot = [0.3,1,2,3.5,4,5,6.5,8]
#r_plot = [0.3,1,1.9,3.4,4.1,4.9,6.4,8]
gL_plot = [0.]*8
bins = [0.]*8
unc_plot = [0.]*8

for l in range(len(gL)):

 if r_gL[l]==0.3: #if r_gL[l]>=0 and r_gL[l]<0.375: #0.25
    gL_plot[0] += gL[l]
    bins[0] += 1
    unc_plot[0] += U_gL[l]

 if r_gL[l]==1:   #if r_gL[l]>=0.375 and r_gL[l]<0.625: #0.5
    gL_plot[1] += gL[l]
    bins[1] += 1
    unc_plot[1] += U_gL[l]

 if r_gL[l]==1.9:     #if r_gL[l]>=0.625 and r_gL[l]<0.875: #0.75
    gL_plot[2] += gL[l]
    bins[2] += 1
    unc_plot[2] += U_gL[l]

 if r_gL[l]==3.4: #if r_gL[l]>=0.875 and r_gL[l]<1.25: #1
    gL_plot[3] += gL[l]
    bins[3] += 1
    unc_plot[3] += U_gL[l]

 if r_gL[l]==4.1: #if r_gL[l]>=1.25 and r_gL[l]<1.75: #1.5
    gL_plot[4] += gL[l]
    bins[4] += 1
    unc_plot[4] += U_gL[l]

 if r_gL[l]==4.9: #if r_gL[l]>=1.75 and r_gL[l]<2.5: #2
    gL_plot[5] += gL[l]
    bins[5] += 1
    unc_plot[5] += U_gL[l]

 if r_gL[l]==6.4: #if r_gL[l]>=2.5 and r_gL[l]<3.5: #3
    gL_plot[6] += gL[l]
    bins[6] += 1
    unc_plot[6] += U_gL[l]

 if r_gL[l]==8: #if r_gL[l]>=3.5 and r_gL[l]<4.5: #4
    gL_plot[7] += gL[l]
    bins[7] += 1
    unc_plot[7] += U_gL[l]

gL_plot_rounded = [0.]*8
for m in range(len(gL_plot)):
  gL_plot_rounded[m] = gL_plot[m]/bins[m]

print gL_plot_rounded

plt.errorbar(r_plot,gL_plot_rounded, yerr=unc_plot,label='Geant4', color='blue', ls='--', marker='o', capsize=5, capthick=1, ecolor='blue')

plt.plot(ref1_r_gL, ref1_gL,color='red',label='Lopez et al', marker='o', linestyle='dashed')
plt.plot(ref2_r_gL, ref2_gL,color='black',label='Estro 8', marker='o', linestyle='dashed')
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$g(r)$',family='sans-serif', fontsize=18, fontweight='heavy')
plt.ylim(0.5,1.5)
#plt.xlim(0,6)
plt.legend()
plt.savefig('gL_plot.eps')
plt.show()

