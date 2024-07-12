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
# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table
import pandas

import DataCollectionA

#this is where we will store the opions for what you can choose
TypesOfInformationCities={"ny":{"reported":["date","borough","suspect_age","suspect_race","suspect_sex","victim_age","vicrtim_ace","victim_sex"],
                                "arrest":["arrest_date","borough","perp_age","perp_sex","perp_race","crime"]},

                          "la":{"2010-2019":["crime","vict_sex","vict_age","vict_descent","datetime_occured","date_occ","crime"], 
                                "2020-current":["crime","vict_sex","vict_age","vict_descent","datetime_occured","date_occ","crime"]}
                            }
                            

keys_for_analyzing = { # keys which will be kept
    "ny": {
"reported":
        {
        "date":"cmplnt_to_dt",
        "borough":"boro_nm",
        "latitude":"latitude",
        "longitude":"longitude",
        "suspect_age":"susp_age_group",
        "suspect_race":"susp_race",
        "suspect_sex":"susp_sex",
        "victim_age":"vic_age_group",
        "vicrtim_ace":"vic_race",
        "victim_sex":"vic_sex"},
    "arrest":
        {"arrest_date":"arrest_date",
        "crime":"ofns_desc",
        "borough":"arrest_boro",
        "latitude":"latitude",
        "longitude":"longitude",
        "perp_age":"age_group",
        "perp_race":"perp_race",
        "perp_sex":"perp_sex"},
    },
    "la":{
        "2010-2019":
        {"crime":"crm_cd_desc",
        "area":"area",
        "vict_sex":"vict_sex",
        "vict_age":"vict_age",
        "vict_descent":"vict_descent",
        "date":"date_occ",
        "latitude":"lat",
        "longitude":"lon"},


        "2020-current":
        {"crime":"crm_cd_desc",
        "area":"area",
        "vict_sex":"vict_sex",
        "vict_age":"vict_age",
        "vict_descent":"vict_descent",
        "date":"date_occ",
        "latitude":"lat",
        "longitude":"lon"},
    }   
} 
data_bases = { # Structure: "City(short)": api # website
    "ny": {"reported":"https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=1000","arrest":"https://data.lacity.org/resource/2nrs-mtv8.json"}, # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "la": {"2010-2019":"https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000","2020=current":"https://data.lacity.org/resource/2nrs-mtv8.json?$limit=1000"}
}

dataplayerwants2=None
link=None
specificData=None
UserSpecificdata=None
ListOfValues=None
def getDataFrameI(link,dataplayerwants2,specificData,UserSpecificdata,ListOfValues):
    b=1
    while b==1:
        print(TypesOfInformationCities.keys())
        x=input("use the form city q to quit: ")
        if x =="q":
            quit()
        if x in TypesOfInformationCities:
            print(TypesOfInformationCities[x])
            y=input("use the form data, q to quit: ")
            if y == "q":
                quit()
            if y in TypesOfInformationCities.get(x):
                print(TypesOfInformationCities[x][y])
                z=input("use the form information, q to quit: ")
                if z== "q":
                    quit()
                if z in TypesOfInformationCities.get(x).get(y):
                    print("hello")
                    break

        else:
            print("Something went wrong, check if you put in right form")
            continue
    link = DataCollectionA.getDataFrame(x,y,z)
    
    # print(link)
    # print(f"Type is: {type(link)}")
    dataplayerwants2 = z

    specificData=link[0].tolist()
    for IndividualData in specificData:
        IndividualData.split(" ")
        ListOfValues.append(IndividualData)
    ListOfValues=set(ListOfValues)
        
    
    while True:
        print(ListOfValues)
        UserSpecificdata=input("what spacific data do you want? choose from choises above")
        UserSpecificdata.lower()
        if UserSpecificdata in specificData:
            break
        elif UserSpecificdata == "q":
            quit()
        else:
            print("sorry something went wrong, check if it is in wright form")
            continue

    return link, dataplayerwants2, UserSpecificdata
