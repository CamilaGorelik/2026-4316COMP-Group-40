import matplotlib.pyplot as plt
import numpy as np
from preprocessing import preprocess_data

def study_hours_visualisation():
    """
    Visualises the relationship between study hours, final grade,
    and productivity using line graphs.
    This function helps identify trends and potential plateau
    in productivity as study hours increase.
    """

    # Load processed dataset
    df = preprocess_data()

    # Group data by study hours and calculate averages
    study_hours_final_grade = df.groupby('study_hours_per_day')['final_grade'].mean().sort_index()
    study_hours_productivity = df.groupby('study_hours_per_day')['productivity_score'].mean().sort_index()

    # Create figure
    plt.figure()

    # Plot final grade trend
    plt.plot(
        study_hours_final_grade.index,
        study_hours_final_grade.values,
        marker='o',
        label='Final Grade'
    )

    # Plot productivity trend
    plt.plot(
        study_hours_productivity.index,
        study_hours_productivity.values,
        marker='s',
        label='Productivity'
    )

    # Titles and labels 
    plt.title("Study Hours vs Academic Performance and Productivity")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("Average Score")

    # Improve readability
    plt.grid(True)
    plt.legend()

    # Display graph
    plt.show()

def study_hours_scatter_visualisation():
    """
    Visualises the relationship between study hours and productivity 
    using a scatter plot and a line of best fit.
    This provides a more detailed view of the data distribution and 
    helps identify correlation and potential plateau.
    """

    # Load dataset
    df = preprocess_data()

    # Create scatter plot 
    plt.figure()
    plt.scatter(
        df['study_hours_per_day'],
        df['productivity_score'],
        alpha=0.5
    )

    # Calculate and plot line of best fit (trend line)
    z = np.polyfit(df['study_hours_per_day'], df['productivity_score'], 1)
    p = np.poly1d(z)
    plt.plot(df['study_hours_per_day'], p(df['study_hours_per_day']))

    # Titles and labels
    plt.title("Study Hours vs Productivity (Scatter Plot with Trend Line)")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("Productivity Score")

    plt.grid(True)

    # Display graph
    plt.show()
