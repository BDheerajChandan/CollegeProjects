import matplotlib.pyplot as plt
import FromExcel
import pandas as pd

print("\nPress 1 for plotting fruit Batch ")
print("Press 2 for plotting fruit weight ")
print("Press 3 for plotting fruit's short width")
print("Press 4 for plotting fruit's long width")
print("Press 5 for plotting fruit's length")
print("Press 6 for plotting fruit volume")
print("Press 7 for plotting fruit's distance to probe")

Plot_Choice=int(input("\nEnter the choice : "))

if(Plot_Choice==1):
    plt.title("BATCHES")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis BATCH NUMBER")
    #plt.plot(FromExcel.Batch_Data(),'x')
    plt.plot(FromExcel.Batch_Data(),color='r')      # color="red"
    #plt.plot()
    #plt.show()

elif(Plot_Choice==2):
    plt.title("WEIGHT")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis FRUIT WEIGHT")
    plt.plot(FromExcel.Weight_Data(),color='g')     #color='green'
    #plt.show()


elif(Plot_Choice==3):
    plt.title("SHORT WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WIDTH")
    plt.plot(FromExcel.ShortWidth(),color='b')      #color='blue'
    #plt.show()

elif(Plot_Choice==4):
    plt.title("LONG WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WIDTH")
    plt.plot(FromExcel.LongWidth(),color='c')       #color='cyan'
    #plt.show()

elif(Plot_Choice==5):
    plt.title("LENGTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis LENGTH")
    plt.plot(FromExcel.Length(),color='m')          #color='magneta'
    #plt.show()

elif(Plot_Choice==6):
    plt.title("VOLUME")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis VOLUME")
    plt.plot(FromExcel.Volume(),color='y')          #color='yellow'
    #plt.show()

elif(Plot_Choice==7):
    plt.title("DISTANCE TO PROBE")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis DISTANCE")
    plt.plot(FromExcel.DistaceToProbe(),color='k')   #color='black'
    #plt.show()
else:
    print("WRONG CHOICE FOR PLOTTING")
plt.show()