import matplotlib.pyplot as plt
from preprocessing import preprocess_data

def study_hours_visualisation():
    df = preprocess_data()

    # Group data
    study_hours_final_grade = df.groupby('study_hours_per_day')['final_grade'].mean()
    study_hours_productivity = df.groupby('study_hours_per_day')['productivity_score'].mean()

    # Plot both lines
    plt.figure()

    plt.plot(study_hours_final_grade, label='Fianl Grade')
    plt.plot(study_hours_productivity, label='Productivity')

    plt.title("Study Hours vs Performance")
    plt.xlabel("Study Hours Per Day")
    plt.ylabel("Average Score")

    plt.legend()

    plt.show()

if __name__ == "__main__":
    study_hours_visualisation()