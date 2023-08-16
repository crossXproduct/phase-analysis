import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True

#input
filename = input("filename: ")
subtract = input("file to subtract: ")
xaxis = input("q or theta? (q\\t) ")

xstart = float(input("x min: "))
xend = float(input("x max: "))
xname = ""
skip = 0
if xaxis == 'q': #initialize params based on datatype
    skip = 5
    xname = "q"
else:
    xname = r'2$\theta$'
    
#load data into arrays and plot
q,intensity = np.genfromtxt(filename,unpack=True,skip_header=5,comments="<",usecols=[0,1],dtype=np.double)
if subtract=="": #if not subtracting, plot the data loaded above
    plt.plot(q,intensity)
else: #if subtracting, load second dataset and plot the difference
    q1,intensity1 = np.genfromtxt(subtract,unpack=True,skip_header=5,comments="<",usecols=[0,1],dtype=np.double)
    qrange = min(len(intensity1),len(intensity))
    plt.plot(q[0:qrange],intensity[0:qrange]-intensity1[0:qrange])

#set plot parameters
plt.xlim(xstart,max(q))
plt.xscale("log")
plt.yscale("log")
plt.title('S('+xname+')')
plt.xlabel(xname)
plt.ylabel("intensity")

#save image file
if subtract=="": 
    plt.savefig(filename+".png")
else: plt.savefig(filename+"-"+subtract+".png")
plt.clf()