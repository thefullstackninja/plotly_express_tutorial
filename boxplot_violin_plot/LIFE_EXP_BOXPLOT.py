import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/gapminder_2007.csv")

print(df.head())

plot = px.box(data_frame=df,
              x='continent',
              y='lifeExp',
              title="Distribution of Life expectancy across the different continents for the 2007 year")

plot.show()