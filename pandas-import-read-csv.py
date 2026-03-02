import pandas as pd

data-file = pd.read_csv("student_productivity_distraction_dataset_20000.csv")

print(data-file.head())
print(data-file.info())
print(data-file.describe())
print(data-file.isnull().sum())
