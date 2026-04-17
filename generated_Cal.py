Here is a complete Python file that meets your specifications:

```python
def calculate_factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer n.

    Args:
        n (int): A non-negative integer for which to calculate the factorial.

    Returns:
        int: The factorial of the given integer n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial


if __name__ == "__main__":
    try:
        user_input = int(input("Enter a non-negative integer: "))
        result = calculate_factorial(user_input)
        print(f"The factorial of {user_input} is {result}.")
    except ValueError as e:
        print(e)
```

### Explanation:
- The `calculate_factorial` function computes the factorial of a non-negative integer `n`. It raises a `ValueError` if `n` is negative.
- The main block prompts the user for input, converts it to an integer, and calls the `calculate_factorial` function. It also handles any `ValueError` exceptions that may arise from invalid input.