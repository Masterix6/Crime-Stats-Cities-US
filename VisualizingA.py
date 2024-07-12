import matplotlib.pyplot as plt

def CreateGraph(x_values: list, graphs: dict, legend=None, colors=None, title=None): #[list]
    '''Creates and shows multiple graph with matplotlib.
    '''
    if title:
        plt.title(title)

    for key, each_graph in graphs.items():
        #print(each_graph)
        #print(type(each_graph))
        plt.plot(x_values, each_graph, label=key)
        
    plt.xticks(x_values)
    plt.legend()
    plt.show()


def CreateBars(x_values: list, y_values: list, legend=None, colors=None, title=None):
    '''Creates and shows multiple bars with matplotlib.
    '''
    if title:
        plt.title(title)
   
    plt.bar(x_values, y_values)
    plt.show()

def CreatePieChart(labels: list, sizes: list, legend=None, colors=None, title=None):
    '''Creates and shows pie chat with matplotlib.
    '''
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)
    plt.show()

