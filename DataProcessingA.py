import pandas, datetime, math

age_groups = {"<18": range(0,18), "18-24": range(18,25), "25-44": range(25,45), "45-64": range(45,65), "65+": range(65, 120)} # all age groups (from ny data)
valid_ages = range(0,120) # acceptable range of ages
age_conversion = [] # age conversion list to assing the age group easier

for age_def, age_group in age_groups.items(): # set age_conversion dict from age_groups
    for age in age_group:
        age_conversion.insert(age, age_def)


def ConvertAge(age_value): # function to convert the age into age group
    try:
        int(age_value)
        if age_value in valid_ages:
            return age_conversion[age]
        else:
            return "UNKNOWN"
        
    except:
        return age_value
    

conversion_data = { # data for conversion to global names (align city data)
    "NY": {
        "start_date":"date",
        "start_time":"time",
        "end_date":"date",
        "end_time":"time",
        "report_date":"date",

        "crime_desc":False,
        "borough":False,

        "suspect_age":ConvertAge,
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

        "victim_age":ConvertAge,
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
        "start_date":"date",
        "start_time":"time",
        "report_date":"date",
        
        "crime_desc":False,
        "borough":False,

        "victim_age":ConvertAge,
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

def clamp(number: int, min: int, max: int): # return number inbetween min and max (sets to limit if out of range), (made since sometime values are wrong, e.g. year: 1022)
    if number > max:
        number = max
    elif number < min:
        number = min

    return number
    
def ExtractDate(DateValue:(str | datetime.datetime | datetime.date)): # can extract the date of different types
    '''Returns (year, month, day) of given Value
    '''
    #print(f"DateValue: {DateValue[5:6]}")
    if type(DateValue) == str:
        return int(DateValue[0:4]), int(DateValue[5:7]), int(DateValue[8:10])
    elif type(DateValue) == datetime.datetime:
        return DateValue.year, DateValue.month, DateValue.day
    elif type(DateValue) == datetime.date:
        return DateValue.year, DateValue.month, DateValue.day
    else:
        print("Date is not a valid type")
        return 
    

def ExtractTime(TimeValue:(str | datetime.datetime | datetime.time)): # can extract the time of different types
    '''Returns (hour, second) of given Value
    '''
    #print(TimeValue)
    if type(TimeValue) == str:
        return int(TimeValue[0:2]), int(TimeValue[3:5])
    elif type(TimeValue) == datetime.datetime:
        return TimeValue.hour, TimeValue.second
    elif type(TimeValue) == datetime.time:
        return TimeValue.hour, TimeValue.second
    else:
        print("Time is not a valid type")
        return 0, 0

def CreateDatetime(TimeValue:(str | datetime.datetime | datetime.date | datetime.time),
                   TimeType: str, 
                   IsMerged: bool):
    '''This function can combine date and time to a datetime but can also handle
    time and date as single value.
    '''
    
    #print(f"Time Value: {TimeValue}, TimeType: {TimeType}, IsMerged: {IsMerged}")
    
    if TimeType == "date":
        Date = TimeValue[0:10]
        Time = TimeValue[23:32] if IsMerged else None
    elif TimeType == "time":
        Date = TimeValue[9:19] if IsMerged else None
        Time = TimeValue[0:8]


    #print(f"Date: {Date} -- Time: {Time}")
    if Date:
        year, month, day = ExtractDate(Date)
        hour, second = ExtractTime(Time)

        year = clamp(year, 2019, 2024)
        #print(f"Month: {month}")
        return datetime.datetime(year, month, day, hour, second)
    
    else:
        hour, second = ExtractTime(Time)
        return datetime.time(hour, second)

def ConvertFromDict(value, city, key): # function for dataframe.apply(function)
    return conversion_data[city][key][value]



def ConvertData(data_base: pandas.DataFrame, city: str, to_convert: str, merge=False):
    '''This function converts the values of one column into global readable values and returns the new data base.
    If merging it will combine 2 data columns into the given column, other column will be not changed.
    '''
    coloumn = None # column from data base
    conversion = None # conversion data from conversion_data
    merge_column = None # other coloumn from merge in case of a merge

    # check if column exits
    try:
        coloumn = data_base[to_convert]
    except:
        print("The column tried to convert does not exits.")
        return data_base # return unchanged data base

    # check if converion data exits
    try:
        conversion = conversion_data[city][to_convert]
    except:
        print("Conversion tried to access non existing conversion data.")
        return data_base # return unchanged data base
    
    if conversion == False: # False = format is already good, no changing needed
        print("Conversion not possible")
        return data_base # return unchanged data base

    # get column and conversion data for merge if merge is requested
    if merge:
        split_num = to_convert.find("_") # "start_time" <-> "start_date" <- format of mergable keys "name_type", type referes to type of time (date or time(mins, hrs...)
        #print(type(split_num))
        
        if split_num > 0: # if it was able to find a split character to split name and type
            #print(to_convert)
            string_name, string_time = to_convert[0:split_num], to_convert[(split_num + 1):len(to_convert)] # split key-name into 'name' and 'type'
            #print(string_time)
            if string_time == "date" or string_time == "time": # only types which are elgiable for merge
                opposit = "time" if string_time == "date"  else "date" # get the other to find the merge column
                #print(3)
                try: # try to find merge column
                    merge_column = data_base[f"{string_name}_{opposit}"]
                except: # couldnt find merge column
                    print("Merge failed, continuing single conversion")

    #print(f"Merge column: {merge_column}")
    #print(type(None))
    if type(merge_column) != type(None):
        coloumn = coloumn + merge_column
        #print(coloumn)


    if type(conversion) == dict:
        data_base[to_convert] = coloumn.apply(ConvertFromDict, args=(city, to_convert))

    elif type(conversion) == str: # it will be considered as date or time type
        data_base[to_convert] = coloumn.apply(CreateDatetime, args=(conversion, type(merge_column) != type(None)))
        #coloumn[index] = 
        # data_base[to_convert][index] = CreateDatetime(value, conversion, merge_column[index] if merge_column else None)

    elif type(conversion) == type(ConvertAge):
        data_base[to_convert] = coloumn.apply(conversion)

        
           
    #data_base[to_convert] = coloumn #whats best way?

    return data_base




def GetGraph_CompareCities(dataframes: (tuple | list), 
                           x_column: (str), 
                           y_column: str | None = None, 
                           y_lookfor = None, 
                           filter_mode: str | None = None):
    '''This function counts the amount of a appearances of one value in different data frames. 
    X_values are the names sorted and y_values the amount of those.
    '''

    x_values = set() # set so no doubles, only unique
    x_values_indexs = {} # x_value: index of x_value in
    graphs = {} # y_value for each graph/dataframe
    attribute_of_value = filter_mode

    dataframe_for_x = dataframes[0]

    #test = set()

    # get each unquie value also by extracitng values from classes like datetime
    for value in dataframe_for_x[x_column]:
        try:
            #test.add(type(value))
            if type(value) == pandas.Timestamp or type(value) == datetime.datetime: # check if can extract date/times from time
                if filter_mode == "month":
                    x_values.add(int(value.month))

                elif filter_mode == "day":
                    x_values.add(int(value.day))

                elif filter_mode == "hour" and value.hour:
                    x_values.add(int(value.hour))

                elif filter_mode == "second" and value.second:
                    x_values.add(int(value.second))

                else: # year standard lookfor
                    x_values.add(int(value.year))
                    attribute_of_value = "year"

            else: # otherwise just use value as label(x_value)
                print("else")
                x_values.add(int(value))

        except: # something went wrong, the rest of function does not with without x_values
            #print(test)
            print("Creating x values failed, returnig")
            return

    x_values = list(x_values) # convert to list so matplotlib can work with it
    x_values.sort() # sort it to not mess up graphs (which go for example backwards)

    # create table to easier change the correct value with the correct index in the y_values/graphs dict
    index = 0
    for value in x_values:
        x_values_indexs[value] = index
        index += 1

    # create keys/indexs to prevent key error
    current_graph = 0
    for dataframe in dataframes:
        for index in x_values_indexs.values():
            try:
                graphs[current_graph][index] = 0
            except:
                graphs[current_graph] = {}
                graphs[current_graph][index] = 0

            
        # loop to count values
        if y_lookfor: # if it should count each row haveing a ceratin value (for example each row of the year 2020)
            if attribute_of_value: # if for example it should extract year from datetime
                for index, row in dataframe.iterrows():
                    if row[y_column] == y_lookfor:
                        graphs[current_graph][int(x_values_indexs[row[x_column].__getattribute__(attribute_of_value)])] += 1 # add 1 to the value which is linked to the same data value

            else: # if it should just take the value without extraction
                for index, row in dataframe.iterrows():
                    if row[y_column] == y_lookfor:
                        graphs[current_graph][int(x_values_indexs[row[x_column]])] += 1 # add 1 to the value which is linked to the same data value
                
        else:
            if attribute_of_value: # if for example it should extract year from datetime
                for index, row in dataframe.iterrows():
                    graphs[current_graph][int(x_values_indexs[row[x_column].__getattribute__(attribute_of_value)])] += 1 # add 1 to the value which is linked to the same data value
            
            else: # if it should just take the value without extraction
                for index, row in dataframe.iterrows():
                    graphs[current_graph][int(x_values_indexs[row[x_column]])] += 1 # add 1 to the value which is linked to the same data value

        graphs[current_graph] = list(graphs[current_graph].values()) # convert each graph to list to make it readable for matplotlib
        current_graph += 1

    return [list(x_values), graphs]





def GetGraph_CompareCity(dataframe: pandas.DataFrame, 
                           x_column: str, 
                           y_column: str, 
                           filter_mode: str | None = None):
    '''This function counts the amount of a appearances of one value in different data frames. 
    X_values are the names sorted and y_values the amount of those.
    '''

    x_values = set() # set so no doubles, only unique
    x_values_indexs = {} # x_value: index of x_value in
    graphs = {} # y_value for each graph/dataframe
    attribute_of_value = filter_mode

    #test = set()
    
    # get each unquie value also by extracitng values from classes like datetime
    for value in dataframe[x_column]:
        try:
            #test.add(type(value))
            if type(value) == pandas.Timestamp or type(value) == datetime.datetime: # check if can extract date/times from time
                if filter_mode == "month":
                    x_values.add(int(value.month))

                elif filter_mode == "day":
                    x_values.add(int(value.day))

                elif filter_mode == "hour" and value.hour:
                    x_values.add(int(value.hour))

                elif filter_mode == "second" and value.second:
                    x_values.add(int(value.second))

                else: # year standard lookfor
                    x_values.add(int(value.year))
                    attribute_of_value = "year"

            else: # otherwise just use value as label(x_value)
                print("else")
                x_values.add(int(value))

        except: # something went wrong, the rest of function does not with without x_values
            #print(test)
            print("Creating x values failed, returnig")
            return

    x_values = list(x_values) # convert to list so matplotlib can work with it
    x_values.sort() # sort it to not mess up graphs (which go for example backwards)

    # create table to easier change the correct value with the correct index in the y_values/graphs dict
    index = 0
    for value in x_values:
        x_values_indexs[value] = index
        index += 1

    # create keys/indexs to prevent key error
    unique_values = dataframe[y_column].unique()
    for unique_value in unique_values:
        for index in x_values_indexs.values():
            try:
                graphs[unique_value][index] = 0
            except:
                graphs[unique_value] = {}
                graphs[unique_value][index] = 0

    # loop to count values   
    if attribute_of_value: # if for example it should extract year from datetime
        for index, row in dataframe.iterrows():
               graphs[row[y_column]][int(x_values_indexs[row[x_column].__getattribute__(attribute_of_value)])] += 1 # add 1 to the value which is linked to the same data value
    else: # if it should just take the value without extraction
        for index, row in dataframe.iterrows():
            graphs[row[y_column]][int(x_values_indexs[row[x_column]])] += 1 # add 1 to the value which is linked to the same data value


    for key in graphs.keys():
        graphs[key] = list(graphs[key].values()) # convert each graph to list to make it readable for matplotlib

    return [list(x_values), graphs]



def GetBars_CompareCity(dataframe: pandas.DataFrame, 
                            column: str, 
                            filter_mode: str | None = None,
                            merge: bool = False):
    '''This function counts the amount of a appearances of one value in different data frames. 
    It returns labels + sizes which fit for bar and pie charts.
    '''

    x_values = set() # set so no doubles, only unique
    x_values_indexs = {} # x_value: index of x_value in
    graphs = [] # y_value for each graph/dataframe

    #test = set()

    # get each unquie value also by extracitng values from classes like datetime
    for value in dataframe[column]:
        try:
            #test.add(type(value))
            if type(value) == pandas.Timestamp or type(value) == datetime.datetime: # check if can extract date/times from time
                if filter_mode == "month":
                    x_values.add(int(value.month))

                elif filter_mode == "day":
                    x_values.add(int(value.day))

                elif filter_mode == "hour" and value.hour:
                    x_values.add(int(value.hour))

                elif filter_mode == "second" and value.second:
                    x_values.add(int(value.second))

                else: # year standard lookfor
                    x_values.add(int(value.year))

            else: # otherwise just use value as label(x_value)
                x_values.add(value)

        except: # something went wrong, the rest of function does not with without x_values
            # print(test)
            print("Creating x values failed, returnig")
            return

    x_values = list(x_values) # convert to list so matplotlib can work with it
    x_values.sort() # sort it to not mess up graphs (which go for example backwards)

    # create table to easier change the correct value with the correct index in the y_values/graphs list
    index = 0
    for value in x_values:
        x_values_indexs[value] = index
        index += 1

    # create keys/indexs to prevent key error
    for index in x_values_indexs.values():
            graphs.insert(index,0)
                
    # loop to count values
    for value in dataframe[column].values:
        graphs[x_values_indexs[value]] += 1 # add 1 to the value which is linked to the same data value
        

    return [list(x_values), graphs]