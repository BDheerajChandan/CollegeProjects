# Import required packages
import random
import pandas as pd
import matplotlib.pyplot as plt

# Give input for range
limit=int(input("Enter the limit : "))

# Collect the random numbers of specific range 
Arr_num=[]
for i in range(limit):
    Arr_num.append(random.randint(0,9)) # Append the random values which numbers are in between 0,9 as list

def n():
    return Arr_num # Return the Appended list
