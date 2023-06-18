import pyautogui as pg
import time
import random as r
from datetime import datetime

 

# 2 seconds sleep so that you can open you VDI/Application
time.sleep(2)
i=1

 

#running while loop
while 1 :
    #provide random coordinate values to x,y to keep your mouse within those range
    x,y=r.randint(1074,1151),r.randint(354,433)
   
    #Print the number of times the loop has run to keep a record, not necessary can be commented
    print("No. of times- ", i)

    #to check on current time to keep track of time. Not necessary, can be removed
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    #actual moving of the cursor , DONT REMOVE. 
    pg.moveTo(x,y,2)
    pg.leftClick()
    time.sleep(5)
    i += 1
