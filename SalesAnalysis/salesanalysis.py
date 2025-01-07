import pandas as pd
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt



def dfminmax(dataframe, columns):
    for column in columns:
        min = dataframe[column].min()
        max = dataframe[column].max()
        dataframe[column] = (dataframe[column] - min)/(max - min)

dataframe = pd.read_csv("./SalesAnalysis/AusApparalSales4thQrt2020.csv", parse_dates=["Date"])

dataframe.head()

print(dataframe.isna().sum()) #Check for null values


dataframe.dropna() #Data Cleaning

scaleddata = dataframe.copy()
scaler = preprocessing.MinMaxScaler()
dfminmax(scaleddata, ['Unit', 'Sales']) #Data Scaling


print('--Sales by State and Group--')
groupeddata = dataframe.copy().groupby(['State', 'Group'])
print(groupeddata['Sales'].sum())


print(f'Mean: {dataframe[['Sales', 'Unit']].mean()}')
print(f'Median: {dataframe[['Sales', 'Unit']].median()}')
print(f'Mode: {dataframe[['Sales', 'Unit']].mode()}')
print(f'Standard Deviation: {dataframe[['Sales', 'Unit']].std()}')


g = dataframe.groupby(['State', 'Group'])['Sales'].sum().reset_index()

plt.figure(figsize=(10, 6))

sns.barplot(x='State', y='Sales', hue='Group', data=g)

plt.title('Sales Sum by State and Group', fontsize=14)
plt.xlabel('State', fontsize=12)
plt.ylabel('Total Sales', fontsize=12)

plt.show()