def add(num1: int | float ,num2: int | float) -> int | float :
    """
    It add's two numbers and returns the result. 

    Args
    - num1 (int | float) : 
      first number 
    - num2 (int | float): 
      second number 

    Returns 
    - result (int | float): 
      sum of num1 and num2

    Example 
    ```
    add(10,20)
    returns: 
    30 
    ```
    """
    result = num1 + num2 
    return result 

def display(nums: list[int | float]): 
    pass 

result = add(10,15)
result = add(50,30)
print(result)