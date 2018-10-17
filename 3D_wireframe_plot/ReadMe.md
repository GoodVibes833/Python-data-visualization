# 3D wireframe plot

- python
- pandas




<<<<<<< HEAD

=======
<video src="wireframe_video.mov" />



<video controls>                                                                
    <source                                                                     
        src="/Users/jin-tak.han/code/Python_data_visualization/3D_wireframe_plot/wireframe_video.mov"
        type="video/mp4">                                                       
</video>


<video width="320" height="240" controls>
  <source src="/Users/jin-tak.han/code/Python_data_visualization/3D_wireframe_plot/wireframe_video.mov" type="video/mp4">
</video>


Video

<video src="/Users/jin-tak.han/code/Python_data_visualization/3D_wireframe_plot/wireframe_video.mov"></video>
>>>>>>> 023afc63f30d5e3c890fee129e5c6e37f27644e4


### #  plot

### ![3D_wireframe](3D_wireframe.png)





### #  code

```python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import pandas as pd


#df =  pd.read_csv('/Users/jin-tak.han/Code/Python_data_visualization/Pie_graph_basic/data_sample_pie_chart.csv')
#revenue_data = df["Revenue"]


x = [1,3,5,8,14,23,42,56]
y = [1,2,3,4,4,4,3,2]

z = np.array([[1,1,1,1,1,1,1,1],[3,4,5,6,7,8,9,10]])

figure = plt.figure()
axis = figure.add_subplot(111, projection = '3d')

axis.plot_wireframe(x, y, z)

axis.set_xlabel('x-axis')
axis.set_ylabel('y-axis')
axis.set_zlabel('z-axis')

plt.show()
```



