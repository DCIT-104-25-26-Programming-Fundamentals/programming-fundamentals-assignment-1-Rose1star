# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def do_add (x, y):
  return x + y

def do_subtract (x, y):
  return x - y

def do_multiply (x, y):
  return x * y

def do_divide (x, y):
  if y == 0:
    return None
  return round(x / y, 2)

def do_modulus (x, y):
  if y == 0:
    return None
  return x % y

def do_exponent (x, y):
  return x ** y

def collect_inputs ():
  val1_input = input("Enter first number : ")
  val2_input = input("Enter second number: ")
  val1 = float(val1_input)
  val2 = float(val2_input)
  return val1, val2

def show_menu ():
  print("============================")
  print("     SIMPLE CALCULATOR")
  print("============================")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Modulus")
  print("6. Exponentiation")
  print("7. Quit")

def main ():
  active = True

  while active:
    show_menu()
    option = input("Select an operation (1-7): ")

    if option == "7":
      print("Goodbye!")
      active = False
      print()
      continue

    if option not in ["1", "2", "3", "4", "5", "6"]:
      print("Error: Please enter a number between 1 and 7.")
      print()
      continue

    val1, val2 = collect_inputs()

    if option == "1":
      outcome = do_add(val1, val2)
      print(f"Result: {val1} + {val2} = {outcome}")
    elif option == "2":
      outcome = do_subtract(val1, val2)
      print(f"Result: {val1} - {val2} = {outcome}")
    elif option == "3":
      outcome = do_multiply(val1, val2)
      print(f"Result: {val1} * {val2} = {outcome}")
    elif option == "4":
      outcome = do_divide(val1, val2)
      if outcome is None:
        print("Error: Cannot divide by zero.")
      else:
        print(f"Result: {val1} / {val2} = {outcome}")
    elif option == "5":
      outcome = do_modulus(val1, val2)
      if outcome is None:
        print("Error: Cannot divide by zero.")
      else:
        print(f"Result: {val1} % {val2} = {outcome}")
    elif option == "6":
      outcome = do_exponent(val1, val2)
      print(f"Result: {val1} ** {val2} = {outcome}")

    print()

main()
