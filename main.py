import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv('apple_products.csv')
print(data.head())
print(data.isnull().sum())
print(data.describe())

# 1 Top 10 highest rated IPhones on flipkart

highest_rated=data.sort_values(by=['Star Rating'], ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])

# 2 How many rating do the highest rated IPhone

iphones=highest_rated['Product Name'].value_counts()
label=iphones.index
counts=highest_rated['Number Of Ratings']
figure=px.bar(highest_rated,x=label,y=counts)
figure.show()

# 3 which IPhone has the highest number of review on flipkart

highest_review=data.sort_values(by=['Number Of Reviews'], ascending=False)

iphones=highest_rated['Product Name'].value_counts()
label=iphones.index
counts=highest_rated['Number Of Reviews']
figure=px.bar(highest_rated,x=label,y=counts,title='Number of Highest Reviews')
figure.show()


# 4  What is the realtioship b/w the sale price of IPhones & no. of rating on flipkart
figure = px.scatter(data_frame=data, 
                    x="Number Of Ratings", 
                    y="Sale Price",
                    size="Discount Percentage", 
                    trendline='ols', 
                    title='Relationship Between Sale Price & Number of Ratings')
figure.show()

# 5 What is the realtioship b/w the Discount Percentage and Number of Ratings of IPhone on flipkart

figure = px.scatter(data_frame=data, 
                    x="Discount Percentage", 
                    y="Number Of Ratings",
                    size="Sale Price", 
                    trendline='ols', 
                    title='Relationship Between Discount Percentage & Number of Ratings')
figure.show()

# 6 Most Expensive and Least Expensive

most_expensive=data.loc[data['Sale Price'].idxmax()]
least_expensive=data.loc[data['Sale Price'].idxmin()]

print("Most Expensive Products : ")
print(most_expensive)
print("Least Expensive Products : ")
print(least_expensive)