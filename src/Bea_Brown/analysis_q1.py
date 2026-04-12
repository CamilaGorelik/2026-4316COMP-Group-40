"""
Are there gender differences in productivity levels among students, and if so, what factors contribute to these differences?
"""

import pygal
from preprocessing import preprocess_data

def analyse_gender (data):
    """
    Grouping the data by gender and calculating averages
    """
    return data.groupby("gender").mean(numeric_only=True)
    