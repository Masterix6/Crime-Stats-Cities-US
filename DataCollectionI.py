# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table

import pandas
#this is where we will store the opions for what you can choose
TypesOfInformationCities={"ny":{"reported":["start_date","start_time","borough","suspect","victum"]},
                          "la":[{"2010-2019":["area","victum","datetime_occured","location","crime"]}, 
                                {"2020-current":["area","victum","datetime_occured","location","crime"]}]}

keys_for_analyzing = { # keys which will be kept
    "ny": {
"reported":
        {"date":["start_date","end_date"],
        "start_time":["start_time","end_time"],
        "borough":["borough"],
        "location":["latitude","longitude"],
        "suspect":["suspect_age","suspect_race","suspect_sex"],
        "victim":["vic_age_group","vic_race","vict_sex"]}
    },
    "la":{
        "2010-2019":
        {"crime":["crm_cd_desc"],
        "area":["area","rpt_dist_no","premis_cd"],
        "victim":["vict_sex","vict_age","vict_descent"],
        "datetime_occured":["date_occ","time_occ"],
        "location":["latitude","longitude"]},


        "2020-current":
        {"crime":["crm_cd_desc"],
        "area":["area","rpt_dist_no","premis_cd"],
        "victim":["vict_sex","vict_age","vict_descent"],
        "datetime_occured":["date_occ","time_occ"],
        "location":["latitude","longitude"]}
    }   
} 

data_bases = { # Structure: "City(short)": api # website
    "ny": {"reported":"https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=1000"}, # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "la": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000",
}

dataplayerwants=None
link=None
def getDataFrame():
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
    global link
    link = data_bases.get(x).get(y)
    global dataplayerwants
    dataplayerwants = keys_for_analyzing.get(x).get(y).get(z)
    

    return link
