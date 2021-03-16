import time
import pyautogui as pyg

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

