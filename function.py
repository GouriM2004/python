def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage
if __name__ == "__main__":
    nums = [10, 20, 30, 40, 50]
    avg = calculate_average(nums)
    print(f"Average: {avg}")