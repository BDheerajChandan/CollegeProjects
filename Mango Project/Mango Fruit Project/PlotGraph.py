import matplotlib.pyplot as plt
import FromExcel
import numpy as np

print("\nPress 1 for plotting fruit Batch ")
print("Press 2 for plotting fruit weight ")
print("Press 3 for plotting fruit's short width")
print("Press 4 for plotting fruit's long width")
print("Press 5 for plotting fruit's length")
print("Press 6 for plotting fruit volume")
print("Press 7 for plotting fruit's distance to probe")
print("Press 8 for plotting fruit's Short,Long,Length&Volume")
print("Press 9 for plotting fruit's Short,Long,Length")

Plot_Choice=int(input("\nEnter the choice : "))
#Plot_Choice=9
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

elif(Plot_Choice==8):
    fig,axis=plt.subplots(2,2)
    fig.suptitle("SHORT,LONG,LENGTH & VOLUME")                # Plotting 3 graphs in a single graph
    
    axis[0,0].set_xlabel("X-Axis FRUIT ID")          
    axis[0,0].set_ylabel("Y-Axis SHORT WIDTH")  # 1. plotting short width graph 
    axis[0,0].set_title("SHORT WIDTH")
    axis[0,0].plot(FromExcel.ShortWidth(),color='b')
    
    axis[0,1].set_xlabel("X-Axis FRUIT ID")          
    axis[0,1].set_ylabel("Y-Axis LONG WIDTH")  # 1. plotting long width graph 
    axis[0,1].set_title("LONG WIDTH")
    axis[0,1].plot(FromExcel.LongWidth(),color='c')
    
    axis[1,0].set_xlabel("X-Axis FRUIT ID")          
    axis[1,0].set_ylabel("Y-Axis LENGTH")  # 1. plotting length graph 
    axis[1,0].set_title("LENGTH")
    axis[1,0].plot(FromExcel.Length(),color='m')

    axis[1,1].set_xlabel("X-Axis FRUIT ID")          
    axis[1,1].set_ylabel("Y-Axis VOLUME")  # 1. plotting length graph 
    axis[1,1].set_title("VOLUME")
    axis[1,1].plot(FromExcel.Volume(),color='y')
    #plt.show()

elif(Plot_Choice==9):
        fig,axis=plt.subplots(2,2)
        fig.suptitle("SPECTROMETER DATA")                # Plotting 3 graphs in a single graph
        
        axis[0,0].set_xlabel("X-Axis FRUIT ID")          
        axis[0,0].set_ylabel("Y-Axis INNOSPECTRA")  # 1. plotting short width graph 
        axis[0,0].set_title("INNOSPECTRA")
        axis[0,0].plot(FromExcel.ShortWidth(),color='b')
        
        axis[0,1].set_xlabel("X-Axis FRUIT ID")          
        axis[0,1].set_ylabel("Y-Axis LONG WIDTH")  # 2. plotting long width graph 
        axis[0,1].set_title("LONG WIDTH")
        axis[0,1].plot(FromExcel.LongWidth(),color='c')
        
        axis[1,0].set_xlabel("X-Axis FRUIT ID")          
        axis[1,0].set_ylabel("Y-Axis LENGTH")  # 3. plotting length graph 
        axis[1,0].set_title("LENGTH")
        axis[1,0].plot(FromExcel.Length(),color='m')

        axis[1,1].set_title("SHORT , LONG , LENGTH")
        axis[1,1].set_xlabel("X-Axis FRUIT ID")          
        axis[1,1].set_ylabel("Y-Axis SHORT,LONG,LENGTH")  # 4. plotting short,long widths and length in graph 
        axis[1,1].plot(FromExcel.ShortWidth(),color='b')
        axis[1,1].plot(FromExcel.LongWidth(),color='c')
        axis[1,1].plot(FromExcel.Length(),color='m')
        #plt.show()
else:
    print("WRONG CHOICE FOR PLOTTING")
plt.show()