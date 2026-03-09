import pandas as pd

# marks = pd.read_csv('marks.csv')
 # Example marks for 5 students
marks = (80, 90, 75, 85, 95)
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