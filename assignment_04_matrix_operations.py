# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_matrix (num_rows, num_cols):
  grid = []
  for r in range(num_rows):
    line = input(f"Enter row {r + 1}: ")
    entries = line.split()
    row_data = []
    for entry in entries:
      row_data.append(int(entry))
    grid.append(row_data)
  return grid

def display_matrix (grid):
  for row_data in grid:
    text = ""
    for value in row_data:
      text = text + str(value) + "\t"
    print(text)

def transpose (grid, num_rows, num_cols):
  flipped = []
  for c in range(num_cols):
    new_row = []
    for r in range(num_rows):
      new_row.append(grid[r][c])
    flipped.append(new_row)
  return flipped

def add_grids (grid_a, grid_b, num_rows, num_cols):
  combined = []
  for r in range(num_rows):
    new_row = []
    for c in range(num_cols):
      new_row.append(grid_a[r][c] + grid_b[r][c])
    combined.append(new_row)
  return combined

def multiply_grids (grid_a, grid_b, rows_a, shared_dim, cols_b):
  product = []
  for r in range(rows_a):
    new_row = []
    for c in range(cols_b):
      cell_sum = 0
      for k in range(shared_dim):
        cell_sum = cell_sum + grid_a[r][k] * grid_b[k][c]
      new_row.append(cell_sum)
    product.append(new_row)
  return product

def main ():
  print("PART A: Transpose a Matrix")
  r1 = int(input("Enter number of rows: "))
  c1 = int(input("Enter number of columns: "))
  original = get_matrix(r1, c1)
  print("Original Matrix:")
  display_matrix(original)
  flipped = transpose(original, r1, c1)
  print("Transposed Matrix:")
  display_matrix(flipped)

  print()
  print("PART B: Add Two Matrices")
  r2 = int(input("Enter number of rows: "))
  c2 = int(input("Enter number of columns: "))
  print("Enter Matrix A:")
  grid_a = get_matrix(r2, c2)
  print("Enter Matrix B:")
  grid_b = get_matrix(r2, c2)
  total_grid = add_grids(grid_a, grid_b, r2, c2)
  print("Sum Matrix:")
  display_matrix(total_grid)