# def area_of_square(length: float) -> float: 
#     return length * length 
def area_of_square(length: float | int ) -> float | int: 
    return length * length 

"""
data type     type hints 
string     -    str 
list       -    list[]
list of 
integers   -   list[int]
list of 
float      - list[float]
list of 
string     - list[str]
boolean    - bool 


ex: 
create the following functions and add type hints to it 
1) area of rectangle -> parameters are length and breadth 
- it should return the area 
2) area of circle -> parameters are radius 
- it should return the area 


"""

result = area_of_square(5)
print(result)