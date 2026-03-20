from exercise_sleep_productivity import exercise_sleep_analysis
from study_hours_grade import study_hours_analysis
from visualisation import study_hours_visualisation

def main():

    print("Student Productivity Analysis")
    print("1 - Exercise vs Sleep")
    print("2 - Study Hours")
    print("3 - Run All")
    print("4 - Show Visualisation")

    choice = input("Enter your choice: ")

    # Analysis 1
    if choice == "1":
        exercise_sleep_analysis()

    # Analysis 2
    elif choice == "2":
        study_hours_analysis()

    elif choice == "3":
        exercise_sleep_analysis()
        study_hours_analysis()

    elif choice == "4":
        study_hours_visualisation()

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()