import numpy as np

def get_matrix(rows, cols, name="Matrix"):
    """Takes input from user to create a matrix."""
    print(f"\nEnter the elements of {name} row-wise (separated by spaces):")
    entries = list(map(float, input().split()))
    
    if len(entries) != rows * cols:
        print("Error: Incorrect number of elements entered.")
        return None
    
    return np.array(entries).reshape(rows, cols)

def matrix_addition():
    """Performs matrix addition."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    matrix1 = get_matrix(rows, cols, "First Matrix")
    matrix2 = get_matrix(rows, cols, "Second Matrix")

    if matrix1 is not None and matrix2 is not None:
        print("\nResultant Matrix (Addition):\n", matrix1 + matrix2)

def matrix_subtraction():
    """Performs matrix subtraction."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix1 = get_matrix(rows, cols, "First Matrix")
    matrix2 = get_matrix(rows, cols, "Second Matrix")

    if matrix1 is not None and matrix2 is not None:
        print("\nResultant Matrix (Subtraction):\n", matrix1 - matrix2)

def scalar_multiplication():
    """Multiplies a matrix by a scalar (constant)."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = get_matrix(rows, cols)
    scalar = float(input("Enter the scalar value: "))

    if matrix is not None:
        print("\nResultant Matrix (Scalar Multiplication):\n", scalar * matrix)

def matrix_multiplication():
    """Performs matrix multiplication."""
    rows1 = int(input("Enter rows of first matrix: "))
    cols1 = int(input("Enter columns of first matrix: "))

    matrix1 = get_matrix(rows1, cols1, "First Matrix")

    rows2 = int(input("Enter rows of second matrix: "))
    cols2 = int(input("Enter columns of second matrix: "))

    if cols1 != rows2:
        print("\nError: Number of columns in first matrix must equal number of rows in second matrix.")
        return

    matrix2 = get_matrix(rows2, cols2, "Second Matrix")

    if matrix1 is not None and matrix2 is not None:
        print("\nResultant Matrix (Multiplication):\n", np.dot(matrix1, matrix2))

def matrix_transpose():
    """Finds the transpose of a matrix."""
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = get_matrix(rows, cols)

    if matrix is not None:
        print("\nTranspose of the Matrix:\n", matrix.T)

def matrix_determinant():
    """Calculates the determinant of a square matrix."""
    size = int(input("Enter the size of the square matrix (N for NxN): "))

    matrix = get_matrix(size, size)

    if matrix is not None:
        print("\nDeterminant of the Matrix:", round(np.linalg.det(matrix), 2))

def matrix_inverse():
    """Finds the inverse of a square matrix (if it exists)."""
    size = int(input("Enter the size of the square matrix (N for NxN): "))

    matrix = get_matrix(size, size)

    if matrix is not None:
        determinant = np.linalg.det(matrix)
        
        if determinant == 0:
            print("\nError: The matrix is singular and does not have an inverse.")
        else:
            print("\nInverse of the Matrix:\n", np.linalg.inv(matrix))

def menu():
    """Displays the menu and handles user choice."""
    while True:
        print("\n📌 MATRIX CALCULATOR MENU")
        print("1. Matrix Addition")
        print("2. Matrix Subtraction")
        print("3. Scalar Multiplication")
        print("4. Matrix Multiplication")
        print("5. Matrix Transpose")
        print("6. Matrix Determinant")
        print("7. Matrix Inverse")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            matrix_addition()
        elif choice == "2":
            matrix_subtraction()
        elif choice == "3":
            scalar_multiplication()
        elif choice == "4":
            matrix_multiplication()
        elif choice == "5":
            matrix_transpose()
        elif choice == "6":
            matrix_determinant()
        elif choice == "7":
            matrix_inverse()
        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("\nInvalid choice! Please try again.")

if __name__ == "__main__":
    print("🔢 WELCOME TO MATRIX CALCULATOR 🔢")
    menu()
