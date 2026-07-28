# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def get_numbers(n):
    numbers = []
    for i in range(n):
        score = float(input(f"Enter number {i + 1}: "))
        if score.is_integer():
            score = int(score)
        numbers.append(score)
    return numbers


def findSum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def findAvg(numbers):
    total = findSum(numbers)
    return total / len(numbers)


def findMax(numbers):
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest


def findMin(numbers):
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest


def main():
    try:
        n = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    numbers = get_numbers(n)

    total = findSum(numbers)
    average = findAvg(numbers)
    maximum = findMax(numbers)
    minimum = findMin(numbers)


    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()