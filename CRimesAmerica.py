import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import DataProcessing
link=DataProcessing.getDataFrame()
dataplayerwants = None
#DataProcessing.getDataFrame()
print(link)
h=[] #every crime varuable
b=1
info=pd.read_json(link)
print(info)
font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'black','size':10}
for index,row in info.iterrows():
  #find the latitude and longitude of all the crimes and what crimes were commited
  x=row['latitude']#latitude
  y=row['longitude']#longitude
  if x != 0 and y !=0:
    plt.plot(x, y,marker = '*',ms=0.1)#maked  the graph
  
  h=h+[row['crime']]#get all the crimes commited
plt.show()#show the map
h.sort()#sort all the crimes
z=set(h)#gets rid of all duplicates
plt.figure(figsize=(15, 10))#sets size for graph

for p in z:#gets all of the difrent crimes
  q = h.count(p)#see how many times the crime was commited
  plt.bar(p,q)#creates the bar
  plt.text(p, q, q,ha = 'center')#adds the labals to the graph
plt.title(f"Crime Data",fontdict = font1)#title
plt.xlabel("Longitude",fontdict = font2)#x labal
plt.ylabel("Latitude",fontdict = font2)#y lebal
plt.xticks(rotation=90)#rotates the titals and makes it so it doesn't overlap

plt.show()#show graph
