import matplotlib.pyplot as plt
import numpy as np
from src.Camila_Gorelik.preprocessing import preprocess_data

def study_hours_visualisation():
    """
    Visualises the relationship between study hours, final grade,
    and productivity using line graphs.
    This function helps identify trends and potential plateau
    in productivity as study hours increase.
    """

    # Load processed dataset
    df = preprocess_data()

    df['study_hours_per_day'] = df['study_hours_per_day'].round()

    # Group data by study hours and calculate averages
    study_hours_final_grade = df.groupby('study_hours_per_day')['final_grade'].mean().sort_index()
    study_hours_productivity = df.groupby('study_hours_per_day')['productivity_score'].mean().sort_index()

    # Create figure
    plt.figure()

    # Plot final grade trend
    plt.plot(
        study_hours_final_grade.index,
        study_hours_final_grade.values,
        label='Final Grade'
    )

    # Plot productivity trend
    plt.plot(
        study_hours_productivity.index,
        study_hours_productivity.values,
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
        alpha=0.3,
        zorder=1
    )

    # Calculate and plot line of best fit (trend line)
    z = np.polyfit(df['study_hours_per_day'], df['productivity_score'], 1)
    p = np.poly1d(z)
    x = np.sort(df['study_hours_per_day'])
    y = p(x)
    plt.plot(
        x,
        y,
        linewidth=3,
        color='red',
        label='Trend Line',
        zorder=3
    )

    # Titles and labels
    plt.title("Study Hours vs Productivity (Scatter Plot with Trend Line)")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("Productivity Score")

    plt.legend()
    plt.grid(True)

    # Display graph
    plt.show(block=True)
    plt.close
