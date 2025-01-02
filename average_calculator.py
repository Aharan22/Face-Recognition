def calculate_average_marks(student_marks):
    """
    Calculate the average marks from a dictionary of student names and their marks.

    Parameters:
        student_marks (dict): A dictionary where keys are student names and values are their marks.

    Returns:
        float: The average marks of the students.
    """
    if not student_marks:
        return 0  # To handle the case where the dictionary is empty

    total_marks = sum(student_marks.values())  # Calculate the sum of all marks
    number_of_students = len(student_marks)  # Count the number of students
    
    average_marks = total_marks / number_of_students  # Calculate the average
    return average_marks


# Function to take dynamic input
def get_student_marks():
    """
    Get student names and marks from user input.

    Returns:
        dict: A dictionary with student names as keys and marks as values.
    """
    student_marks = {}
    print("Enter student names and marks. Type 'stop' to finish.")
    
    while True:
        name = input("Enter student name (or type 'stop' to finish): ").strip()
        if name.lower() == 'stop':
            break
        
        try:
            mark = float(input(f"Enter marks for {name}: ").strip())
            student_marks[name] = mark
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")
    
    return student_marks


# Example usage
student_marks = get_student_marks()
average_marks = calculate_average_marks(student_marks)
print(f"The average marks are: {average_marks:.2f}" if student_marks else "No data entered.")
