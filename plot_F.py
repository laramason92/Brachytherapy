from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

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



#************ theta = 0 ******************
for l in file_F_0:
    row = l.split()

    #print float(row[0]), " & " , float(row[1]), " & ", float(row[2]), " & " , float(row[3]), " \\ "

    r_F_0.append(float(row[0])) #/10 to get to cm
    F_0.append(float(row[1]))
    U_F_0.append(float(row[2]))

F_rounded_0 = [0.]*11
bins_0 = [0.]*11

for s in range(len(r_F_0)):

  nint = int(round(r_F_0[s]))
  if F_0[s]>0:
    F_rounded_0[nint] += float(F_0[s])
    bins_0[nint] += float(1)

F_plot_0 = [0.]*11

for m in range(len(F_rounded_0)):
  F_plot_0[m] = F_rounded_0[m]/bins_0[m]

print F_plot_0
plt.plot(F_plot_0)
#plt.show()


#************ theta = 10 ******************
for l in file_F_10:
    row = l.split()

    r_F_10.append(float(row[0])) #/10 to get to cm
    F_10.append(float(row[1]))
    U_F_10.append(float(row[2]))

F_rounded_10 = [0.]*11
bins_10 = [0.]*11

for s in range(len(r_F_10)):

  nint = int(round(r_F_10[s]))
  if F_10[s]>0:
    F_rounded_10[nint] += float(F_10[s])
    bins_10[nint] += float(1)

F_plot_10 = [0.]*11

for m in range(len(F_rounded_10)):
  F_plot_10[m] = F_rounded_10[m]/bins_10[m]

print F_plot_10
plt.plot(F_plot_10)
#plt.show()


#************ theta = 20 ******************
for l in file_F_20:
    row = l.split()

    r_F_20.append(float(row[0])) #/10 to get to cm
    F_20.append(float(row[1]))
    U_F_20.append(float(row[2]))

F_rounded_20 = [0.]*11
bins_20 = [0.]*11

for s in range(len(r_F_20)):

  nint = int(round(r_F_20[s]))
  if F_20[s]>0:
    F_rounded_20[nint] += float(F_20[s])
    bins_20[nint] += float(1)

F_plot_20 = [0.]*11

for m in range(len(F_rounded_20)):
  F_plot_20[m] = F_rounded_20[m]/bins_20[m]

print F_plot_20
plt.plot(F_plot_20)
#plt.show()


#************ theta = 30 ******************
for l in file_F_30:
    row = l.split()

    r_F_30.append(float(row[0])) #/10 to get to cm
    F_30.append(float(row[1]))
    U_F_30.append(float(row[2]))

F_rounded_30 = [0.]*11
bins_30 = [0.]*11

for s in range(len(r_F_30)):

  nint = int(round(r_F_30[s]))
  if F_30[s]>0:
    F_rounded_30[nint] += float(F_30[s])
    bins_30[nint] += float(1)

F_plot_30 = [0.]*11

for m in range(len(F_rounded_30)):
  F_plot_30[m] = F_rounded_30[m]/bins_30[m]

print F_plot_30
plt.plot(F_plot_30)
#plt.show()


#************ theta = 40 ******************
for l in file_F_40:
    row = l.split()

    r_F_40.append(float(row[0])) #/10 to get to cm
    F_40.append(float(row[1]))
    U_F_40.append(float(row[2]))

F_rounded_40 = [0.]*11
bins_40 = [0.]*11

for s in range(len(r_F_40)):

  nint = int(round(r_F_40[s]))
  if F_40[s]>0:
    F_rounded_40[nint] += float(F_40[s])
    bins_40[nint] += float(1)

F_plot_40 = [0.]*11

for m in range(len(F_rounded_40)):
  F_plot_40[m] = F_rounded_40[m]/bins_40[m]

print F_plot_40
plt.plot(F_plot_40)
#plt.show()



#************ theta = 50 ******************
for l in file_F_50:
    row = l.split()

    r_F_50.append(float(row[0])) #/10 to get to cm
    F_50.append(float(row[1]))
    U_F_50.append(float(row[2]))

F_rounded_50 = [0.]*11
bins_50 = [0.]*11

for s in range(len(r_F_50)):

  nint = int(round(r_F_50[s]))
  if F_50[s]>0:
    F_rounded_50[nint] += float(F_50[s])
    bins_50[nint] += float(1)

F_plot_50 = [0.]*11

for m in range(len(F_rounded_50)):
  F_plot_50[m] = F_rounded_50[m]/bins_50[m]

print F_plot_50
plt.plot(F_plot_50)
#plt.show()


#************ theta = 60 ******************
for l in file_F_60:
    row = l.split()

    r_F_60.append(float(row[0])) #/10 to get to cm
    F_60.append(float(row[1]))
    U_F_60.append(float(row[2]))

F_rounded_60 = [0.]*11
bins_60 = [0.]*11

for s in range(len(r_F_60)):

  nint = int(round(r_F_60[s]))
  if F_60[s]>0:
    F_rounded_60[nint] += float(F_60[s])
    bins_60[nint] += float(1)

F_plot_60 = [0.]*11

for m in range(len(F_rounded_60)):
  F_plot_60[m] = F_rounded_60[m]/bins_60[m]

print F_plot_60
plt.plot(F_plot_60)
#plt.show()


#************ theta = 70 ******************
for l in file_F_70:
    row = l.split()

    r_F_70.append(float(row[0])) #/10 to get to cm
    F_70.append(float(row[1]))
    U_F_70.append(float(row[2]))

F_rounded_70 = [0.]*11
bins_70 = [0.]*11

for s in range(len(r_F_70)):

  nint = int(round(r_F_70[s]))
  if F_70[s]>0:
    F_rounded_70[nint] += float(F_70[s])
    bins_70[nint] += float(1)

F_plot_70 = [0.]*11

for m in range(len(F_rounded_70)):
  F_plot_70[m] = F_rounded_70[m]/bins_70[m]

print F_plot_70
plt.plot(F_plot_70)
#plt.show()


#************ theta = 80 ******************
for l in file_F_80:
    row = l.split()

    r_F_80.append(float(row[0])) #/10 to get to cm
    F_80.append(float(row[1]))
    U_F_80.append(float(row[2]))

F_rounded_80 = [0.]*11
bins_80 = [0.]*11

for s in range(len(r_F_80)):

  nint = int(round(r_F_80[s]))
  if F_80[s]>0:
    F_rounded_80[nint] += float(F_80[s])
    bins_80[nint] += float(1)

F_plot_80 = [0.]*11

for m in range(len(F_rounded_80)):
  F_plot_80[m] = F_rounded_80[m]/bins_80[m]

print F_plot_80
plt.plot(F_plot_80)
#plt.show()


#************ theta = 90 ******************
for l in file_F_90:
    row = l.split()

    r_F_90.append(float(row[0])) #/10 to get to cm
    F_90.append(float(row[1]))
    U_F_90.append(float(row[2]))

F_rounded_90 = [0.]*11
bins_90 = [0.]*11

for s in range(len(r_F_90)):

  nint = int(round(r_F_90[s]))
  if F_90[s]>0:
    F_rounded_90[nint] += float(F_90[s])
    bins_90[nint] += float(1)

F_plot_90 = [0.]*11

for m in range(len(F_rounded_90)):
  F_plot_90[m] = F_rounded_90[m]/bins_90[m]

print F_plot_90
plt.plot(F_plot_90)
#plt.show()
