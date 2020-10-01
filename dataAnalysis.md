# Data Analysis

Data is collected everywhere around us, but data does not mean information. Data analysis (data science), helps us unlock the information and insights from raw data to answer our questions. So data analysis plays an important role by helping us to discover useful information from the data, answer questions, and even predict the future or the unknown.

## Links

- [Vocabulary](#vocabulary)
- [Importing and exporting](#importing-and-exporting)
- [Checking data](#checking-data)
- [Accessing Databases with Python](#accessing-databases-with-python)
- [Data wrangling](#data-wrangling)

## Vocabulary

**Dataset** is a file, data collection, sometimes the first row is a header, which contains columns names.

**Target value** or label in other words. Is the value that we want to predict from the dataset and the predictors should be all the other variables listed like symboling, normalized-losses, make, and so on. 

**Data acquisition** is a process of loading and reading data into notebook from various sources.

In a dataset, each row is one **Datapoint**, a large number of properties are associated with each datapoint (is like a *tuple* in RDB?).

A **DataFrame** is generally the most commonly used *Pandas* object. A 2-dimensional labeled data structure with columns of potentially different types. (like an SQL table)

**Data preprocessing**, often called data cleaning or data wrangling, is the process of converting or mapping data from one raw form into another format to make it ready for further analysis. (Indentify and handle missing values, data formatting, data normalization (centering/scaling), data binning, and turning categorical values to numeric variables.

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
## Data Wrangling

### Pre-processing Data

When no data value is stored for feature for a particular observation, we say this feature has a missing value. We can **drop missing values**(drop the variable, drop the data entry), **replace them**(with average or similar datapoints, frequency or based on other functions), **or leave the missing data as missing data**... of course, each situation is different and should be judged differently.

Before anyting, you can check if the dataset is according python types for computational speed and convenience: If Missing values come with "?" (for example) we can deal with it as follows:

```
# replace "?" to NaN
df.replace("?", np.nan, inplace = True)

#to check it: df.head(5)
#remember import numpy!!!

```

Aditionally, there are two methods to detect missing data:

.isnull()
.notnull()

```
#The output is a boolean value indicating whether the value that is passed into the argument is in fact missing data.
#"True" stands for missing value, while "False" stands for not missing value.

missing_data = df.isnull()

```

Using a for loop in Python, we can quickly figure out the number of missing values in each column. As mentioned above, "True" represents a missing value, "False" means the value is present in the dataset. In the body of the for loop the method ".value_counts()" counts the number of "True" values.

```
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")  

```

When you drop data, you could either drop the whole variable or just the single data entry with the missing value. If you don't have a lot of observations with missing data, usually dropping the particular entry is the best. If you're removing data, you want to look to do something that has the least amount of impact. Replacing data is better since no data is wasted. However, it is less accurate since we need to replace missing data with a guess of what the data should be. One standard for placement technique is to replace missing values by the average value of the entire variable. One standard for placement technique is to replace missing values by the average value of the entire variable.

But what if the values cannot be averaged as with categorical variables? For a variable like fuel type, there isn't an average fuel type since the variable values are not numbers. In this case, one possibility is to try using the mode, the most common like gasoline.

To remove data that contains missing values Panda's library has a built-in method called *dropna*, with the dropna method, you can choose to drop rows or columns that contain missing values like NaN. So you'll need to specify access equal zero to drop the rows or access equals one to drop the columns that contain the missing values.

```
# dropna method dataframes.dropna():
df.dropna(subset=["price"], axis=0, inplace=True)

```

Setting the argument in place to true, allows the modification to be done on the data set directly. In place equals true, just writes the result back into the data frame.

To replace missing values like NaNs with actual values, Pandas library has a built-in method called replace which can be used to fill in the missing values with the newly calculated values. As an example, assume that we want to replace the missing values of the variable normalized losses by the mean value of the variable. Therefore, the missing value should be replaced by the average of the entries within that column. 

```
#dataframe.replace(missing_value, new_value):

# In Python, first we calculate the mean of the column.
mean = df["normalised-losess"].mean()

#Then we use the method replace to specify the value we would like to be replaced as the first parameter, in this case NaN. The second parameter is the value we would like to replace it with i.e the mean in this example.
df["normalised-losess"].replace(np.nan, mean)

```
This is a fairly simplified way of replacing missing values.

### Formatting

Data formatting means bringing data into a common standard of expression that allows users to make meaningful comparisons. As a part of dataset cleaning, data formatting ensures the data is consistent and easily understandable.

```
#Converting "mpg" to "L/100km"
df["city-mpg"]= 235/df["city-mpg"]

#Renaming column
df.rename(columns={"city-mpg": "city-L/100Km"}, inplace=True)

```
Although the expected data type should really be an integer or float type. It is important for later analysis to explore the features data type and convert them to the correct data types. Otherwise, the developed models later on may behave strangely, and totally valid data may end up being treated like missing data.

```
#to identify data types
dataframe.dtypes()

#to convert data types and cast
dataframe.astype()

```
### Normalization

Making the ranges consistent between variables, normalization enables a fair comparison between the different features, making sure they have the same impact (It is also important for computational reasons). 

> *Example: Consider a data set containing two features, age and income. Where age ranges from 0-100, while income ranges from 0-20,000 and higher. Income is about 1,000 times larger than age and ranges from 20,000-500,000. So, these two features are in very different ranges. When we do further analysis, like linear regression for example, the attribute income will intrinsically influence the result more due to its larger value. But this doesn't necessarily mean it is more important as a predictor. So, the nature of the data biases the linear regression model to weigh income more heavily than age. To avoid this, we can normalize these two variables into values that range from zero to one.*


There are several ways to normalize data but we gonna check three of them:
![Normalization](https://github.com/silvaralth/py-stuff/blob/master/wikiImages/Normalization.svg)

The first method called **simple feature scaling** just divides each value by the maximum value for that feature. This makes the new values range between **zero and one**. The second method called **min-max** takes each value X_old subtract it from the minimum value of that feature, then divides by the range of that feature. Again, the resulting new values range between **zero and one**. The third method is called **z-score** or **standard score**. In this formula for each value you subtract the **mu (µ)** which is the **average of the feature**, and then divide by the **standard deviation sigma (σ)**. The resulting values hover **around zero**, and typically range between **negative three and positive three** but can be higher or lower.


```
#simple feature scaling
#df[column] = df[column] / df[column].max()

df["lenght"] = df["length"]/df["length"].max()

#min-max
#df[column] = ( df[column] - df[column].max() ) / ( df[column].max() - df[column].min() )

df["lenght"] = (df["length"]-df["length"].max())/
               (df["length"].max()-df["length"].min())

#z-score
#df[column] = ( df[column] - df[column].mean() ) / ( df[column].std() )

#df[column] = (df["length"]-df["length"].mean())/(df["length"].std())

``` 

In z-score, *Mean* method will return the average value of the feature in the data set, and *STD* method will return the standard deviation of the features in the data set.

### Binning

Binning is when you group values together into bins. For example, you can bin “age” into [0 to 5], [6 to 10], [11 to 15] and so on. Sometimes, binning can improve accuracy of the predictive models.

> Example: “price” here is an attribute range from 5,000 to 45,500. Using binning, we categorize the price into three bins: low price, medium price, and high prices. In the actual car dataset, ”price" is a numerical variable ranging from 5188 to 45400, it has 201 unique values. We can categorize them into 3 bins: low, medium, and high-priced cars. In Python we can easily implement the binning: We would like 3 bins of equal binwidth, so we need 4 numbers as dividers that are equal distance apart. First we use the numpy function “linspace” to return the array “bins” that contains 4 equally spaced numbers over the specified interval of the price. We create a list “group_names “ that contains the different bin names. We use the pandas function ”cut” to segment and sort the data values into bins.

```
#numpy linspace
bins = np.linspace(min(df[price]), max(df["price]), 4)

#creating a "group_names" list
group_names = ["Low", "Medium", "High"]

# Segmenting and sorting the data into bins
df["price-binned"] = pd.cut(df["price"], bins, labels=group_names, include_lowest=True )

```

Most statistical models cannot take in objects or strings as input and for model training only take the numbers as inputs. We encode the values by adding new features corresponding to each unique element in the original feature we would like to encode. This technique is often called **"One-hot encoding"**. In Pandas, we can use get_dummies method to convert categorical variables to dummy variables (0 or 1).

```
#Dummy variables
pd.get_dummies(df["column"])

```

The get_dummies method automatically generates a list of numbers, each one corresponding to a particular category of the variable.


## Exploratory Data Analysis

EDA is an approach to analyze data in order to summarize main characteristics of the data, gain better understanding of the data set, uncover relationships between different variables, and extract important variables for the problem we're trying to solve.

### Descriptive statistics

When you begin to analyze data, it's important to first explore your data before you spend time building complicated models. One easy way to do so, is to calculate some Descriptive Statistics for your data. Descriptive statistical analysis helps to describe basic features of a data set, and obtains a short summary about the sample and measures of the data.

```
df.describe()
````
Using the describe function and applying it on your data frame, the describe function automatically computes basic statistics for all numerical variables. It shows the mean, the total number of data points, the standard deviation, the quartiles and the extreme values. Any NAN values are automatically skipped in these statistics. This function will give you a clear idea of the distribution of your different variables.


```
#value_counts()
df=pd.DataFrame({'A':["a","b","a","c","a"]})
df['A'].value_counts()
```
You could have also categorical variables in your data set. These are variables that can be divided up into different categories or groups, and have discrete values. 

```
#BoxPlots
```

Box plots are a great way to visualize numeric data, since you can visualize the various distributions of the data. The main features that the box plot shows, are the median of the data, which represents where the middle data point is. The upper quartile shows where the 75th percentile is. The lower quartile shows where the 25th percentile is. The data between the upper and lower quartile represents the interquartile range. Next you have the lower and upper extremes. These are calculated as 1.5 times the interquartile range, above the 75th percentile, and as 1.5 times the IQR below the 25th percentile. Finally, box plots also display outliers as individual dots that occur outside the upper and lower extremes. With box plots, you can easily spot outliers, and also see the distribution and skewness of the data. Box plots make it easy to compare between groups.

```
#Scatter Plot

x=df[“engine-size”]
y=df[“price”]
plt.scatter(x,y)
plt.title(“Scatterplot of Engine Size vs Price”)
plt.xlabel(“Engine Size”) 
plt.ylabel(“Price”) 

```
What if we want to understand the relationship between engine size and price. Could engine size possibly predict the price of a car? One good way to visualize this is using a scatter plot. Each observation in the scatter plot is represented as a point. This plot shows the relationship between two variables. The predictor variable, is the variable that you are using to predict an outcome. In this case our predictor variable is the engine size.

## GroupBy

The group by method is used on categorical variables, groups the data into subsets according to the different categories of that variable. You can group by a single variable or you can group by multiple variables by passing in multiple variable names.

```
#Find the average "price" of each car based on "body-style" ?
df[['price','body-style']].groupby(['body-style'],as_index= False).mean()
```

To make it easier to understand, we can transform this table to a pivot table by using the pivot method. In the previous table, both drive wheels and body style were listening columns. **A pivot table has one variable displayed along the columns and the other variable displayed along the rows**. Just with one line of code and by using the Panda's pivot method, we can pivot the body style variable so it is displayed along the columns and the drive wheels will be displayed along the rows. The price data now becomes a rectangular grid, which is easier to visualize. This is similar to what is usually done in Excel spreadsheets. 

Another way to represent the pivot table is using a heat map plot. Heat map takes a rectangular grid of data and assigns a color intensity based on the data value at the grid points. It is a great way to plot the target variable over multiple variables and through this get visual clues with the relationship between these variables and the target. 

### Correlation

Correlation is a statistical metric for measuring to what extent different variables are interdependent. In other words, when we look at two variables over time, if one variable changes how does this affect change in the other variable? 
