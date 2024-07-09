import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
h=[]
b=1
while b == 1:
  Years=input("years:2010-2019 or 2020-current, q to quit: ")
  Years.lower()
  if Years == "2010-2019":
    info=pd.read_json("https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000000")
    break
  elif Years == "2020-current":
    info=pd.read_json("https://data.lacity.org/resource/2nrs-mtv8.json?$limit=1000000")
    break
  elif Years == "q":
    break
  else:
    print("did not put valad answer, please try again")
    continue
try:
  x_list = []
  y_list = []



  font1 = {'family':'serif','color':'blue','size':20}
  font2 = {'family':'serif','color':'black','size':10}
  for index,row in info.iterrows():
    if row['lat'] != 0 and row['lon'] != 0:
      x_list.append(row['lat'])
      y_list.append(row['lon'])
      h=h+[row['crm_cd_desc']]

  plt.scatter(x_list, y_list)
  plt.show()
  print("Here 1")
  #h = row['crm_cd_desc'].sort()
  z=set(h)
  print(z)
  plt.figure(figsize=(15, 10))

  for p in z:
    #print("Here")
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