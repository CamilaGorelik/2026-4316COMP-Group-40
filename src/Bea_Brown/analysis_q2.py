"""
Does attendance affect performance, and if so, to what extent?

"""

import pandas as pd
import pygal
from src.Bea_Brown.preprocessing import preprocess_data

def analyse_attendance(data):
    """
    Group attendance into categories and calculating the average final grade
    """

    data["attendance_group"] =pd.cut(
        data["attendance_percentage"],
        bins=[0, 50, 70, 85, 100],
        labels=["Low", "Medium", "High2", "Very High"]
    )

    result = data.groupby("attendance_group")["final_grade"].mean()

    return result

def create_chart(result):
    """
    Create bar chart for attendance vs performance
    """
    chart = pygal.Bar()
    chart.title = "Attendance vs Final Grade"

    for group, score in result.items():
        chart.add(group, score)

    chart.render_to_file("attendance_vs_grade.svg")

def main():
    data = preprocess_data()

    result = analyse_attendance(data)
    print (result)

    create_chart(result)


if __name__ == "__main__":
    main()