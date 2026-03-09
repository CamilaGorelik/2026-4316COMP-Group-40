import pandas as pd
import src.data_loader as load_data

def preprocess_data():
    df = load_data()
    
    columns = [
        "exercise_hours",
        "sleep_hours",
        "productivity_score",
        "study_hours",
        "final_grade"
    ]

    df = df[columns]

    return df