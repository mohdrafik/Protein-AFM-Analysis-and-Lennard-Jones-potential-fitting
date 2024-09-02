
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_data(data, label=None,color=None, marker=None, markersize=None, alpha=None,title=None, Xaxis=None, Yaxis=None, subplot=None):
    """
    Plot data from different formats (DataFrame, NumPy array, list, tuple).

    Parameters:
        data: DataFrame, NumPy array, list, or tuple
            The data to be plotted.
        x: str, optional
            The column name for the x-axis (if data is DataFrame).
        y: str or int, optional
            The column name or index for the y-axis (if data is DataFrame or 2D NumPy array).
        title: str, optional
            The title of the plot.
        subplot: tuple, optional
            Specifies the layout of subplots (rows, columns, index).

    Returns:
        fig, ax: matplotlib.figure.Figure, matplotlib.axes.Axes
            The figure and axes objects created by Matplotlib.
    """
    if isinstance(data, pd.DataFrame):
        columns_name = data.columns # return the list of the column name. 
        if len(columns_name) == 1:
            x_data = np.arange(len(data))
            y_data = data[columns_name[0]]
        elif len(columns_name) == 2:
            x_data = data[columns_name[0]]
            y_data = data[columns_name[1]]
            
        elif len(columns_name) > 2:
            print(columns_name)
            x_columns_name = columns_name[int(input("enter Index: start from 0 for column_name list for XAxis  :"))]           
            y_columns_name = columns_name[int(input("enter Index: start from 0 for column_name list for YAxis  :"))]          
               
            x_data = data[x_columns_name]
            y_data = data[y_columns_name]
        else:
            raise ValueError("Both 'x' and 'y' must be specified when data is a DataFrame.")
        
    elif isinstance(data, np.ndarray):
        if data.ndim == 1:
            x_data = np.arange(len(data))
            y_data = data
        elif data.ndim == 2:
            row = data.shape[0]
            col = data.shape[1]
            if row >= col :
                x_data = data[:,0]
                y_data = data[:,1]
            else: 
                x_data = data[0,:]
                y_data = data[1,:]
        else:
            raise ValueError("Only 1D or 2D NumPy arrays are supported.")
        

    elif isinstance(data, (list, tuple)):
        x_data = np.arange(len(data))
        y_data = data
    else:
        raise ValueError("Unsupported data format. Supported formats: DataFrame, NumPy array, list, tuple.")


    if subplot is not None:
        rows, cols, index = subplot
        fig, ax = plt.subplots(rows, cols, figsize=(10, 6))
        ax = ax.flatten()
        ax[index].plot(x_data, y_data,label=label,color=color,marker=marker,markersize=markersize,alpha=alpha)
        # plt.show()
        ax.grid()
        ax.legend()
    else:
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_data, y_data,label=label,color=color,marker=marker,markersize=markersize,alpha=alpha)
        ax.grid()
        ax.legend()

    ax.set_xlabel(Xaxis)
    ax.set_ylabel(Yaxis)
    # ax.grid()
    # ax.legend()
    if title is not None:
        ax.set_title(title)
        # ax.grid()
        # ax.legend()
    # plt.show()

    return fig, ax

if __name__ =="__main__":
        
    df = pd.DataFrame({'X': np.arange(10), 'Y': np.random.randn(10)})
    array_data = np.random.randint(1,10,size=(10,2))

    # list_data = [1, 2, 3, 4, 5]
    # tuple_data = (1, 2, 3, 4, 5)

    # Plot DataFrame
    fig, ax = plot_data(df,label='amp', color='blue', marker='o', markersize=5, alpha=0.8, Xaxis='X', Yaxis='Y', title='DataFrame Plot',subplot=None)
    # plt.show()

    # Plot NumPy array
    fig, ax = plot_data(array_data,label='dataArray', color='red', marker='s', markersize=6, alpha=0.5, Xaxis='x1data',Yaxis='y1data',title='NumPy Array Plot',subplot=None)
    # plt.show()
    # # Plot list
    # fig, ax = plot_data(list_data, title='List Plot'

    # # Plot tuple
    # fig, ax = plot_data(tuple_data, title='Tuple Plot')

    plt.show()
