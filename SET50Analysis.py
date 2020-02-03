
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from time import strptime
def visualAll(dataset):
   print(dataset)
   dataset.plot(kind='line',x='Date',y='Price',color='red')
   plt.show()

def visualY20(dataset):
   print(dataset.loc[dataset["Date"].dt.year == 2020])
   data20 = dataset.loc[dataset["Date"].dt.year == 2020]
   data20.plot(kind='line',x='Date',y='Price',color='blue')
   plt.show()

def visualY19(dataset):
   print(dataset.loc[dataset["Date"].dt.year == 2019])
   data19 = dataset.loc[dataset["Date"].dt.year == 2019]
   data19.plot(kind='line',x='Date',y='Price',color='blue')
   plt.show()

def convertDate(x):
   x = x.replace(",","")
   arr = x.split(" ")
   newDate = "" + str(strptime(arr[0],'%b').tm_mon) + "/" + arr[1] + "/" + arr[2]
   return newDate
def Main():
   dirpath = os.path.dirname(__file__)
   pathData = dirpath + "/DataSet/"
   dataset = pd.read_csv(pathData + "SET50Data.csv")

   dataset["Price"] = [x.replace(",","") for x in dataset["Price"]]
   dataset["Price"] = dataset["Price"].astype(np.float64)
   #dataset = dataset.set_index("Date")

   dataset["Date"] = [ convertDate(x) for x in dataset["Date"]]
   dataset["Date"] = pd.to_datetime(dataset["Date"])
   #dataset = dataset.set_index("Date")
   dataset = dataset.sort_values("Date",ascending=True)
   #print(dataset)
   visualY20(dataset)
   visualY19(dataset)
   visualAll(dataset)

if __name__ == '__main__':
    Main()