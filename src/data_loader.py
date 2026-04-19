import os
import pandas as pd

def load_data():
    # Get the root directory of the project
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Build path to the CSV file
    file_path = os.path.join(
        base_dir,
        "data",
        "student_productivity_distraction_dataset_20000.csv"
    )
    df = pd.read_csv(file_path)
    return df
