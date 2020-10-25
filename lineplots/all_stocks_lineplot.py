import plotly_express as px
import pandas as pd

# import data
stocks_df = pd.read_csv("../data/all_stocks_5yr.csv")

print(stocks_df.head())

all_stock_prices = px.line(data_frame=stocks_df,
                           x='date', y='high',color='Name',
                           title="Line plot of Stock High Prices over time"
                           )

all_stock_prices.show()