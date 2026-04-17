Here's a complete Python file that meets your requirements. The file includes a new function `Calculate_addition`, a main block that asks the user for a number, and prints the factorial of that number. The code also includes appropriate docstrings.

```python
def Calculate_addition(m: int, n: int) -> int:
    """
    Calculate the sum of two integers.

    Parameters:
    m (int): The first integer.
    n (int): The second integer.

    Returns:
    int: The sum of m and n.
    """
    return m + n

def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer.

    Returns:
    int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a non-negative integer to calculate its factorial: "))
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"The factorial of {user_input} is {factorial(user_input)}.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
```

### Explanation:
- The `Calculate_addition` function takes two integers as input and returns their sum.
- The `factorial` function calculates the factorial of a non-negative integer.
- The main block prompts the user for input, checks if the input is valid, and prints the factorial of the given number. If the input is invalid, it provides an appropriate error message.