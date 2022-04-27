# import pandas
import pandas as pd
dataset = {
    'fruits': ["apple", "banana", "kiwi"],
    'quantities in kg': [1, 2, 3]
}
x = pd.DataFrame(dataset)
print(x)

# Checking Pandas Version
import pandas as pd
print(pd.__version__)

# Create a simple Pandas Series from a list:
import pandas as pd
x = [2, 3, 5, 8, 6]
y = pd.Series(x)
print(y)

# Labels
import pandas as pd
x = [2, 3, 5, 8, 6]
y = pd.Series(x)
print(y[2])

"""
Create Labels
With the index argument, you can name your own labels.
"""
import pandas as pd
x = [2, 3, 5, 8, 6]
y = pd.Series(x, index=["a","b", "c", "d", "e"])
print(y)
print(y["c"])

# Key/Value Objects as Series
import pandas as pd
fruits = {"apple": 1, "orange": 3, "kiwi": 5}
y = pd.Series(fruits)
print(y)

# Series is like a column, a DataFrame is the whole table.
import pandas as pd
dataset = {
    'fruits': ["apple", "banana", "kiwi"],
    'quantities in kg': [1, 2, 3]
}
x = pd.DataFrame(dataset)
print(x)

# Locate Row
import pandas as pd
dataset = {
    'fruits': ["apple", "banana", "kiwi"],
    'quantities in kg': [1, 2, 3]
}
x = pd.DataFrame(dataset)
print(x.loc[0])
#use a list of indexes:
print(x.loc[[0, 1]])

# Named Indexes
import pandas as pd
dataset = {
    'fruits': ["apple", "banana", "kiwi"],
    'quantities in kg': [1, 2, 3]
}
x = pd.DataFrame(dataset, index=["a", "b", "c"]) # With the index argument, you can name your own indexes.
print(x)

# Read CSV Files
# Print the DataFrame without the to_string() method:
# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:
import pandas as pd
df = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\test.csv")
print(df)

# use to_string() to print the entire DataFrame.
import pandas as pd
df = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\test.csv")
print(df.to_string())

# Check the number of maximum returned rows:
# by using pd.options.display.max_rows statement.
import pandas as pd
print(pd.options.display.max_rows)

"""
If your JSON code is not in a file, but in a Python Dictionary, 
you can load it into a DataFrame directly:
"""
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df)

# Analyzing DataFrames by using head()
# Note: if the number of rows is not specified, the head() method will return the top 5 rows.
import pandas as pd
df = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\test.csv")
print(df.head(20))
print(df.head())
print(df.tail())

# Info About the Data
print(df.info())

# Cleaning Data
# By default, the dropna() method returns a new DataFrame, and will not change the original.
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
newdata = data.dropna()
print(newdata.to_string())

# If you want to change the original DataFrame, use the inplace = True argument:
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
data.dropna(inplace=True)
print(data.to_string())

# Replace Empty Values
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
data.fillna(150, inplace=True)
print(data.to_string())

# Cleaning Data of Wrong Format
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
data["Date"] = pd.to_datetime(data["Date"])
print(data.to_string())

# Fixing Wrong Data
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
data.loc[7, "Duration"] = 45
print(data.to_string())

# If the value is higher than 120, set it to 120:
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
for x in data.index:
  if data.loc[x, "Duration"] > 120:
    data.loc[x, "Duration"] = 120
print(data.to_string())

# Removing Duplicates
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
print(data.duplicated())

# To remove duplicates, use the drop_duplicates() method.
import pandas as pd
data = pd.read_csv("C:\\Users\\PRAVEEN\\Downloads\\csv\\dirtydata.csv")
data.drop_duplicates(inplace=True)
print(data.to_string())