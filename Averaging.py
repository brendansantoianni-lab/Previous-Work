import numpy as np
import matplotlib.pyplot as plt

#This opens the directory for the images that need to be averaged (make sure they're different)
location = "C:\\Users\\Connor Donovan\\Desktop\\PY452\\"
file1 = "Clean Wafer\\Region 1\\"
file2 = "Clean Wafer\\Region 2\\"
region1 = "CleanWafer_10um_R1"
region2 = "CleanWafer_10um_R2"

image1 = np.genfromtxt(location + file1 + region1 + ".txt", skip_header=1 )
image2 = np.genfromtxt(location + file2 + region2 + ".txt" , skip_header=1)


#This takes the average of the images for a given region
average = np.mean(np.array([ image1, image2 ]), axis=0)

#This takes only the flattened region of the averaged images
flat_avg = average[2049:2560, :]

#This shows the flattened average image and saves it to the Averaged Images file
#plt.imshow(flat_avg)
#plt.show()

np.savetxt(location + "Clean Wafer\\Averaged Images\\CleanWafer_10um_avg.txt", np.array(average),  delimiter='\t', fmt="%s")


#This subtracts the averaged background from the film images (make sure they're same size)
file = "Film\\Region 3\\"
film = "PolFilm_10um_R3"
filmImage = np.genfromtxt(location + file + film +".txt")

#This subtracts the background and saves the new image
backSubtract = filmImage - average 

#Uncomment this line to save the film image with subtracted background
np.savetxt(location + file + "Background Subtracted Images\\" + film + "_noBack.txt", np.array(backSubtract),  delimiter='\t', fmt="%s")


#This plots the original image and the one with a subtracted background
Original = filmImage[2049:2560, :]
No_Background = backSubtract[2049:2560, :]

fig, (ax1, ax2) = plt.subplots(1, 2)
    

ax1.imshow(Original)
ax1.set_title('Original - 10um')
    
ax2.imshow(No_Background)
ax2.set_title('No Background')


