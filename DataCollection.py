# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table

import pandas
#this is where we will store the opions for what you can choose
TypesOfInformationCities={"NY":{"Reported":["start_date","start_time","borough","suspect","victum"]},
                          "La":{"2010-2019":["area","victum","datetime_occured","location","crime"]},
                          "La":{"2020-current":["area","victum","datetime_occured","location","crime"]}}
while True:
    data_bases=input("What city do you want to look at, (about) to see what citys you can choose from, q to quit: ")
    data_bases.lower()
    if data_bases == "about":
        print(TypesOfInformationCities)
        continue
    elif data_bases=="q":
        quit()
    wanteddatatype=input("docuement do you want:")
    Wanteddata=input("what statistic do you want: ")
    break
keys_for_analyzing = { # keys which will be kept
    "NY": {
        ["cmplnt_fr_dt","cmplnt_to_dt"]: "date",
        ["cmplnt_fr_tm","cmplnt_to_tm"]: "start_time",
        "boro_nm": "borough",
        ["latitude","longitude"]:"location",
        ["susp_age_group","susp_race","susp_sex"]:"suspect",
        ["vic_age_group","vic_race","vict_sex"]:"victum",
    "LA":{
        "crm_cd_desc":"crime",
        ["area","rpt_dist_no","premis_cd"]:"area",
        ["vict_sex","vict_age","vict_descent"]:"victum",
        ["date_occ","time_occ"]:"datetime_occured",
        ["latitude","longitude"]:"location",
    }


    }
} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=50000", # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "LA": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=50000",
}


def getDataFrame(city: str):


    return {}