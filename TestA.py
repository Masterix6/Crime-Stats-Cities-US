import pandas

data_set = pandas.read_json("https://data.cityofnewyork.us/resource/qgea-i56i.json?$limit=1000")
data_set2 = pandas.read_json("https://data.lacity.org/resource/63jg-8b9z.json?$limit=1000")

list_of_values = []
list_of_values2 = []

column_name = "ofns_desc"
column_name2 = "crm_cd_desc"

for each_value in data_set[column_name]:
    if not each_value in list_of_values:
        list_of_values.append(each_value)

print(len(list_of_values))

for each_value in data_set2[column_name2]:
    if each_value in list_of_values:
        list_of_values.remove(each_value)

    if not each_value in list_of_values2:
        list_of_values2.append(each_value)

print(len(list_of_values2))

print(len(list_of_values))