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

r_plot = [0.25,0.5,0.75,1,1.5,2,3,4,5,6,7,8,9,10]
gL_plot = [0.]*14
bins = [0.]*14
unc_plot = [0.]*14

for l in range(len(gL)):

 if r_gL[l]>=0 and r_gL[l]<0.375: #0.25
    gL_plot[0] += gL[l]
    bins[0] += 1
    unc_plot[0] += U_gL[l]

 if r_gL[l]>=0.375 and r_gL[l]<0.625: #0.5
    gL_plot[1] += gL[l]
    bins[1] += 1
    unc_plot[1] += U_gL[l]

 if r_gL[l]>=0.625 and r_gL[l]<0.875: #0.75
    gL_plot[2] += gL[l]
    bins[2] += 1
    unc_plot[2] += U_gL[l]

 if r_gL[l]>=0.875 and r_gL[l]<1.25: #1
    gL_plot[3] += gL[l]
    bins[3] += 1
    unc_plot[3] += U_gL[l]

 if r_gL[l]>=1.25 and r_gL[l]<1.75: #1.5
    gL_plot[4] += gL[l]
    bins[4] += 1
    unc_plot[4] += U_gL[l]

 if r_gL[l]>=1.75 and r_gL[l]<2.5: #2
    gL_plot[5] += gL[l]
    bins[5] += 1
    unc_plot[5] += U_gL[l]

 if r_gL[l]>=2.5 and r_gL[l]<3.5: #3
    gL_plot[6] += gL[l]
    bins[6] += 1
    unc_plot[6] += U_gL[l]

 if r_gL[l]>=3.5 and r_gL[l]<4.5: #4
    gL_plot[7] += gL[l]
    bins[7] += 1
    unc_plot[7] += U_gL[l]

 if r_gL[l]>=4.5 and r_gL[l]<5.5: #5
    gL_plot[8] += gL[l]
    bins[8] += 1
    unc_plot[8] += U_gL[l]

 if r_gL[l]>=5.5 and r_gL[l]<6.5: #6
    gL_plot[9] += gL[l]
    bins[9] += 1
    unc_plot[9] += U_gL[l]

 if r_gL[l]>=6.5 and r_gL[l]<7.5: #7
    gL_plot[10] += gL[l]
    bins[10] += 1
    unc_plot[10] += U_gL[l]

 if r_gL[l]>=7.5 and r_gL[l]<8.5: #8
    gL_plot[11] += gL[l]
    bins[11] += 1
    unc_plot[11] += U_gL[l]

 if r_gL[l]>=8.5 and r_gL[l]<9.5: #9
    gL_plot[12] += gL[l]
    bins[12] += 1
    unc_plot[12] += U_gL[l]

 if r_gL[l]>=9.5 and r_gL[l]<10.5: #10
    gL_plot[13] += gL[l]
    bins[13] += 1
    unc_plot[13] += U_gL[l]

gL_plot_rounded = [0.]*14
for m in range(len(gL_plot)):
  gL_plot_rounded[m] = gL_plot[m]/bins[m]

print gL_plot_rounded

plt.errorbar(r_plot,gL_plot_rounded, yerr=unc_plot,label='Geant4', color='blue', ls='--', marker='o', capsize=5, capthick=1, ecolor='blue')

plt.plot(ref1_r_gL, ref1_gL,color='red',label='Lopez et al', marker='o', linestyle='dashed')
plt.plot(ref2_r_gL, ref2_gL,color='black',label='Estro 8', marker='o', linestyle='dashed')
plt.xlabel('r(cm)',family='sans-serif', fontsize=16)
plt.ylabel(r'$g(r)$',family='sans-serif', fontsize=18, fontweight='heavy')

plt.legend()
plt.savefig('gL_plot.eps')
plt.show()

