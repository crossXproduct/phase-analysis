import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import textwrap
#import Dans_Diffraction as dif
import tools.Dans_Diffraction.Dans_Diffraction as dif

# Take user input
cif = np.genfromtxt("cifs.txt",dtype=str, unpack=True,comments='#') #COD numbers of CIF files to be compared
#TODO: add and read second, third columns as relative scales, x-shifts
data = input("Data file (without extension): ") #Path to user data
background = np.float64(input("Constant background (data-cif): ")) #Subtract a constant background correction
scalefactor = int(input("Scale factor (cif/data): ")) #Relative multiplicative scale correction between CIF and user data intensities
twotheta_max = np.float64(input("Maximum 2theta: ")) #Maximum 2theta value to plot

# Extract and plot data
twotheta,intensity = np.genfromtxt(data+".xy",unpack=True,skip_header=0,usecols=[0,1],dtype=np.double)
intensity = scalefactor*(intensity-background) #Implement scale and background corrections

xtl = []
fig, ax = plt.subplots()

ncifs = cif.size
for n in range(ncifs):
    if ncifs > 1: xtl.append(dif.Crystal(cif[n]+".cif"))
    else: xtl.append(dif.Crystal(str(cif)+".cif"))
    xtl[n].Plot.simulate_powder(ax=ax)
    ax.lines[-1].set_color(str(list(mcolors.BASE_COLORS)[n+3])) #Set different colors for different files
    if ncifs > 1: ax.lines[-1].set_label(cif[n]) #Set labels for plot legend
    else: ax.lines[-1].set_label(str(cif))

# Plot data and set plot parameters
plt.plot(twotheta,intensity,color='black',linewidth=3,label=textwrap.fill(data,width=25,break_long_words=True))
plt.xlim(min(twotheta),twotheta_max)
plt.ylim(0,max(intensity,))
plt.legend()
plt.savefig(data+"_"+str(cif)+".png")