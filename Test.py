import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
h=[]
b=1
while b == 1:
  Years=input("years:2010-2019 or 2020-current, q to quit: ")
  Years.lower()
  if Years == "2010-2019":#choose if data is from 2010-2019 or 2020-current
    info=pd.read_json("https://data.lacity.org/resource/63jg-8b9z.json?$limit=100000")
    break
  elif Years == "2020-current":
    info=pd.read_json("https://data.lacity.org/resource/2nrs-mtv8.json?$limit=100000")
    break
  elif Years == "q":#way to quit 
    break
  else:#not valid in input
    print("did not put valad answer, please try again")
    continue
try:#how the text is going to look
  font1 = {'family':'serif','color':'blue','size':20}
  font2 = {'family':'serif','color':'black','size':10}
  for index,row in info.iterrows():
    x=row['lat']#latitude
    y=row['lon']#longitude
    if x != 0 and y !=0:
      plt.plot(x, y,marker = '*',ms=0.1)#maked  the graph
    
    h=h+[row['crm_cd_desc']]#get all the crimes commited
  plt.show()#show the map
  h.sort()#sort all the crimes
  z=set(h)#gets rid of all duplicates
  plt.figure(figsize=(15, 10))#sets size for graph

  for p in z:#gets all of the difrent crimes
    q = h.count(p)#see how many times the crime was commited
    plt.bar(p,q)#creates the bar
    plt.text(p, q, q,ha = 'center')#adds the labals to the graph
  plt.title("Crime in los Angeles",fontdict = font1)#title
  plt.xlabel("Longitude",fontdict = font2)#x labal
  plt.ylabel("Latitude",fontdict = font2)#y lebal
  plt.xticks(rotation=90)#rotates the titals and makes it so it doesn't overlap

  plt.show()#show graph
except:
  exit()#if you typed q it would quit