from exercise_sleep_productivity import exercise_sleep_analysis
from study_hours_grade import study_hours_analysis
from visualisation import study_hours_visualisation

def main():
    """
    Main entry point for the application.
    This function allows the user to select which analysis or visualisation to run until they
    choose to exit. It connects user input to the appropriate analysis functions.
    """

    while True: 
        # Display menu options to the user
        print("\nStudent Productivity Analysis")
        print("1 - Exercise vs Sleep")
        print("2 - Study Hours")
        print("3 - Run All")
        print("4 - Show Visualisation")
        print("5 - Quit")

    # Take user input to determine which function to execute
    choice = input("Enter your choice: ").strip().lower()

    # Exit condition
    if choice == "5":
        print("Exiting program...")
        break
        
    # Option 1: Run exercise vs sleep analysis
    elif choice == "1":
        exercise_sleep_analysis()

    # Option 2: Run study hours vs grade/productivity analysis
    elif choice == "2":
        study_hours_analysis()

    # Option 3: Run all analyses sequentially
    elif choice == "3":
        exercise_sleep_analysis()
        study_hours_analysis()

    # Option 4: Display visualisation for study hours analysis
    elif choice == "4":
        study_hours_visualisation()

    # Handle invalid input
    else:
        print("Invalid choice. Please enter 1-4 or '5' to quit.")

# Ensures that the program runs only when this file is executed directly,
# and not when it is imported as a module in another script
if __name__ == "__main__":
    main()
