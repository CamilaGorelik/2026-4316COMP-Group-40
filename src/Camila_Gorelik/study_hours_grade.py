"""
What is the relationship between study hours per day and final grade, and does productivity plateau after a certain number of study hours?
"""

from src.Camila_Gorelik.preprocessing import preprocess_data

def study_hours_analysis():
    # Load the preprocessed dataset
    df = preprocess_data()

    # Group the data by study hours per day and calculate the average final grade
    # This allows me to observe how academic performence changes as study time increases
    study_hours_final_grade = df.groupby('study_hours_per_day')['final_grade'].mean()

    # Group the data by study hours per day and calculate the average productivity score
    # This helps me identify whether productivity continues to increase or reaches a plateau
    study_hours_productivity = df.groupby('study_hours_per_day')['productivity_score'].mean()

    # Output the results in a sorted order of study hours for clearer interpretation
    print("Average final grade by study hours per day:")
    print(study_hours_final_grade.sort_index())

    print("Average productivity by study hours per day:")
    print(study_hours_productivity.sort_index())

# Results:
# The grouped averages show that final grades generally increase as study hours increase,
# indicating a positive relationship between study time and academic performence.
# Productivity only increases up to a certain point and then begins to level off.
# This suggest a plateau, where additional study hours don't significantly improve productivity, 
# possibly due to fatigue or reduced efficiency.
