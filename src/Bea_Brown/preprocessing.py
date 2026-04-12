import pandas as pd
from data_loader import load_data

def preprocess_data():
    """
    Loading in my dataset and choosing only what i need
    """
    df = load_data()

#choosing the relevant columns
    columns = [
        'gender',
        'study_hours_per_day',
        'attendance_percentage',
        'focus_score',
        'stress_level',
        'sleep_hours',
        'final_grade'
    ]
    """
Removing any empty values
"""
    df = df[columns]

    return df

