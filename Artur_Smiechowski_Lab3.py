'''
Artur_Smiechowski_Lab3.py

@author: Artur Smiehcowski

A program that:
    Uses pyautogui to create a new txt file and write name to if before saving
    Run  a loop that controls the mouse via keboard input
    Call the main method of lab 1 and graph/save the data from 2 EMG channels
    Reshape the saved EMG data into 200ms long epochs, save the 3D array and graph one "action" epoch
'''
# %% General Imports
import time
import pyautogui as pyg
import numpy as np

# %% Part 1
# Import os.path to allow checking for existing file
from os import path

# Open a newfile on Spyder
pyg.hotkey('ctrl', 'n') # Use a hotkey approach to avoid missing with cursor
time.sleep(0.01) # Wait 1/100th of a second to allow for computer to act

# Write name to the new file
pyg.typewrite('Artur Alex Smiechowski', interval=0.0001) # Interval works as omitted, small time just in case and to demonstrate
time.sleep(0.01)

# Save the file
pyg.hotkey('ctrl','s')
time.sleep(0.01) # Wait 1/100th of a second to allow for computer to act

# Type the filename
pyg.typewrite('name.txt', interval=0.0001)

# Hit enter to save
pyg.typewrite('\n') # \n newline is the enter key

# Add a hit to the 'y' key if the file needs to be overwritten
if path.exists('name.txt'):
    time.sleep(0.01)
    pyg.typewrite('y') # hit y to confirm file  overwrite

# %% Part 2

# Dimensions are just screen resolution
# Maximums x = 1920, y = 1080
x_max = 1920
y_max = 1080


for step in range(10):
    value = input("Please enter a string:\n")
    cur_pos = pyg.position()
    print(cur_pos[0])
    print("You entered %s"%value)
    
    if(value == 'w'):
        pyg.moveTo(cur_pos[0],cur_pos[1]-(y_max/5))
    if(value == 'a'):
        pyg.moveTo(cur_pos[0]-(x_max/5),cur_pos[1])
    if(value == 's'):
        pyg.moveTo(cur_pos[0],cur_pos[1]+(y_max/5))
    if(value == 'd'):
        pyg.moveTo(cur_pos[1]+(x_max/5),cur_pos[1])
    if(value == 'x'):
        pyg.click()
        
# %% Part 3

# I've never imported libraries at a place other than top of script before
# NOTE, Labs and Projects are in different working dir's, sys commands remedy that by adding those to pth at runtime
import sys
sys.path.insert(1, 'C:\\Users\Artur Smiechowski\Documents\BME227_Code\BME227_Project_1')
# Import project 1 code
import Main

Main.read_and_plot_serial_data('COM4', 40, 2, 500)

# %% Part 4
#import plotting library
from matplotlib import pyplot as plt

# File names changed for convienance
# Data pruned due to issue described in lab submission

# Data File to load (L and R emg recordings)
input_file = "Data_Values"

# Load Numpy Array of Sample Times (Actual, not predicted)
emg_time = np.load("Data_Time.npy")[0:14800] # Values sliced due to signal drop

# Load Numpy Array of Sample Data
emg_voltage = np.load(input_file + ".npy")[0:14800][:] # Values sliced due to signal drop

# Initialize an empty 3D epoch array 
emg_epoch = np.zeros((100, np.shape(emg_voltage)[1], int(len(emg_time)/100)+1)) 
#(~100 is average sample count per 200ms, due to variance cannot dynamically extract)
# Tried to avoid magic numbers where possible, epoch number +1 to account for remainder data whose index not divisible by epoch_sample_count

# Fill 3D epoch array with loaded data
for epoch in range(np.shape(emg_epoch)[2]): # Iterate Through the epochs
    for channel in range(np.shape(emg_epoch)[1]): # Iterate Through Data Channels
        for sample in range(np.shape(emg_epoch)[0]): # Iterate Through each sample in the epoch
            # Set the value in emg_epoch
            emg_epoch[sample][channel][epoch] = emg_voltage[sample*(epoch+1)][channel] # sample index +1 to prevent only pulling same data on first index
            
# Save the epoched data
np.save(input_file + "_epochs.npy", emg_epoch)

# Plot an "action" epoch (will use epoch 20; both hands clenched)

plt.clf() # Clear figure just in case

# Epoch to graph as variable for ease of change
graphed_epoch = 20

# Set up format and labels for graph
plt.title('EMG Data Left/Right Arms at Epoch ' + str(graphed_epoch))
plt.xlabel('time(ms)')
plt.ylabel('Voltage(V)')

# Graph Left hand channel
plt.plot(np.linspace(0, 200, len(emg_epoch[:][0][0])), emg_epoch[:][graphed_epoch][0], label='Left Arm') # Why does epoch and channel index swap? No clue but inspection shows it does for some reason
# Graph Right hand channel
plt.plot(np.linspace(0, 200, len(emg_epoch[:][0][0])), emg_epoch[:][graphed_epoch][1], label='Right Arm')

plt.legend() # Show the line legend for left vs right arm

# Save the plot
plt.savefig('emg_figure_at_epoch_'+str(graphed_epoch))

plt.show() # Show the plot on screen
