import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import DataCollectionI
import DataCollectionA
import folium

dataplayerwant=None
link=None
specificData=None
UserSpecificdata=None
ListOfValues=[]
b=0
colored= ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']
while True:
    b=b+1
    if b == 15:
        quit()
    dataplayerwants2,UserSpecificdata=DataCollectionI.getDataFrameI(link,dataplayerwant,specificData,UserSpecificdata,ListOfValues)
    link = DataCollectionA.getDataFrame(x,y,z)
    info=link
    
    m = folium.Map([40.7128, -74.0060], zoom_start=4)
    group_1 = folium.FeatureGroup("first group").add_to(m)
    for row in info:
    #find the latitude and longitude of all the crimes and what crimes were commited
        print(info)
        latitude=link[1]#latitude
        longitude=link[2]#longitude
        
        if latitude == "nan" or longitude == "nan":
            continue
        
        if longitude != 0 and latitude !=0:
            print(f"Lat: {type(latitude)}, Long: {longitude}")
            folium.Marker(
                location=[latitude,longitude],
                tooltip="Click me!",
                popup="2",
                icon=folium.Icon(color=colored[b]),
            ).add_to(m)
            #folium.LayerControl().add_to(m)
    m.save("index.html")
