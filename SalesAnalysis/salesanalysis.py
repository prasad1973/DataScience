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

print('--Sales by Group--')
groupeddata = dataframe.copy().groupby(['Group'])
max = 0
maxstr = ""
min = float('inf')
minstr = ""
for group, subdf in groupeddata:
    print("-------------------------")
    print(str(group[0]) + ": " + str(subdf['Sales'].sum()))
    if int(subdf['Sales'].sum()) > max:
        max = int(subdf['Sales'].sum())
        maxstr = str(group[0])
    if int(subdf['Sales'].sum()) < min:
        min = int(subdf['Sales'].sum())
        minstr = str(group[0])

print('Most sales made in group: ' + maxstr)
print('Least sales made in group: ' + minstr)


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