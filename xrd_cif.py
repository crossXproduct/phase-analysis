import numpy as np
import matplotlib.pyplot as plt
import Dans_Diffraction as dif

cif = input("CIF file number: ")
data = input("Data file (without extension): ")
scalefactor = int(input("Scale factor (cif/data): "))

twotheta,intensity = np.genfromtxt(data+".xy",unpack=True,skip_header=0,usecols=[0,1],dtype=np.double)

xtl = dif.Crystal(cif+".cif")
xtl.Plot.simulate_powder()
#for txt in plt.gcf().texts:
#    txt.set_visible(False)
plt.plot(twotheta,intensity*scalefactor,color='limegreen',linewidth=3)
plt.savefig(cif+".png")