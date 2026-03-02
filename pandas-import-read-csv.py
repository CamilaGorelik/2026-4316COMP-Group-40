import pandas as pd

dataFile = pd.read_csv("student_productivity_distraction_dataset_20000.csv")

print(dataFile.head())
print(dataFile.info())
print(dataFile.describe())
print(dataFile.isnull().sum())
