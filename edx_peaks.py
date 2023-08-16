import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

#input
filename = input("filename: ")
kev_range = np.float64(input("max keV: "))
n_peaks = int(input("number of peaks to save: "))
peak_h = np.float64(input("peak height minimum (keV): "))
kev,counts = np.loadtxt(filename,comments='#',delimiter=",",unpack=True,usecols=[0,1],dtype=np.double)
#switch to index units
kev_range = round(kev_range*len(kev)/max(kev))
peak_w = round(0.001*len(kev)/max(kev))
peak_spacing = round(0.2*len(kev)/max(kev))

#find peaks
max_index = find_peaks(counts,threshold=1,height=peak_h,width=peak_w,distance=peak_spacing)[0] #get indices of local maxima in counts
n_max = len(max_index)
#sort peak points in order of ascending counts (numpy doesn't allow descending sorts...’\_(~)_/`)
sort_index = np.argsort(counts[max_index])
peaks_x = kev[max_index]
peaks_x = peaks_x[sort_index]
peaks_y = counts[max_index][sort_index]
peaks_sorted = np.column_stack([peaks_x[n_max-n_peaks-1:n_max],peaks_y[n_max-n_peaks-1:n_max]])
#save highest [n_peaks] peaks to file
f = open(filename+"_peaks.txt","w")
f.write("kev counts\n"+str(peaks_sorted))

#plot
p1 = plt.stairs(counts[0:kev_range-2],kev[0:kev_range-1]) #full dataset
for i in range(n_peaks): #n_peaks peaks (https://stackoverflow.com/questions/14432557/scatter-plot-with-different-text-at-each-data-point)
    if n_peaks-i+1 > len(peaks_sorted):
        print("peak "+str(i)+" is out of range")
        continue
    plt.annotate(str(i+1),(peaks_sorted[n_peaks-i][0],peaks_sorted[n_peaks-i][1]))
#plot labels
plt.title("EDX elemental decomposition")
plt.xlabel("keV")
plt.ylabel("counts")
#save fig
plt.savefig(filename+"_peaks.png")
plt.clf()
