def add(num1: int | float ,num2: int | float) -> int | float :
    # doc string 
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

def exp(num1: int,num2: int) -> int:
    """
    It calcuates the exponent and returns the value. 

    Args
    - num1 (int) : It is the base value 
    - num2 (int) : It is the power value

    Returns 
    - result (int) : exponent of num1 ^ num2 
    """
    
    result = num1 ** num2
    return result


int1 = int(input("Enter your first number: "))
int2 = int(input("Enter your second number: "))
result = exp(int1,int2)
print(result)

def sub(num1: int | float ,num2: int | float) -> int | float :

  """
  It subtract's two numbers and returns the result. 

  Args
  - num1 (int | float) : 
    first number 
  - num2 (int | float): 
    second number 

  Returns 
  - result (int | float): 
    num 1 minus num 2

  Example 
  ```
  sub(50,25)
  returns: 
  25 
  ```
  """
  result = num1 - num2 
  return result

result = add(10,15)
result = add(50,30)
print(result)