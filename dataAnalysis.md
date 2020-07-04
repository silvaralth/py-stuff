# Data Analysis

Data is collected everywhere around us, but data does not mean information. Data analysis (data science), helps us unlock the information and insights from raw data to answer our questions. So data analysis plays an important role by helping us to discover useful information from the data, answer questions, and even predict the future or the unknown.

## Links

- [Vocabulary](#vocabulary)
- [Importing and exporting](#importing-and-exporting)
- [Checking data](#checking-data)
- [Accessing Databases with Python](#accessing-databases-with-python)

## Vocabulary

**Dataset** is a file, data collection, sometimes the first row is a header, which contains columns names.

**Target value** or label in other words. Is the value that we want to predict from the dataset and the predictors should be all the other variables listed like symboling, normalized-losses, make, and so on. 

**Data acquisition** is a process of loading and reading data into notebook from various sources.

In a dataset, each row is one **Datapoint**, a large number of properties are associated with each datapoint (is like a *tuple* in RDB?).

A **DataFrame** is generally the most commonly used *Pandas* object. A 2-dimensional labeled data structure with columns of potentially different types. (like an SQL table)

## Importing and exporting
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
## Checking data

As we can use math functions to manipulate data, we can check the **datatypes** in a dataframe ussing **dtypes**

```
# check datatype, return the type of each column in a series
df.dtypes
```

Commonly we can check the statistical summary of each column to learn about the distribution of data (in each column). Statistical metrics can tell if are mathematical issues that may exist such as extreme outliers and large deviations to address theese issues later.

To get the quick statistics, we use the **describe** method.

```
df.describe()

# count -> number of terms
# mean -> average value
# std -> standard deviation
# min/max
```

By default, the **dataframe.describe** functions skips rows and columns that do not contain numbers. 

```
df.describe(include="all")

# unique -> the number of distinct objects in the column
# top -> most frequently occurring object
# freq -> the number of times the top object appears in the column
```

Another method to check the dataset is **df. info**, it returns the top 30 rows and bottom 30 rows o a dataframe.

## Accessing Databases with Python

An application programming interface is a set of functions that you can call to get access to some type of servers. The SQL API consists of library function calls as an application programming interface, API, for the DBMS. To pass SQL statements to the DBMS, an application program calls functions in the API, and it calls other functions to retrieve query results and status information from the DBMS.

![SQL API](https://github.com/silvaralth/py-stuff/blob/master/wikiImages/SQLAPI.svg)

To send the SQL statement to the DBMS, the program builds the statement as a text string in a buffer and then makes an API call to pass the buffer contents to the DBMS. The application program makes API calls to check the status of its DBMS request and to handle errors. 

**DB-API** is Python's standard API for accessing relational databases. It is a standard that allows you to write a single program that works with multiple kinds of relational databases instead of writing a separate program for each one. So, if you learn the DB-API functions, then you can apply that knowledge to use any database with Python.

We use **Conection Objects** to manage transactions and **Cursor Object** to make database queries:

```
# Common methods

cursor()
commit()
rollback()
close()

# DB-API example 
from dbmodule import connect

# create connection object
connection = connect('dbname','username','password')

# create a cursor object
cursor = connection.cursor()

# run queries
cursor.execute('SELECT * FROM MyTable')
results = cursor.fetchall()

# free resources
cursor.close()
connection.close()
```
