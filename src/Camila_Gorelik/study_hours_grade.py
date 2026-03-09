"""
What is the relationship between study hours per day and final grade, and does productivity plateau after a certain number of study hours?
"""

from preprocessing import preprocess_data

df = preprocess_data()

study_hours_final_grade = df.groupby('study_hours_per_day')['final_grade'].mean()

study_hours_productivity = df.groupby('study_hours_per_day')['productivity_score'].mean()

print("Average final grade by study hours per day:")
print(study_hours_final_grade.sort_index())

print("Average productivity by study hours per day:")
print(study_hours_productivity.sort_index())
