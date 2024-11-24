#Import required packages
import pandas as pd
import ArrayNumLimit
import InputString
import InputNumber
import PlotGraph

# Defining the functions

c=InputString.b()
num=int(input("Enter the Number :"))
l=InputNumber.b()
e=ArrayNumLimit.n()

# To check output / Return values from function 
print(l) # Return value from function a() 
print(c) # Return value from function b() 
print(ArrayNumLimit.n())

# Create the Data frame
df1 = pd.DataFrame([['Hi', 'Hello', 'Hey'], ['Nandini', 'Rupali', 'Malina'], ['Ram','Shyam', 'Babu']], index=['one', 'two', 'three'], columns=['a', 'b', 'c'])# "index" are rows and "columns" are columns
df2 = pd.DataFrame([c,l],index=["String","Number"],columns=["Output"])
df3 = pd.DataFrame(e,index=[i for i in range(len(ArrayNumLimit.n()))],columns=["Numbers"])

#Create excel sheet at custom location and write the data to it using dataframe
with pd.ExcelWriter("C:\\Users\\dheeraj\\Desktop\\Python\\ToExcel_1.xls") as writer:
    df1.to_excel(writer, sheet_name='sheet_A') # giving custom sheet 1
    df2.to_excel(writer, sheet_name='sheet_B') # giving custom sheet 2
    df3.to_excel(writer, sheet_name='sheet_C') # giving custom sheet 2

#To Display the dataframe 
def out1():
    return df1
def out2():
    return df2
def out3():
    return df3
def out4():
    return PlotGraph.plotG()