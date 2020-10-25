import plotly_express as px
import pandas as pd

basic_plot = px.line(x=[1,2,3,4,5],
                     y=[2,3,4,5,6],
                     title="Basic line plots")


basic_plot.show()