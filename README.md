Exam Marks Statistics Analysis
A Python-based statistical analysis tool for evaluating student exam performance using NumPy.
Description
This command-line application allows educators to quickly analyze exam results by computing essential statistics, identifying performance trends, and generating comprehensive insights about class performance.
Features

Calculate descriptive statistics (mean, median, standard deviation)
Identify students performing above class average
Track failing students (marks below 35)
Compute class pass rate
Display highest and lowest scores
Input validation with error handling
Warning system for out-of-range marks (0-100)

Requirements

Python 3.6+
NumPy

Installation
bash# Clone the repository
git clone https://github.com/yourusername/exam-marks-analysis.git

# Navigate to the directory
cd exam-marks-analysis

# Install dependencies
pip install numpy
Usage
Run the program:
bashpython exam_marks_analysis.py
```

When prompted, enter exam marks separated by spaces:
```
Enter your marks as space-separated values: 
85 92 67 78 45 56 89 34 91 72
```

## Example Output
```
Exam Marks Statistics Analysis...

Enter your marks as space-separated values: 
85 92 67 78 45 56 89 34 91 72

Exam Marks: [85 92 67 78 45 56 89 34 91 72]

--- Class Statistics ---
Average Marks: 70.90
Median: 75.00
Standard Deviation: 18.96

--- Performance Insights ---
Students scoring above average: [85 92 78 89 91 72]
Number of students above average: 6
Students who failed (marks < 35): [34]
Number of failed students: 1
Pass Rate: 90.00%

--- Extremes ---
Highest Score: 92
Lowest Score: 34
Code Structure
The program is organized into modular functions:

load_data() - Handles user input and validates exam marks
compute_statistics() - Calculates mean, median, and standard deviation
analyze_performance() - Identifies above-average and failing students
find_extremes() - Finds highest and lowest scores
display_statistics() - Outputs statistical measures
display_performance() - Displays performance insights and pass rate
display_extremes() - Shows extreme scores
main() - Orchestrates the entire analysis workflow

Configuration
Note: The code references a PASSING_MARK constant that needs to be defined. Add this line near the top of the file:
pythonPASSING_MARK = 35
You can modify this value to change the passing threshold.
Error Handling
The program includes robust error handling for:

Non-numeric input
Empty input
Marks outside the 0-100 range (displays warning but continues)
Invalid data types

Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

Author
Your Name - Kaki Siva Rama Krishna
Acknowledgments

Built with NumPy for efficient array operations and statistical computations
