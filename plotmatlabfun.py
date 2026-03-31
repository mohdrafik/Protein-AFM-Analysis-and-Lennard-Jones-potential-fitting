import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_data(data, label=None, color=None, marker=None, markersize=None, alpha=None, title=None, Xaxis=None, Yaxis=None, ax=None, subplot=None):
    """
    Plot data from different formats (DataFrame, NumPy array, list, tuple).
    Generates a high-quality "research paper style" compact IEEE standard plot.
    """
    if isinstance(data, pd.DataFrame):
        columns_name = data.columns 
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

    # High quality styling base parameter settings - IEEE standard
    plt.rcParams.update({
        'font.family': 'serif', 
        'font.serif': ['Times New Roman', 'DejaVu Serif'],
        'font.size': 9,           # IEEE typically uses 8-10pt font
        'axes.labelsize': 10,
        'axes.titlesize': 10,
        'xtick.labelsize': 9,
        'ytick.labelsize': 9,
        'legend.fontsize': 8,
    })

    if ax is None:
        if subplot is not None:
            rows, cols, index = subplot
            fig, axes = plt.subplots(rows, cols, figsize=(7.16, 3)) # IEEE full width
            ax = axes.flatten()[index]
        else:
            fig, ax = plt.subplots(figsize=(3.5, 2.5)) # IEEE single column width
            
    # Draw plot with appropriate linewidth for IEEE
    line_kws = {'label': label, 'color': color, 'alpha': alpha, 'linewidth': 1.0}
    if marker:
        line_kws.update({'marker': marker, 'markersize': markersize if markersize else 3})
    ax.plot(x_data, y_data, **line_kws)

    # Styling Axis
    if Xaxis:
        ax.set_xlabel(Xaxis, fontweight='bold')
    if Yaxis:
        ax.set_ylabel(Yaxis, fontweight='bold')
    if title:
        ax.set_title(title, fontweight='bold')
        
    # Standard spines and ticks for compact prints
    for spine in ax.spines.values():
        spine.set_linewidth(0.8)
    ax.tick_params(axis='both', which='major', width=0.8, length=4)
    
    # Very light grid
    ax.grid(color='#e0e0e0', linestyle='--', linewidth=0.5, alpha=0.6)
    
    if label:
        ax.legend(loc='best', frameon=True, edgecolor='#cccccc', framealpha=0.9)

    return ax.figure, ax

if __name__ =="__main__":
    df = pd.DataFrame({'X': np.arange(10), 'Y': np.random.randn(10)})
    array_data = np.random.randint(1,10,size=(10,2))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.16, 3))
    plot_data(df, label='amp', color='navy', marker='o', alpha=0.8, Xaxis='X', Yaxis='Y', title='DataFrame Plot', ax=ax1)
    plot_data(array_data, label='dataArray', color='darkred', marker='s', alpha=0.5, Xaxis='x1data', Yaxis='y1data', title='NumPy Array Plot', ax=ax2)
    plt.tight_layout()
    plt.show()
