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

def create_charts(stats):
        """
        Creating a few charts for gender comparison
        """
        #The final grade chart
        chart1 = pygal.Bar()
        chart1.title = "Average Final Grade by Gender"

        for gender, score in stats["final_grade"].items():
            chart1.add(gender, score)

        chart1.render_to_file("gender_final_grade.svg")

        #study hours chart
        chart2 = pygal.Bar()
        chart2.title = "Study Hours Per Day by Gender"

        for gender, hours in stats["study_hours_per_day"].items():
            chart2.add(gender, hours)

        chart2.render_to_file("gender_study_hours.svg")

        #Focus Score chart
        chart3 = pygal.Bar()
        chart3.title = "Focus Score by Gender"

        for gender, focus in stats["focus_score"].items():
            chart3.add(gender, focus)

        chart3.render_to_file("gender_focus.svg")

def main():
        data = preprocess_data()

        stats = analyse_gender(data)
        print(stats)

        create_charts(stats)

if __name__ == "__main__" :
    main()