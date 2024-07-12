import DataCollectionA
import DataProcessingA
import VisualizingA
import time

keys_for_analyzing = ["start_date", "crime_desc", "borough", "suspect_age", "suspect_race", "suspect_sex", "victim_age", "victim_race", "vicitm_sex", "position"]
time_types = ["start_date"]#, "end_date", "report_date"]
part_of_dates = ["year", "month", "day", "hour", "second"]

dataframes = {}
cities = ["NY", "LA"]

def collectAllData(): #collect data from all cities
    for city in cities:
        dataframes[city] = DataCollectionA.getDataFrame(city)

def ConvertAll():
    for city, dataframe in dataframes.items():
        for key in  dataframe.columns:
           if key.find("time") > 0: # to not first merge into date then again into column time (also bug prevention, due to new datatypes)
               continue
           dataframes[city] = DataProcessingA.ConvertData(dataframe, city=city, to_convert=key, merge=True)


# Start
start_time = time.time()

print(f"Starting to collect data.")

collectAllData()

print(f"Collected all data after {time.time() - start_time}, starting with data proccessing")
start_time = time.time()

ConvertAll()

print(f"Processed all data after {time.time() - start_time}")

print(f"\nHello, this program can analyze crime data from different cities. Current cities included are: " + ", ".join(cities))
print(f"You can choose if you ether want to compare data between cities or within one city.")
print(f"You can display the data in 3 different ways: graph, bar, pie, map")
print(f"You can select data from different columns: " + ", ".join(keys_for_analyzing))
print(f"From dates you can choose from: year, month, day, hour, second")

while True:
    compare_type = input("\nDo you want to analyze data within one city (1) or compare between multiple cites (2)?: ")
    if compare_type == "":
        break

    try:
        compare_type = int(compare_type)
    except:
        print("Not a valid number")
        continue

    if not compare_type in range(1,3):
        print("Not a valid number")
        continue

    if compare_type == 1:
        city = input("Which city do you want to analyze the data from?: ")
        if not city in cities:
            print("city not valid")
            continue


        graph_type = input("How do you want to display the data?: ")

        if not graph_type in ["graph", "pie", "bar", "map"]:
            print("Not a valid number")
            continue

        
        if graph_type == "graph":
            y_column = input("Which coloumn do you want to choose for the y values: ")
            if not y_column in keys_for_analyzing:
                print("Not valid key")
                continue
        
            x_column = input("Which coloumn do you want to choose for the x values: ")
            if not x_column in keys_for_analyzing or x_column == y_column:
                print("Not valid key")
                continue
            if not x_column in time_types:
                print("A number type is needed for x axis for graphs")
                continue
            

            date_spec = input("Which value do you want to choose from the date?: ")
            if not date_spec in part_of_dates:
                date_spec = None
            
            result = DataProcessingA.GetGraph_CompareCity(dataframes[city], x_column, y_column, date_spec)
            if result:
                VisualizingA.CreateGraph(result[0], result[1])
            else:
                continue

        elif graph_type == "bar":
            column = input("Which coloumn do you want to choose for the values: ")
            if not column in keys_for_analyzing:
                print("Not valid key")
                continue

            date_spec = None
            if column in time_types:
                date_spec = input("Which value do you want to choose from the date?: ")
                if not date_spec in part_of_dates:
                    date_spec = None
            
            
            result = DataProcessingA.GetBars_CompareCity(dataframes[city], column, date_spec)
            if result:
                VisualizingA.CreateBars(result[0], result[1])
            else:
                continue

        elif graph_type == "pie":
            column = input("Which coloumn do you want to choose for the values: ")
            if not column in keys_for_analyzing:
                print("Not valid key")
                continue

            date_spec = None
            if column in time_types:
                date_spec = input("Which value do you want to choose from the date?: ")
                if not date_spec in part_of_dates:
                    date_spec = None
            
            
            result = DataProcessingA.GetBars_CompareCity(dataframes[city], column, date_spec)
            if result:
                VisualizingA.CreatePieChart(result[0], result[1])
            else:
                continue

        elif graph_type == "map":
            print("Not avaible atm")

    else:
            print("All cities are choosen and only graph is avaiable as option.")
            y_column = input("Which coloumn do you want to choose for the y values: ")
            y_spec = None
            if not y_column in keys_for_analyzing:
                y_column = None
            else:
                y_spec = input("Which coloumn do you want to look for a certain y value?: ")
                if y_spec == "":
                    y_spec = None
        
            x_column = input("Which coloumn do you want to choose for the x values: ")
            if not x_column in keys_for_analyzing or x_column == y_column:
                print("Not valid key")
                continue
            if not x_column in time_types:
                print("A number type is needed for x axis for graphs")
                continue
            

            date_spec = input("Which value do you want to choose from the date?: ")
            if not date_spec in part_of_dates:
                date_spec = None
            
            result = DataProcessingA.GetGraph_CompareCities(dataframes, x_column, y_column, y_spec, date_spec)
            if result:
                VisualizingA.CreateGraph(result[0], result[1])
            else:
                continue
