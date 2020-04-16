# Data Analysis

Data is collected everywhere around us, but data does not mean information. Data analysis (data science), helps us unlock the information and insights from raw data to answer our questions. So data analysis plays an important role by helping us to discover useful information from the data, answer questions, and even predict the future or the unknown.

These are my notes from the IA Specialization to begin looking into some basic insights from the data.

## Vocabulary:

**Dataset** is a file, data collection, sometimes the first row is a header, which contains columns names.

**Target value** or label in other words. Is the value that we want to predict from the dataset and the predictors should be all the other variables listed like symboling, normalized-losses, make, and so on. 

**Data acquisition** is a process of loading and reading data into notebook from various sources.

In a dataset, each row is one **Datapoint**, a large number of properties are associated with each datapoint (is like a *tuple* in RDB?).

A **DataFrame** is generally the most commonly used *Pandas* object. A 2-dimensional labeled data structure with columns of potentially different types. (like an SQL table)

## Importing and exporting:
``` 
import pandas as pd

url = "https://domain.tld/file.data"

# if csv has head
df = pd.read_csv(url)
# is none
df = pd.read_csv(url, header = None)

# print all the dataframe
df 

# print the first n rows
df.head(n)

# print the bottom n rows
df.tail(n)

# add column names if the dataset hasnt any
headers = ["One","Two",...]
df.columns = headers

# preserving changes to a local file
path = /home/pystuff/fileToSave.csv
df.to_csv(path)

# we can read or save in _csv() _sql() _json() _excel()
# ex.
pd.read_sql(url)
df.to_sql(path)

```
