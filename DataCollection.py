# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table

import pandas

keys_for_analyzing = { # keys which will be kept
    "NY": {
        "cmplnt_fr_dt": "start_date",
        "cmplnt_fr_tm": "start_time",
        "cmplnt_to_dt": "end_date",
        "cmplnt_to_tm": "end_time",
        "rpt_dt": "report_date",
        
        "law_cat_cd": "lvl_offense",
        "boro_nm": "borough",
        "susp_age_group": "suspect_age",
        "susp_race": "suspect_race",
        "susp_sex": "suspect_sex",

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
        "vict_descent": "victim_race", # needs conversion
        "vict_sex": "vicitm_sex", # needs conversion

        "lat": "latitude",
        "lon": "longitude",
    }
} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=1000", # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "LA": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000", #https://data.lacity.org/Public-Safety/Crime-Data-from-2010-to-2019/63jg-8b9z/about_data
}


def getDataFrame(city: str):
    data_base = None
    label_conversion = None
    try:
        data_base = data_bases[city]
    except:
        print("City not found")
        return False
    
    try:
        label_conversion = keys_for_analyzing[city]
    except:
        print("City not found")
        return False    
    
    data_base = pandas.read_json(data_base)
    to_drop = list(data_base.columns) - label_conversion.keys()

    data_base.drop(to_drop, axis=1, inplace=True)
    data_base = data_base.rename(columns=label_conversion)
    
    return data_base