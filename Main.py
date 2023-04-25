import pandas as pd
from sklearn.linear_model import LinearRegression
import time as t
print('Hi, I can predict future price of Iphone')
print()
t.sleep(2)
i_model = int(input('Enter The Future Model Number of Iphone:- '))
data = pd.read_csv("D:\\Rigved\\Python2\\Machine Learning\\Iphone Price Prediction\\Iphone_price.csv")

model = LinearRegression()
model.fit(data[['version']], data[['price']])



pred = int(model.predict([[i_model]])) 
print(f'Price of Iphone {i_model} would be Rupees {pred}')
