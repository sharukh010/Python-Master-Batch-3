# def display(first_name: str,last_name: str): 
#     print(first_name,last_name)

# # display("john","doe") # positional arguments
# # display("doe","john") 

# display(first_name="john",last_name="doe") # keyword arguments 
# display(last_name="doe",first_name="john")

def sum(num1: int = 0 ,num2: int=0): # default values to parameters 
    return num1 + num2 

result = sum(10)
print(result)

"""
task: 
create a function that calculates simple intrest 
SI = PxTxR / 100 
P - principle amount 
T - Time period (in years)
R - rate of interest 

- use type hints 
- make T,R as default values 
- T = 1 (year)
- R = 12 (intrest)
- return the simple interest from the function 
"""