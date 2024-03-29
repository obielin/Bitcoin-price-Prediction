# -*- coding: utf-8 -*-
"""Bitcoin price prediction.ipynb
"""

from google.colab import files
uploaded = files.upload()

#import json

# Assuming your JSON file is named 'cryptocurrency_data.json'
#with open('CurrencyJSONDataSet.json') as f:
 #   df = json.load(f)

import pandas as pd
import seaborn as sns
import datetime as dt
from plotly.express import histogram, density_contour
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from itertools import cycle

df = pd.read_csv('coin_Bitcoin.csv')
# Convert JSON data to DataFrame
#df = pd.DataFrame(df)

print(df.head())

#Understand the shape of dataset
df.shape

#Get general info about the dataset
df.info()

#check for missing values in the dataframe
df.isna().sum()

#Creation of a variable for predicting '5' days out into the future
projection_Bitcoin = 5
#creation of a new column with a name prediction
df['Prediction'] = df[['Close']].shift(-projection_Bitcoin)
df

# Summary statistics
print(df.describe())

"""histograms plots for numerical columns like Price and to understand their distribution (normal, skewed, etc.)"""

# Interactive histogram for Price
fig_hist_price = histogram(df, x="Prediction", title="Price Distribution")
fig_hist_price.update_layout(xaxis_title="Price", yaxis_title="Count")
fig_hist_price.show()

# Interactive histogram for Price
fig_hist_volume = histogram(df, x="Volume", title="Volume Distribution")
fig_hist_volume.update_layout(xaxis_title="Volume", yaxis_title="Count")
fig_hist_volume.show()

# Interactive histogram for Price
fig_hist_high = histogram(df, x="High", title="High Distribution")
fig_hist_high.update_layout(xaxis_title="High", yaxis_title="Count")
fig_hist_high.show()

# Interactive histogram for Price
fig_hist_Low = histogram(df, x="Low", title="Low Distribution")
fig_hist_Low.update_layout(xaxis_title="Low", yaxis_title="Count")
fig_hist_Low.show()

visualize_Bitcoin = cycle(['Open','Close','High','Low','Prediction'])

fig = px.line(df, x=df.Date, y=[df['Open'], df['Close'],
                                          df['High'], df['Low'],df['Prediction']],
             labels={'Date': 'Date','value':'Price'})
fig.update_layout(title_text='Bitcoin', font_size=15, font_color='black',legend_title_text='Parameters')
fig.for_each_trace(lambda t:  t.update(name = next(visualize_Bitcoin)))
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()

"""Area chart for daily prices"""

area = px.area(data_frame = df ,
               y = "Prediction",
               x="Date",
               title = 'Bitcoin (BTC) Daily Price')

area.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

area.update_yaxes(title_text = 'Price in USD', ticksuffix = '$')
area.update_layout(showlegend = True,
    title = {
        'text': 'Bitcoin(BTC) Daily Price (2013-Present)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        template="plotly_white")

area.show()

"""Time series plots using Candlestick Chart"""

candle_stick = go.Figure(data = [go.Candlestick(x =df["Date"],
                                               open = df[('Open')],
                                               high = df[('High')],
                                               low = df[('Low')],
                                               close = df[('Prediction')])])
candle_stick.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

candle_stick.update_layout(
    title = {
        'text': 'Bitcoin(BTC) Daily Price(2013-Present) Candelstick Chart',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        template="plotly_white")

candle_stick.update_yaxes(title_text = 'Price in USD', ticksuffix = '$')
candle_stick.show()

ohlc_chart = go.Figure(data = [go.Ohlc(x = df["Date"],
                                               open = df[('Open')],
                                               high = df[('High')],
                                               low = df[('Low')],
                                               close = df[('Prediction')])])

ohlc_chart.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

ohlc_chart.update_layout(
    title = {
        'text': 'Bitcoin(BTC) Daily Price(2013-Present) OHLC Chart',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        template="plotly_white")
ohlc_chart.update_yaxes(title_text = 'Price in USD', ticksuffix = '$')
ohlc_chart.show()

"""Daily Percentage Change"""

line = px.line(data_frame=df,
               x = "Date" ,
               y="Marketcap",
               title = 'Bitcoin (BTC) Market Cap(2010-Present)')

line.update_xaxes(
    title_text = 'Date',
    rangeslider_visible = True,
    rangeselector = dict(
        buttons = list([
            dict(count = 1, label = '1M', step = 'month', stepmode = 'backward'),
            dict(count = 6, label = '6M', step = 'month', stepmode = 'backward'),
            dict(count = 1, label = 'YTD', step = 'year', stepmode = 'todate'),
            dict(count = 1, label = '1Y', step = 'year', stepmode = 'backward'),
            dict(step = 'all')])))

line.update_yaxes(title_text = 'Perctange Change', ticksuffix = '%')
line.update_layout(showlegend = True,
    title = {
        'text': 'Bitcoin (BTC) Daily Percentage Change(2013-Present)',
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        template="plotly_white")

line.show()

"""### Correlation matrix:
- Calculate the correlation matrix using df.corr() to identify potential relationships between different features.
- Visualize the correlation using a heatmap to see which features move together.
"""

# Calculate correlation matrix
corr_matrix = df.corr()

# Create a heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Cryptocurrency Features')
plt.show()

"""Price Prediction"""

import numpy as np
#Creation of the independent data set (X)
X_df = np.array(df[['Close']])
X_df = X_df[:-projection_Bitcoin]
print(X_df)

#creation of the dependent data set (y)
y_df = df['Prediction'].values
y_df= y_df[:-projection_Bitcoin]
print(y_df)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X_df,y_df,test_size=0.20)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Initialize models
linear_reg_model = LinearRegression()
random_forest_model = RandomForestRegressor()
svr_model = SVR()

# Train models
linear_reg_model.fit(x_train, y_train)
random_forest_model.fit(x_train, y_train)
svr_model.fit(x_train, y_train)

# Predictions
linear_reg_preds = linear_reg_model.predict(x_test)
random_forest_preds = random_forest_model.predict(x_test)
svr_preds = svr_model.predict(x_test)

# Evaluate models
linear_reg_mse = mean_squared_error(y_test, linear_reg_preds)
random_forest_mse = mean_squared_error(y_test, random_forest_preds)
svr_mse = mean_squared_error(y_test, svr_preds)

print("Linear Regression MSE:", linear_reg_mse)
print("Random Forest MSE:", random_forest_mse)
print("SVR MSE:", svr_mse)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

# Assume you have already defined X_df and y_df

# Step 1: Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(X_df, y_df, test_size=0.20)

# Step 2: Train the models
linear_reg_model = LinearRegression()
random_forest_model = RandomForestRegressor()

linear_reg_model.fit(x_train, y_train)
random_forest_model.fit(x_train, y_train)

# Step 3: Evaluate the models
linear_reg_score = linear_reg_model.score(x_test, y_test)
random_forest_score = random_forest_model.score(x_test, y_test)

print("Linear Regression R-squared:", linear_reg_score)
print("Random Forest R-squared:", random_forest_score)

x_projection_Bitcoin = np.array(df[['Close']])[-projection_Bitcoin:]
print(x_projection_Bitcoin)

linReg_prediction_Bitcoin = linear_reg_model.predict(x_projection_Bitcoin)
print(linReg_prediction_Bitcoin)

Randforest_prediction_Bitcoin = random_forest_model.predict(x_projection_Bitcoin)
print(Randforest_prediction_Bitcoin)

from sklearn.metrics import mean_squared_error
import numpy as np

# Assuming you have already made predictions
#linReg_predictions = linear_reg_model.predict(x_test)
#randForest_predictions = random_forest_model.predict(x_test)

# Calculate RMSE for Linear Regression
linReg_rmse = np.sqrt(mean_squared_error(x_projection_Bitcoin, linReg_prediction_Bitcoin))
print("Linear Regression RMSE:", linReg_rmse)

# Calculate RMSE for Random Forest
randForest_rmse = np.sqrt(mean_squared_error(x_projection_Bitcoin, Randforest_prediction_Bitcoin))
print("Random Forest RMSE:", randForest_rmse)
