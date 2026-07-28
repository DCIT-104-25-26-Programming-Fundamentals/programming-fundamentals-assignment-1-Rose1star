# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def calc_average (marks):
  total = 0
  for mark in marks:
    total = total + mark
  result = total / len(marks)
  return round(result, 2)

def register_student (roster):
  full_name = input("Student name: ")
  id_input = input("Student ID: ")
  reg_number = int(id_input)

  qty_input = input("How many scores? ")
  qty = int(qty_input)

  marks = []
  for i in range(1, qty + 1):
    mark_input = input(f"Enter score {i}: ")
    marks.append(int(mark_input))

  record = {
    "name": full_name,
    "id": reg_number,
    "scores": marks
  }
  roster.append(record)
  print(f'Student "{full_name}" added successfully.')

def list_students (roster):
  if len(roster) == 0:
    print("No students have been added yet.")
    return

  print("-" * 50)
  print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average':<10}")
  print("-" * 50)
  for record in roster:
    marks_text = ", ".join(str(m) for m in record["scores"])
    avg = calc_average(record["scores"])
    print(f"{record['name']:<15}{record['id']:<12}{marks_text:<15}{avg:<10}")
  print("-" * 50)

def lookup_average (roster):
  id_input = input("Enter student ID: ")
  target_id = int(id_input)

  for record in roster:
    if record["id"] == target_id:
      avg = calc_average(record["scores"])
      print(f"{record['name']}'s average score: {avg}")
      return

  print("Error: No student found with that ID.")

def show_menu ():
  print("================================")
  print("   STUDENT RECORD SYSTEM MENU")
  print("================================")
  print("1. Add student")
  print("2. Display all students")
  print("3. Calculate average score")
  print("4. Quit")

def main ():
  roster = []
  active = True

  while active:
    show_menu()
    selection = input("Enter your choice (1-4): ")

    if selection == "1":
      register_student(roster)
    elif selection == "2":
      list_students(roster)
    elif selection == "3":
      lookup_average(roster)
    elif selection == "4":
      print("Goodbye!")
      active = False
    else:
      print("Error: Please enter a number between 1 and 4.")

    print()

main()