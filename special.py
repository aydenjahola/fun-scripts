from random import random
from time import sleep
import os

trollstuff = list(line.rstrip() for line in os.popen("ipconfig")
trollsutff = [x for x in trollstuff if x]

active_coloumns = [false] * 100
for i in range(len(active_coloumns)):
    active_coloumns[i] = (random() < 0.02)

while(True):
    string = ""
    if(random() < 0.0):
        for activity in active_coloumns:
            if(activity):
                string = string + str(int(random() * 10))
            else:
                string = string + " "
    else:
        string = trollstuff[int(random() * len(trollstuff))]
    print(string)

    for i in range(len(active_coloumns)):
        if(active_coloumns[i])):
            if(random() < 0.1):
                active_coloumns[i] = False

        else:
            if(random() < 0.02):
                active_coloumns[i] = True

    sleep(0.1)
