"""
Is sleep duration or exercise time more strongly correlated with student productivity, and how do these factors interact with each other?

"""

from preprocessing import preprocess_data

df = preprocess_data()

exercise_productivity = df.groupby('exercise_minutes')['productivity_score'].mean()

sleep_productivity = df.groupby('sleep_hours')['productivity_score'].mean()

print("Average productivity by exercise minutes:")
print(exercise_productivity)

print("Average productivity by sleep hours:")
print(sleep_productivity)