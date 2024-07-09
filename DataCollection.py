# script for getting the data from the api and removing unneccessary keys

import pandas

keys_for_analyzing = { # keys which will be kept
    "start_date": {"NY": "cmplnt_fr_dt",},
    "start_time": {"NY": "cmplnt_fr_tm",},
    "end_date": {"NY": "cmplnt_to_dt",},
    "end_time": {"NY": "cmplnt_to_tm",},
    "report_date": {"NY": "rpt_dt",},

} 

data_bases = { # Structure: "City(short)": api # website
    "NY": "https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=50000" # https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i/about_data

}


def getDataFrame(city: str):


    return ""