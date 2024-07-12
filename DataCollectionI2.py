# script for getting the data from the api, removing unneccessary keys and converts it into a (for the program) readable dict

import pandas, time

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
    "la": {"2010-2019":"https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000","2020-current":"https://data.lacity.org/resource/2nrs-mtv8.json$limit=1000"}
}

# get the Dataframe of choosen city with only valid coloums (to analyze)
def getDataFrame(city: str,DataSet:str, column:str):
    start_time = time.time()
    data_base = None # data base from city crime api - none because value will be tried to set with 'try'
    label_conversion = None # conversion table (keys_for_analyzing) - also being set with 'try'

    # try to find city crime api
    try:
        data_base = data_bases[city][DataSet]
    except:
        print("City not found")
        return False # error with finding city's crime api in api/data_bases dict (did not find)
    
    # try to find conversion table
    try:
        label_conversion = keys_for_analyzing[city][DataSet][column]
    except:
        print("City not found")
        return False # error with finding city in conversion table (did not find)
    
    print(f"Gets json after {time.time() - start_time} seconds") 
    
    data_base = pandas.read_json(data_base) # get json data from api with pandas

    return data_base[label_conversion],data_base["latitude"],data_base["longitude"]
