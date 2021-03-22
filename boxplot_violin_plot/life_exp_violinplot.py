import plotly.express as px
import pandas as pd

df = pd.read_csv("../data/gapminder_2007.csv")

plot = px.violin(data_frame=df,
                 x='continent',
                 y='lifeExp',
                 points='all',
                 box=True,
                 hover_name='country',
                 title="Violinplot of Life expectancy across the different continents for the 2007 year")

plot.show()