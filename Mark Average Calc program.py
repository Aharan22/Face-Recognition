
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


# Example usage
student_marks = {"Aharan": 85, "Sarang": 95, "Anas": 92, "Subin": 88}
average_marks = calculate_average_marks(student_marks)
print(f"The average marks are: {average_marks:.2f}")




          
        