import DataCollectionA
import DataProcessingA
import VisualizingA

Dataframe = DataCollectionA.getDataFrame("NY")
Dataframe = DataProcessingA.ConvertData(Dataframe, city="NY", to_convert="start_date", merge=True)
Dataframe = DataProcessingA.ConvertData(Dataframe, city="NY", to_convert="vicitm_sex", merge=True)
list_for_graph = DataProcessingA.GetBars_CompareCity(Dataframe, "vicitm_sex", filter_mode="year")
print(list_for_graph)
if list_for_graph:
    VisualizingA.CreatePieChart(list_for_graph[0], list_for_graph[1])

print(Dataframe.columns)