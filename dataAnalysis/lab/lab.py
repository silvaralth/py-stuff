# Lab1 - @Silvaralth

import pandas as pd

# originalPath = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"

df = pd.read_csv(other_path, header=None)

# --- Q1 --- check the bottom 10 rows of data frame "df".
df.tail(10)

# To better describe our data we can introduce a header, this information is available at: https://archive.ics.uci.edu/ml/datasets/Automobile
# create headers list
headers = [ "symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
            "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
            "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
            "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
df.head(10)

# we can drop missing values along the column "price" as follows
df.dropna(subset=["price"], axis=0)

# --- Q2 --- Find the name of the columns of the dataframe
print(df.dtypes)

# --- Q3 --- Apply the method to ".describe()" to the columns 'length' and 'compression-ratio'.
df[['length','compression-ratio']].describe()

# look at the info of "df"
df.info