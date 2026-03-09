import pandas as pd

def load_data():
    df = pd.read_csv(r"M:\2026-4316COMP-group40\data\student_productivity_distraction_dataset_20000.csv")
    return df