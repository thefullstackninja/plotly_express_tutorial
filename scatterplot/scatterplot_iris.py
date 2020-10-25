import plotly_express as px
import pandas as pd


df = pd.read_csv("./data/iris.csv")

print(df.head())


iris_scatterplot = px.scatter(data_frame=df, x='SepalLengthCm',
                              y='SepalWidthCm',
                              color='Species',
                              title="Scatterplot of Sepal Length vs Sepal Width")

iris_scatterplot.show()