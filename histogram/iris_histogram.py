import plotly_express as px
import pandas as pd

iris_df = pd.read_csv("../data/iris.csv")

print(iris_df.head())

basic_histogram = px.histogram(data_frame=iris_df, nbins=30,
                               title="Histogram plot of Sepal Length",
                               x='SepalLengthCm')

basic_histogram.show()