import matplotlib.pyplot as plt
import FromExcel
import numpy as np

print("\nPress 1 for plotting INNOSPECTRA_NIR data ")
print("Press 2 for plotting ARCOPTIX_NIR data ")
print("Press 3 for plotting WASATCH_NIR data")
print("Press 4 for plotting WASATCH_VISNIR data")

Plot_Choice=int(input("\nEnter the choice : "))
#Plot_Choice=9
if(Plot_Choice==1):
    plt.title("INNOSPECTRA DATA")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis INNOSPECTRA")
    #plt.plot(FromExcel.Batch_Data(),'x')
    plt.plot(FromExcel.Innospectra_NIR(),color='r')      # color="red"
    #plt.plot()
    #plt.show()

elif(Plot_Choice==2):
    plt.title("ARCOPTICS")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis ARCOPTICS")
    plt.plot(FromExcel.Arcoptics_NIR(),color='g')     #color='green'
    #plt.show()


elif(Plot_Choice==3):
    plt.title("SHORT WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WASATCH_NIR")
    plt.plot(FromExcel.wasatch_NIR(),color='b')      #color='blue'
    #plt.show()

elif(Plot_Choice==4):
    plt.title("LONG WIDTH")
    plt.xlabel("X-Axis FRUIT ID")
    plt.ylabel("Y-Axis WIDTH")
    plt.plot(FromExcel.WASATCH_VISNIR,color='c')       #color='cyan'
    #plt.show()

    '''elif(Plot_Choice==5):
        fig,axis=plt.subplots(2,2)
        fig.suptitle("SHORT,LONG,LENGTH & VOLUME")                # Plotting 3 graphs in a single graph    
        axis[0,0].set_xlabel("X-Axis FRUIT ID")          
        axis[0,0].set_ylabel("Y-Axis SHORT WIDTH")  # 1. plotting short width graph 
        axis[0,0].set_title("SHORT WIDTH")
        axis[0,0].plot(FromExcel.ShortWidth(),color='b')
        
        axis[0,1].set_xlabel("X-Axis FRUIT ID")          
        axis[0,1].set_ylabel("Y-Axis LONG WIDTH")  # 2. plotting long width graph 
        axis[0,1].set_title("LONG WIDTH")
        axis[0,1].plot(FromExcel.LongWidth(),color='c')
        
        axis[1,0].set_xlabel("X-Axis FRUIT ID")          
        axis[1,0].set_ylabel("Y-Axis LENGTH")  # 3. plotting length graph 
        axis[1,0].set_title("LENGTH")
        axis[1,0].plot(FromExcel.Length(),color='m')

        axis[1,1].set_xlabel("X-Axis FRUIT ID")          
        axis[1,1].set_ylabel("Y-Axis VOLUME")  # 4. plotting length graph 
        axis[1,1].set_title("VOLUME")
        axis[1,1].plot(FromExcel.Volume(),color='y')
        #plt.show()
''''''
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
        #plt.show()'''

else:
    print("WRONG CHOICE FOR PLOTTING")
plt.show()