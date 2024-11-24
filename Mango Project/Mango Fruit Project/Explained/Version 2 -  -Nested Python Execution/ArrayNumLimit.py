# Import required packages
import random
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import time,datetime

# Give input for range
limit=int(input("Enter the limit : "))

# Collect the random numbers of specific range 
Arr_num=[]
dateslist=[]
timelist=[]

for i in range(limit):
    Arr_num.append(random.randint(0,9)) # Append the random values which numbers are in between 0,9 as list
    dateslist.append(date.today())
    timelist.append(datetime.datetime.now().time())
def n():
    return Arr_num # Return the Appended list
def dates():
    return dateslist
def Currenttime():
    return timelist


