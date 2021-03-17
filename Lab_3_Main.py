import time
import pyautogui as pyg
import numpy as np

# %% Part 1

print(pyg.position()) # Get and print current mouse pos
# Newfile on Spyder is x=30 y=110

# Dimensions are just screen resolution
# Maximums x = 1920, y = 1080, ade
x_max = 1920
y_max = 1080


#pyg.click(x=30,y=110,clicks=1,interval=0.1,button='left')

print(pyg.position())
#pyg.click(button=1)

# %% Part 2
'''
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
'''        
# %% Part 3

# I've never imported libraries at a place other than top of script before
# NOTE, Labs and Projects are in different working dir's, sys commands remedy that by adding those to pth at runtime
import sys
sys.path.insert(1, 'C:\\Users\Artur Smiechowski\Documents\BME227_Code\BME227_Project_1')
# Import project 1 code
import Main

Main.read_and_plot_serial_data('COM4', 40, 2, 500)

# %% Part 4

# File names changed for convienance
# Data pruned due to issue described in lab submission

# Data File to load (L and R emg recordings)
input_file = "Data_Values.npy"

# Load Numpy Array of Sample Times (Actual, not predicted)
emg_time = np.load("Data_Time.npy")[0:14800] # Values sliced due to signal drop

# Load Numpy Array of Sample Data
emg_voltage = np.load(input_file)[0:14800][:] # Values sliced due to signal drop

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
            
            