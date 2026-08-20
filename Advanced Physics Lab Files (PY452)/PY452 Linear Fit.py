import numpy as np
import matplotlib.pyplot as plt

#Change location/filename as necessary
location = ""
file = "Film\\Region 2\\correlations\\"
name = "PolFilm_1um_R2cor"



#Unpacks all of the data from the graphs
dist = np.loadtxt(location + file + name +".txt", usecols=0, skiprows = 1)
cor = np.loadtxt(location + file + name +".txt", usecols=1, skiprows = 1)

#Takes only the points for fitting alpha
x = dist[dist < 7]#This number is subject to change
y = []
for i in range(len(x)):
    y.append(cor[i]) 
    
#Apply Linear Fit
coefficients = np.polyfit(np.log(x), np.log(y), 1)
slope = coefficients[0]
intercept = coefficients[1]

xplot = np.linspace(0, np.log(x[-1]), 100)

plt.close()
plt.plot(np.log(x), np.log(y), "ko", label= "Height Correlation")
plt.plot(xplot, slope*xplot + intercept, "r", label=str(slope) + "x + " + str(intercept))
plt.legend()
plt.title(name)
plt.show()

print(slope)
