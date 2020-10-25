import plotly_express as px
import pandas as pd

# import data
stocks_df = pd.read_csv("../data/all_stocks_5yr.csv")

print(stocks_df.head())

apple = stocks_df[stocks_df['Name'] =='AAPL']

apple_stock_plot = px.line(x='date', y='open', data_frame=apple,
                           title="Apple stock Open Prices")

apple_stock_plot.show()

