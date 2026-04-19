"""
Is sleep duration or exercise time more strongly correlated with student productivity, and how do these factors interact with each other?

"""

from src.Camila_Gorelik.preprocessing import preprocess_data

def exercise_sleep_analysis():
    # Load the preprocessed dataset
    df = preprocess_data()

    # Group data by exercise minutes and calculate the average productivity score
    # This helps identify whether increased physical activity is associated with higher productivity levels
    exercise_productivity = df.groupby('exercise_minutes')['productivity_score'].mean()

    # Group data by sleep hours and calculate the average productivity score
    # This allows us to observe how changes in sleep duration affect productivity
    sleep_productivity = df.groupby('sleep_hours')['productivity_score'].mean()
    
    # Output the results for interpretation
    print("Average productivity by exercise minutes:")
    print(exercise_productivity)

    print("Average productivity by sleep hours:")
    print(sleep_productivity)

# Results:
# The grouped averages indicate that sleep duration has a stronger relationship
# with productivity compared to exercise time.
# While increased exercise minutes lead to only minor variations in productivity,
# sleep hours show a clearer upward trend, suggesting that sufficient rest plays
# a more significant role in maintaining high productivity levels.
# This suggests that lifestyle factors impact productivity differently, with sleep
# being a more critical factor than exercise in this dataset.
