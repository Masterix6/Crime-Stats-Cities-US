# script for getting the data from the api, removing unneccessary keys and converts it into a (for the programe) readable table

import pandas

keys_for_analyzing = { # keys which will be kept
    "NY": {
        "cmplnt_fr_dt": "start_date",
        "cmplnt_fr_tm": "start_time",
        "cmplnt_to_dt": "end_date",
        "cmplnt_to_tm": "end_time",
        "rpt_dt": "report_date",
        "": "",
    "LA":{
        "crm_cd_desc":"crime",
        "area":"area",
        "rpt_dist_no":"location_code",
        "vict_sex":"victums_sex",
        "vict_age":"victums_age",
        "vict_descent":"victum descent",
        "premis_cd":"premis_area"
    }


    }
} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=50000", # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data
    "LA": "https://data.lacity.org/resource/63jg-8b9z.json?$limit=50000",
}


def getDataFrame(city: str):


    return {}