import pylab
import matplotlib.pyplot as plt

file_norm = open("Normalised_values.txt", "r")
file_GL = open("GL_values.txt", "r")

for l in file_norm:
    row = l.split()
    if str(row[0]) == "Dr0theta0":
        Dr0theta0 = float(row[1])
    elif str(row[0] == "GLr0theta0":
        GLr0theta0 = float(row[1])
    elif str(row[0]) == "Sk":
        Sk = float(row[1])
    elif str(row[0] == "Lambda":
        Lambda == float(row[1]
    else:
        print "problem assigning norm values 
