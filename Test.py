import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
h=[]
b=1
while b == 1:
  Years=input("years:2010-2019 or 2020-current, q to quit: ")
  Years.lower()
  if Years == "2010-2019":
    info=pd.read_json("https://data.lacity.org/resource/63jg-8b9z.json?$limit=10000")
    break
  elif Years == "2020-current":
    info=pd.read_json("https://data.lacity.org/resource/2nrs-mtv8.json?$limit=10000")
    break
  elif Years == "q":
    break
  else:
    print("did not put valad answer, please try again")
    continue
try:
  font1 = {'family':'serif','color':'blue','size':20}
  font2 = {'family':'serif','color':'black','size':10}
  for index,row in info.iterrows():

    x=row['lat']
    y=row['lon']
    if x != 0 and y !=0:
      plt.plot(x, y,marker = '*',ms=0.06)
    
    h=h+[row['crm_cd_desc']]
  plt.show()
  h.sort()
  z=set(h)
  plt.figure(figsize=(15, 10))

  for p in z:
    q = h.count(p)
    plt.bar(p,q)
    plt.text(p, q, q,ha = 'center')
  plt.title("Crime in los Angeles",fontdict = font1)
  plt.xlabel("Longitude",fontdict = font2)
  plt.ylabel("Latitude",fontdict = font2)
  plt.xticks(rotation=90)

  plt.show()
except:
  exit()