


def find_largest_and_smallest(numbers):
    """
    Function to find the largest and smallest numbers in a given list.
    
    Parameters:
        numbers (list): A list of integers or floats.
    
    Returns:
        tuple: A tuple containing the smallest and largest numbers.
    """
    if not numbers:  # Check if the list is empty
        return None, None

    # Initialize smallest and largest with the first number in the list
    smallest = largest = numbers[0]

    # Loop through the list to find smallest and largest
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number

    return smallest, largest


# Input and Output
while True:
    try:
        # Take user input and filter out invalid entries
        user_input = input("Enter a list of numbers separated by spaces: ")
        numbers = list(map(float, user_input.split()))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")

smallest, largest = find_largest_and_smallest(numbers)

if smallest is not None and largest is not None:
    print(f"The smallest number is: {smallest}")
    print(f"The largest number is: {largest}")
else:
    print("The list is empty!")
