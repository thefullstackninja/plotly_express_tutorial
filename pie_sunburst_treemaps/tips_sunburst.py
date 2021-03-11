import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/tips.csv")


plot = px.sunburst(
    data_frame=df,
    path=['day','time','sex','smoker'],
    values='tip',

)

plot.show()

