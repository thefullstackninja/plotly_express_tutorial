import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/ks-projects-201801.csv")


# select only rows funded by usd
df_usd = df[df['currency']=='USD']

plot = px.treemap(
    data_frame=df_usd,
    values='pledged',
    path=['main_category', 'category'],
    color='goal'
)

plot.show()