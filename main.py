import numpy as np

def load_data():
    """
    Create and return a numpy array containing exam marks.
    
    Returns:
        np.ndarray: Array of exam marks, or None if input is invalid
    """
    try:
        print("Enter your marks as space-separated values: ")
        arr = list(map(int, input().split()))
        if not arr:
            raise ValueError("No marks entered")
        marks = np.array(arr)

        if np.any((marks < 0) | (marks > 100)):
            print("Warning: Some marks are outside 0-100 range")
        return marks
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None

def compute_statistics(marks):
    """
    Compute basic statistical measures using numpy.
    
    Parameters:
        marks (np.ndarray): Array of exam marks
        
    Returns:
        tuple: (average, median, std_deviation)
    """
    average = np.mean(marks)

    median = np.median(marks)

    std_deviation= round(np.std(marks),2)

    return average,median,std_deviation

def analyze_performance(marks,average):
    """
    Analyze performance by finding students above average and failed students.
    
    Parameters:
        marks (np.ndarray): Array of exam marks
        average (float): Class average mark
        
    Returns:
        tuple: (above_average, failed_students)
    """

    above_average = marks[marks > average]

    failed_students = marks[marks < 35]

    return above_average,failed_students

def find_extreme(marks):
    """
    Find the highest and lowest scores.
    
    Parameters:
        marks (np.ndarray): Array of exam marks
        
    Returns:
        tuple: (highest_score, lowest_score)
    """
    highest_score = np.max(marks) 
    lowest_score = np.min(marks) 

    return highest_score,lowest_score

def  display_statistics(average, median, std_deviation):
    """
    Display statistical measures.
    
    Parameters:
        average (float): Mean of marks
        median (float): Median of marks
        std_deviation (float): Standard deviation of marks
    """
    print("\n--- Class Statistics ---")
    print(f"Average Marks: {average:.2f}")
    print(f"Median: {median:.2f}")
    print(f"Standard Deviation: {std_deviation}")

def display_performance(above_average, failed_students):
    """
    Display performance insights.
    
    Parameters:
        above_average (np.ndarray): Marks of students above average
        failed_students (np.ndarray): Marks of students who failed
    """
    print("\n--- Performance Insights ---")
    print(f"Students scoring above average: {above_average}")
    print(f"Number of students above average: {len(above_average)}")
    print(f"Students who failed (marks < {PASSING_MARK}): {failed_students}")
    print(f"Number of failed students: {len(failed_students)}")
    
    # Calculate pass rate
    total_students = len(above_average) + len(failed_students)
    if total_students > 0:
        pass_rate = ((total_students - len(failed_students)) / total_students) * 100
        print(f"Pass Rate: {pass_rate:.2f}%")

def display_extremes(highest_score, lowest_score):
    """
    Display extreme scores.
    
    Parameters:
        highest_score (int/float): Highest score in the class
        lowest_score (int/float): Lowest score in the class
    """
    print("\n--- Extremes ---")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")

def main():
    """
    Main function to orchestrate the exam marks analysis.
    """
    print("Exam Marks Statistics Analysis...\n")
    
    marks = load_data()
    
    if marks is not None:
        print(f"\nExam Marks: {marks}")
        
        # Compute statistics
        average, median, std = compute_statistics(marks)
        display_statistics(average, median, std)
        
        # Analyze performance
        above_average, failed_students = analyze_performance(marks, average)
        display_performance(above_average, failed_students)
        
        # Find extremes
        highest_score, lowest_score = find_extremes(marks)
        display_extremes(highest_score, lowest_score)
    else:
        print("Analysis could not be performed due to invalid input.")

if __name__=="__main__":
    main()
