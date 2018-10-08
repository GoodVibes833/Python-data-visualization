import matplotlib.pyplot as plt
import pandas as pd

df =  pd.read_csv('/Users/jin-tak.han/Code/Python_data_visualization/data_sample_pie_chart.csv')

country_data = df["Retailer country"]
medal_data = df["Revenue"]


#colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
          
plt.pie(medal_data, labels=country_data, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("The amount of revenues of countries")
plt.show()