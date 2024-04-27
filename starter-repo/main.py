# starter-repo/main.py

def main():
    """
    Main function to demonstrate a simple functionality that can be expanded or improved upon.
    This function currently prints a welcome message and performs a basic calculation.
    """
    print("Welcome to Repo Wars! Let the battle of code commence!")
    result = basic_calculation(5, 3)
    print(f"The result of our basic calculation is: {result}")

def basic_calculation(a, b):
    """
    A simple function to demonstrate a basic calculation.
    This function adds two numbers and returns the result.
    
    Parameters:
    a (int): The first number
    b (int): The second number
    
    Returns:
    int: The sum of the two numbers
    """
    return a + b

if __name__ == "__main__":
    main()
