# plot data which are extracted from the process.py file.
import numpy as np
import matplotlib.pyplot as plt  # enable when need to save the 3d plots
import plotly.graph_objects as go
from mpl_toolkits.mplot3d import Axes3D
# from plot_3donion import plotonion

# import plotly.io as pio  # enable when need to save the 3d plots
def plot3d_yeastSegmentdata(data,saved_plt_filename):
    print(" ------- please wait --plotting --------")
    array_3d = data  #  have 3D numpy array with shape (201, 201, 201)
    # Create a 3D meshgrid
    x, y, z = np.meshgrid(np.arange(array_3d.shape[0]), np.arange(array_3d.shape[1]), np.arange(array_3d.shape[2]))
    print("size of the given data : array_3d : ",array_3d.shape)
    # Get the values and coordinates for the points with values greater than 0
    # x_vals = x[array_3d > 0].flatten()
    # y_vals = y[array_3d > 0].flatten()
    # z_vals = z[array_3d > 0].flatten()
    # values = array_3d[array_3d > 0].flatten()

    x_vals = x[array_3d > 0].flatten()
    y_vals = y[array_3d > 0].flatten()
    z_vals = z[array_3d > 0].flatten()
    values = array_3d[array_3d > 0].flatten()
#     custom_colormap = np.where(array_3d > 0, 'red', 'blue')
    # Create a 3D scatter plot
    fig = go.Figure(data=go.Scatter3d(
        x=x_vals,
        y=y_vals,
        z=z_vals,
        mode='markers',
        marker=dict(
            size=1,
            color=values,
            colorscale='Viridis',
            opacity=0.5

        )
    ))

    # Set labels for each axis
    fig.update_layout(scene=dict(
    xaxis_title=' ',
    yaxis_title=' ',
    zaxis_title=' ',
    xaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    yaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    zaxis=dict(
        showgrid=False,
        zeroline=False,
        showline=False,
        showticklabels=False,
    ),
    aspectmode = 'auto',    
    ))
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
#     fig.update_layout(scene=dict(bgcolor='white'))
    fig.update_layout(scene=dict(bgcolor='rgba(255,255,255,0)'))

    # Set isometric view
    fig.update_layout(scene_camera=dict(
    center=dict(x=0, y=0, z=0),
    eye=dict(x=6.5, y=1.5, z=1.5)
    ))
# # these lines for the plot saving and filename as given in the argument of the plot function. want 
# #  want to see the plot then uncomment the back
# #     filename1 = plot_savefilename+'.png'
# #     print(filename1)
# # #   plt.tight_layout()
# #     pio.write_image(fig,filename1,format='png', width=600, height=400,scale=5)
# # #     plt.savefig(filename1, dpi=400, bbox_inches='tight')
# #     # Show the interactive plot
    fig.show()

if __name__=="__main__":
    def euclidain_dist(coord,center):
        return np.sqrt(np.sum((coord-center)**2,axis =-1))
        
    upsize =  50
    forbreak = upsize
    count = 0 # for counting the loops
    sep_figure_window = int(input("do you want each figure in seperate window press 1 otherwise 0:"))
    # sep_figure_window = 0
    
    fig = plt.figure()   # this is to hold all the figure which will be generate in the for loop 
    
    for isize in range(upsize,2,-10):
        count = count+1

        data = np.random.rand(upsize,upsize,upsize)  # ctrl+f2
        # print(data,end='\t')
    # if (upsize > forbreak ):
        filenamedata = 'file'+str(isize)
        maxx= data.shape[0] -1
        maxy= data.shape[1] -1
        maxz= data.shape[2] -1
        # center = (maxx/2,maxy/2,maxz/2)
        print("xmax:",end=' ') 
        print(maxx,end=' ')
        shape = data.shape  # Adjust the shape as needed
        arr_dist = np.zeros(shape)
        arr_sliceZ  = np.zeros_like(data)

        center = np.array([maxx/2,maxy/2,maxz/2])   # Define the center
        # radious = np.sqrt(center-)**2
        radious = (isize-1)/2 ;
        print("centre x coordinate isize value:\t",center[0], isize)
        # if (isize < center[0]):
        #     break
        print("centre and  radious and shape",end='') 
        print(center,end='\t ')
        print(radious,end=' \t')
        print(shape,end=' \t')
        print("new arary shape :\t",arr_dist.shape)
        # def euclidain_dist(coord,center):
            # Populate the array with distances
        for i in range(shape[0]):
            for j in range(shape[1]):
                for k in range(shape[2]):
                    coord = np.array([i, j, k])
                    distance = euclidain_dist(coord, center)
                    arr_dist[i, j, k] = distance
                    arr_sliceZ[i,j,k] =k

        data[(arr_dist>radious) | (arr_dist<=(radious-1)) ] = 0
        # data[arr_dist>radious ] = 0
        # data[(arr_dist >radious) | (arr_dist > radious-0.7)] = 0
        # print("\n after the threshold \t radious \t ",radious,arr_dist)
        # data[arr_sliceZ> (30+count)] = 0
        # plotonion(data,upsize,count)
        if sep_figure_window ==1:
            if count !=1:
                fig= plt.figure()
            ax = fig.add_subplot(111,projection='3d')
        else:
            ax = fig.add_subplot(2,3,count,projection='3d')  # define for subplot 2,2

        ax = plotonion(data,upsize, count,sep_figure_window,ax)
    plt.tight_layout()
    plt.show()
        # plot3d_yeastSegmentdata(data,filenamedata)
    









 # <------------------ this is to understand the np.meshgrid() --------------> 
# import numpy as np
# # x=range(2)
# # y= range(2)
# x,y =np.meshgrid(np.arange(3),np.arange(2))
# print(x)
# print(y)
# x1 = [[1,2,4],[9,8,7]]
# x1=np.array(x1)
# print(x1)
# print(x1.flatten()) 
# the output of these lines: -------------------------><------------->
#
# [[0 1 2]
#  [0 1 2]]
# [[0 0 0]
#  [1 1 1]]
# [[1 2 4]
#  [9 8 7]]
# [1 2 4 9 8 7]   <------------ x1.flatten() result