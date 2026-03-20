from exercise_sleep_productivity import exercise_sleep_analysis
from study_hours_grade import study_hours_analysis

def main():

    print("Student Productivity Analysis")
    print("1 - Exercise vs Sleep")
    print("2 - Study Hours")
    print("3 - Run All")

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

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()