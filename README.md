# Student Productivity Analysis 

// Overview
This project analyses the relationship between student study habits, lifestyle factors, and academic performance using the *Student Productivity And Digial Distraction Dataset*.

The application allows users to run different analyses and visualisations through a simple command-line interface.

---

// Features

- ANALYSE:
  - Study hours vs final grade
  - Study hours vs productivity (including plateau effect)
  - Sleep vs exercise impact on productivity
  - Gender differences in performance
  - Attendance vs final grade
 
- VISUALISATIONS:
  - Line graph
  - Scatter plot with trend line
  - Bar charts

---

// Technologies Used

- Python
- pandas (data processing)
- matplotlib (visualisation)
- numpy (trend line calculation)
- pygal (bar charts)

---

// Setup Instructions

1. Clone the repository
   - git clone <https://github.com/CamilaGorelik/2026-4316COMP-Group-40>
   - cd 2026-4316COMP-Group-40

2. Create a virtual environment
   - python3 -m venv venv

3. Activate the virtual environment:
   - On Mac/Linux:
   - source venv/bin/activate
   - On Windows:
   - venv/Scripts/activate

4. Install required packages
   - pip install pandas matplotlib numpy pygal

5. Running the program
   Run the application from the project root:
   - python -m src.Camila_Gorelik.main

---

// Menu Options for Camila's analysis:

Once running, you will see:
- 1 - Exercise vs Sleep
- 2 - Study Hours
- 3 - Run All
- 4 - Line Plot (Study Hours vs Final Grade)
- 5 - Scatter Plot (Study Hours vs Productivity)
- q - Quit

Enter a number to run the corresponding analysis for visualisation.

--- 

// Visualisations

- Line Graph
- Shows average final grade and productivity across study hours
- Uses grouped and averaged data for clarity

- Scatter Plot with Trend Line
- Displays raw data distribution
- Includes a line of best fit using NumPy
- Highlights correlation between study hours and productivity

---

// Dataset

- The dataset is included in the project:

- data/student_productivity_distribution_dataset_20000.csv

- No additional configuration is required.

---

// NOTES

- Make sure the virtual environment is activated before running the program
- Close any graph windows to return to the menu
- Run the program from the project root directory
