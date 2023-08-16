#convert q/I data to 2theta/I

import numpy as np
#import matplotlib.pyplot as plt

#name file
filename = input("filename: ")
wavelength = 0.1542 #np.double(input("wavelength: "))
#print(subtract)
#loadtxt columns into np arrays and skip header
q,intensity = np.genfromtxt(filename,unpack=True,skip_header=5,comments="<",usecols=[0,1],dtype=np.double)
#print(q)

twotheta = 2*np.arcsin(q*wavelength/(4*np.pi))*180/np.pi
#print(twotheta)
#print(intensity)
converted = open(str(filename)+"_2theta","w")
for i in range(0,len(twotheta)-1):
    converted.write(str(twotheta[i])+" "+str(intensity[i])+"\n")
    #print(i)
converted.close()