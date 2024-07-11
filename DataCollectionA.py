# script for getting the data from the api, removing unneccessary keys and converts it into a (for the program) readable dict

import pandas, time

keys_for_analyzing = { # keys which will be kept
    "NY": {
        "cmplnt_fr_dt": "start_date",
        "cmplnt_fr_tm": "start_time",
        "cmplnt_to_dt": "end_date",
        "cmplnt_to_tm": "end_time",
        "rpt_dt": "report_date",

        "ofns_desc": "crime_desc",
        "boro_nm": "borough",

        "susp_age_group": "suspect_age",
        "susp_race": "suspect_race",
        "susp_sex": "suspect_sex",

        "vic_age_group": "victim_age",
        "vic_race": "victim_race",
        "vic_sex": "vicitm_sex",

        "latitude": "latitude",
        "longitude": "longitude",

    },

     "LA": {
        "date_occ": "start_date",
        "time_occ": "start_time",
        # "cmplnt_to_dt": "end_date", #
        # "cmplnt_to_tm": "end_time", #
        "date_rptd": "report_date",
        
        "crm_cd_desc": "crime_desc",
        "area_name": "borough",

        # "susp_age_group": "suspect_age", #
        # "susp_race": "suspect_race", #
        # "susp_sex": "suspect_sex", #

        "vict_age": "victim_age",
        "vict_descent": "victim_race",
        "vict_sex": "vicitm_sex",

        "lat": "latitude",
        "lon": "longitude",
    }
} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=1", # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "LA": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000", #https://data.lacity.org/Public-Safety/Crime-Data-from-2010-to-2019/63jg-8b9z/about_data
}

# get the Dataframe of choosen city with only valid coloums (to analyze)
def getDataFrame(city: str):
    start_time = time.time()
    data_base = None # data base from city crime api - none because value will be tried to set with 'try'
    label_conversion = None # conversion table (keys_for_analyzing) - also being set with 'try'

    # try to find city crime api
    try:
        data_base = data_bases[city]
    except:
        print("City not found")
        return False # error with finding city's crime api in api/data_bases dict (did not find)
    
    # try to find conversion table
    try:
        label_conversion = keys_for_analyzing[city]
    except:
        print("City not found")
        return False # error with finding city in conversion table (did not find)
    
    
    data_base = pandas.read_json(data_base) # get json data from api with pandas
    to_drop = list(data_base.columns) - label_conversion.keys() # set list of keys which are not eligible for analyzing

    data_base.drop(to_drop, axis=1, inplace=True) # removing not eligible keys
    data_base = data_base.rename(columns=label_conversion) # rename keys to (for program) readable format
    
    print(f"Total time for DataCollection (secs): {time.time() - start_time}")
    return data_base