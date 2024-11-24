import pandas as pd
location="C:\\Users\\dheeraj\\Desktop\\Python\\SPECTRA_WAVELENGTHS.csv"
data=pd.read_csv(location)
df=pd.read_csv(location,usecols=data.head())

def FileLoc():
    return location
def FogineData():
    return df
def Innospectra_NIR():
    return df.INNOSPECTRA_NIR
def Arcoptics_NIR():
    return df.ARCOPTIX_NIR
def wasatch_NIR():
    return df.WASATCH_NIR
def wasatch_VISNIR():
    return df.WASATCH_VISNIR

#print(data,'\n\n\n\n\n\n',df)