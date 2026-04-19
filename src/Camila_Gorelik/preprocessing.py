import pandas as pd
from src.data_loader import load_data

def preprocess_data():
    """
    Loads and preprocesses the dataset for analysis.
    This function prepares the dataset by:
    * Loading the raw data from the data loader
    * Selecting only the columns relevant to the questions
    * Returning cleaned data ready for analysis
    """

    # Load the dataset form the external data loader module
    df = load_data()

    # Define the subset of columns needed for the analysis
    # These variables are chosed based on the questions:
       # - exercise_minutes and sleep_hours (lifestyle factors)
       # - productivity_score (main performence metric)
       # - study_hours_per_day and final_grade (academic performence)
    
    columns = [
        'exercise_minutes',
        'sleep_hours',
        'productivity_score',
        'study_hours_per_day',
        'final_grade'
    ]

    # Filter the cleaned data to include only the selected columns
    # Simplifies further analysis and improves readability
    df = df[columns]

    # Return the processed dataset
    return df
