# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table

import pandas
TypesOfInformationCities={"NY":{"Reported":["start_date","start_time",'borough']},"La":""}
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
        "area":"area",
        "rpt_dist_no":"location_code",
        "vict_sex":"victums_sex",
        "vict_age":"victums_age",
        "vict_descent":"victum descent",
        "premis_cd":"premis_area",
        "date_occ":"date_occured",
        "time_occ":"time_occured",
    }


    }
} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=50000", # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "LA": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=50000",
}


def getDataFrame(city: str):


    return {}