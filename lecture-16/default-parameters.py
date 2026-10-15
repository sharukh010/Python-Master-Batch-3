def add(num1 = 0,num2 = 0): 
    return num1+num2 


# print(add(1,2))
print(add(1,2))

"""
a function which can generate super hero name 
by default the last_name = "man" 
"""
def super_hero(first_name,last_name="man"):
    print(first_name,last_name)

super_hero("super") # super man 
super_hero("bat")# bat man 
super_hero("ant")
super_hero("iron")
super_hero("capitan","america")
super_hero("hulk","")

"""
define a function called snacks_combo(item,drink)
consider coke as the default drink 
snacks_combo("french fires")
french fires and coke 

snacks_combo("french fires","smoothie")
french fies and smoothie 
"""