def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage that handles the empty list case
data = []
average = calculate_average(data)
print(f"The average is: {average}")
data = [10, 20, 30]
average = calculate_average(data)
print(f"The average is: {average}")

