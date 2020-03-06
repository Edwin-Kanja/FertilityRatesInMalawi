import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

data=pd.read_csv("C:/Users/admin/Desktop/Eduuh/sample census data.csv")
data.head()

#Histogram
import matplotlib.pyplot as plt

plt.hist(data.Electricity_Units)
plt.title("Electricity units")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend('key')
plt.show()

#scatterplot
plt.scatter(data.Husband_Age, data.Wife_Age)
plt.title("Scatter Plot")
plt.xlabel('x-axis Husband age')
plt.ylabel('y-axis  Wife age')
plt.legend('key')
plt.show()

plt.bar(data.Husband_Age, data.Wife_Age)
plt.title("Lengths Bar chart")
plt.xlabel("Husband income")
plt.ylabel("wife income")
plt.show()

#fill for wife_income
data['Wife_Income'].fillna(data['Wife_Income'].mean(), inplace=True)
data.apply(lambda x:sum(x.isnull()), axis=0)

data.apply(lambda x:sum(x.isnull()), axis=0)


data.describe()
data.info()

#plot the data for the number of children and the number of bedrooms.

plt.plot(data.Number_of_Children, data.Number_of_Bedrooms)
plt.xlabel("Number_of_Children")
plt.ylabel("Number_of_Bedrooms")
plt.title(" Number_of_Children and Number_of_Bedrooms")
plt.show()

plt.pie(data.Husband_Age)
plt.show()

plt.pie(data.Number_of_Children)
plt.show()

data['Husband_Income'].var()
