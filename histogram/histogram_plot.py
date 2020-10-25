import plotly_express as px
import pandas as pd

iris_df = pd.read_csv("../data/iris.csv")

print(iris_df.head())
print('')


hist_plot_by_specie = px.histogram(data_frame=iris_df, nbins=30,
                                   x='SepalLengthCm',
                                   color='Species',
                                   title="Histogram plot of Sepal Length",
                                   histnorm='probability density')

hist_plot_by_specie.show()