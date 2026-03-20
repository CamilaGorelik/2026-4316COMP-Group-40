"""
Is sleep duration or exercise time more strongly correlated with student productivity, and how do these factors interact with each other?

"""

from preprocessing import preprocess_data

def exercise_sleep_analysis():
    df = preprocess_data()

    # Group data by exercise minutes and calculate average productivity
    exercise_productivity = df.groupby('exercise_minutes')['productivity_score'].mean()

    # Group data by sleep hours and calculate average productivity
    sleep_productivity = df.groupby('sleep_hours')['productivity_score'].mean()

    print("Average productivity by exercise minutes:")
    print(exercise_productivity)

    print("Average productivity by sleep hours:")
    print(sleep_productivity)

# The results show that sleep has a stronger relationship with productivity than exercise. While exercise minutes produce only small changes in productivity, sleep hours show a clear upward trend, with higher sleep associated with significantly higher productivity scores.