# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 7
# =============================================================================
#
# TASK: Console-Based To-Do List Application
#
# Build a simple to-do list program that runs entirely in the console and
# allows the user to manage their tasks interactively using a menu.
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Task
#      - Prompt the user to type a task description.
#      - Add it to the list and confirm it was added.
#
#   2. View All Tasks
#      - Display all tasks currently in the list, numbered from 1.
#      - If the list is empty, print a friendly message saying so.
#
#   3. Delete a Task
#      - Show the list of tasks with their numbers.
#      - Ask the user which task number they want to remove.
#      - Remove the task and confirm the deletion.
#      - If the task number is invalid, print an error message.
#
#   4. Quit
#      - End the program with a farewell message.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        TO-DO LIST MENU
#   ============================
#   1. Add task
#   2. View tasks
#   3. Delete task
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Enter task: Buy groceries
#   Task added: "Buy groceries"
#
#   Enter your choice (1-4): 1
#   Enter task: Study for exams
#   Task added: "Study for exams"
#
#   Enter your choice (1-4): 2
#   Your Tasks:
#   1. Buy groceries
#   2. Study for exams
#
#   Enter your choice (1-4): 3
#   Enter task number to delete: 1
#   Task "Buy groceries" has been removed.
#
#   Enter your choice (1-4): 4
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store tasks in a Python list.
# - Use a loop to keep the menu running until the user chooses to quit.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices gracefully (print an error, do not crash).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_item (todo_list):
  description = input("Enter task: ")
  todo_list.append(description)
  print(f'Task added: "{description}"')

def show_items (todo_list):
  if len(todo_list) == 0:
    print("Your to-do list is empty.")
    return

  print("Your Tasks:")
  index = 1
  for item in todo_list:
    print(f"{index}. {item}")
    index = index + 1

def remove_item (todo_list):
  if len(todo_list) == 0:
    print("Your to-do list is empty.")
    return

  show_items(todo_list)
  pick_input = input("Enter task number to delete: ")
  pick = int(pick_input)

  if pick < 1 or pick > len(todo_list):
    print("Error: Invalid task number.")
    return

  deleted_item = todo_list[pick - 1]
  todo_list.pop(pick - 1)
  print(f'Task "{deleted_item}" has been removed.')

def show_menu ():
  print("============================")
  print("     TO-DO LIST MENU")
  print("============================")
  print("1. Add task")
  print("2. View tasks")
  print("3. Delete task")
  print("4. Quit")

def main ():
  todo_list = []
  active = True

  while active:
    show_menu()
    selection = input("Enter your choice (1-4): ")

    if selection == "1":
      add_item(todo_list)
    elif selection == "2":
      show_items(todo_list)
    elif selection == "3":
      remove_item(todo_list)
    elif selection == "4":
      print("Goodbye!")
      active = False
    else:
      print("Error: Please enter a number between 1 and 4.")

    print()

main()
