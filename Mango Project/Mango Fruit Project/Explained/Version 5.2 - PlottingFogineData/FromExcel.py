import pandas as pd
location="Sample_immature_mature.csv"
data=pd.read_csv(location)
df=pd.read_csv(location,usecols=data.head())

def Batch_Data():
    return df.Batch_Fogiene
def Weight_Data():
    return df.WEIGHT_g
def ShortWidth():
    return df.DIA1_mm_shortwidth
def LongWidth():
    return df.DIA2_mm_longwidth
def Length():
    return df.DIA3_mm_length
def Volume():
    return df.VOLUME_ml
def DistaceToProbe():
    return df.Distance