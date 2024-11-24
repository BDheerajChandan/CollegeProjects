import matplotlib.pyplot as plt
import FromExcel
import pandas as pd

print("Press 1 for plotting fruit Batch ")
print("Press 2 for plotting fruit weight ")
print("Press 3 for plotting fruit's short width")
print("Press 4 for plotting fruit's long width")
print("Press 5 for plotting fruit's length")
print("Press 6 for plotting fruit volume")
print("Press 7 for plotting fruit's distance to probe")


Plot_Choice=int(input("Enter the choice : "))


if(Plot_Choice==1):
    plt.title("BATCHES")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis BATCH NUMBER")
    #plt.plot(FromExcel.Batch_Data(),'x')
    plt.plot(FromExcel.Batch_Data())
    #plt.plot()
    #plt.show()

elif(Plot_Choice==2):
    plt.title("WEIGHT")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis FRUIT WEIGHT")
    plt.plot(FromExcel.Weight_Data())
    #plt.show()


elif(Plot_Choice==3):
    plt.title("SHORT WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WIDTH")
    plt.plot(FromExcel.ShortWidth())
    #plt.show()

elif(Plot_Choice==4):
    plt.title("LONG WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WIDTH")
    plt.plot(FromExcel.LongWidth())
    #plt.show()

elif(Plot_Choice==5):
    plt.title("LENGTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis LENGTH")
    plt.plot(FromExcel.Length())
    #plt.show()

elif(Plot_Choice==6):
    plt.title("VOLUME")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis VOLUME")
    plt.plot(FromExcel.Volume())
    #plt.show()

elif(Plot_Choice==7):
    plt.title("DISTANCE TO PROBE")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis DISTANCE")
    plt.plot(FromExcel.DistaceToProbe())
    #plt.show()

plt.show()