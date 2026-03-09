import pandas as pd

# marks = pd.read_csv('marks.csv')
 # Example marks for 5 students
''''marks = (80, 90, 75, 85, 95)
# Calculate average marks
average_marks = sum(marks) / len(marks)
print(f"Average Marks: {average_marks}")

series = pd.Series(marks)
print("Marks Series:")
print(series)

data = {
    "name": ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    "Marks": marks,
    "age": [20, 22, 21, 23, 20]

}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

df.describe()

'''
df = pd.read_csv('data.csv')

# head() method is used to display the first few rows of the DataFrame, which is useful for quickly inspecting the data.
print(df.head(5))

# tail() method is used to display the last few rows of the DataFrame, which can be helpful to check for any anomalies or to see the end of the dataset.
print(df.tail(5))

# info() method provides a concise summary of the DataFrame, including the number of non-null entries, data types, and memory usage.
print(df.info())

# column  shows the names of the columns in the dataset
print(df.columns)

# describe the data like mean, std, min, max, etc.
print(df.describe())

# isnull() method is used to check for missing values in the DataFrame. It returns a DataFrame of the same shape with boolean values indicating whether each element is null (True) or not (False). By summing the result, we can get the total count of null values in each column.

isnull = df.isnull().sum()
print("Number of null values in each column:")
print(isnull)

print(df.isnull().sum())

# fillna() method is used to fill the null values in the DataFrame with a specified value. In this case, we are filling null values with 0. The inplace=True argument modifies the original DataFrame directly.

df.fillna(0, inplace=True)
print("DataFrame after filling null values with 0:")
print(df)

# drop_duplicates() method is used to remove duplicate rows from the DataFrame. By default, it considers all columns to identify duplicates, but you can specify a subset of columns if needed. The inplace=True argument modifies the original DataFrame directly.
df.drop_duplicates(inplace=True)
print("DataFrame after dropping duplicates:")
print(df)

print(df.head())

# replace null values with mean of the column
df.fillna(df.mean(), inplace=True)
print("DataFrame after filling null values with mean:")
print(df)

# data correlation
# +1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no correlation. Values between -1 and +1 indicate the strength of the correlation, with values closer to +1 or -1 indicating stronger correlations.

correlation = df.corr()
print("Correlation Matrix:")
print(correlation)