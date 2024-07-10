import pandas, datetime

conversion_data = {
    "NY": {
        "start_date":datetime,
        "start_time":datetime,
        "end_date":datetime,
        "end_time":datetime,
        "report_date":datetime,

        "crime_desc":False,
        "borough":False,

        "suspect_age":False,
        "suspect_race": {
            "BLACK HISPANIC": "Black hispanic",
            "UNKNOWN": "Unkown",
            "BLACK": "Black",
            "WHITE": "White",
            "ASIAN / PACIFIC ISLANDER": "Asian",
            "WHITE HISPANIC": "White hispanic",
            "AMERICAN INDIAN/ALASKAN NATIVE": "American indian",
            "(null)": "?",
        },
        "suspect_sex": {
            "M": "Male",
            "F": "Female",
            "U": "?",
            "(null)": "?",
        },

        "victim_age":False,
        "victim_race":{
            "BLACK HISPANIC": "Hispanic",
            "UNKNOWN": "Unkown",
            "BLACK": "Black",
            "WHITE": "White",
            "ASIAN / PACIFIC ISLANDER": "Asian",
            "WHITE HISPANIC": "Hispanic",
            "AMERICAN INDIAN/ALASKAN NATIVE": "American indian",
        },
        "vicitm_sex":{
            "M": "Male",
            "F": "Female",
            "D": "Diverse",
            "E": "?",
            "L": "?",
        },

        "latitude":False,
        "longitude":False,
    },
    
     "LA": {
        "start_date":datetime,
        "start_time":datetime,
        "report_date":datetime,
        
        "crime_desc":False,
        "borough":False,

        "victim_age":False,
        "victim_race":{
            "A": "Asian",
            "B": "Black",
            "C": "Asian",
            "D": "Asian",
            "F": "Asian",
            "G": "Asian",
            "H": "Hispanic",
            "I": "American indian",
            "J": "Asian",
            "K": "Asian",
            "L": "Asian",
            "O": "Unknown",
            "P": "Asian",
            "S": "Asian",
            "U": "Asian",
            "V": "Asian",
            "W": "White",
            "X": "Unknown",
            "Z": "Asian",
            "nan": "Unknown",

        },
        "vicitm_sex":{
            "M": "Male",
            "F": "Female",
            "nan": "Unknown"
        },

        "latitude":False,
        "longitude":False,
    }
}

def ConvertData(data_base: pandas.DataFrame, city: str, to_convert: (str | list)):


    return {}