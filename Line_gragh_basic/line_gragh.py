
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/



data = pd.read_csv("/Users/jin-tak.han/Downloads/sample_data.csv")

data.set_index("Num", inplace= True)
data.head()

data.plot()
plt.show()
