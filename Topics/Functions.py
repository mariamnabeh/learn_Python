"""In ths chapter we will learn more about Function , which are named blocks of code designed 
to do one speific job!

Why we use Functions?
well, We use Functions when we want to perform a particular task that you've defined in a function, you call the
 function responsible for it. Also if you need to perform that task multiple times throughout your program.
"""

# syntax: def + function_name (inputs): 
def Hello(name):
    print("Hello", name) # What function do is print hello + name

Hello("mariam") # Calling the function with argument

#---------------------------------------
# Parameters vs Arguments:
# Parameter -> variable inside function definition: def greet(username)
# Argument  -> actual value passed when calling function: greet("Mariam")

#---------------------------------------
# Positional vs Keyword Arguments:
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name.title()}.")

describe_pet("cat", "luna")                       # Positional: order matters!
describe_pet(pet_name="luna", animal_type="cat")  # Keyword: order doesn't matter

#---------------------------------------
# Default Values:
# Note: parameters with default values MUST come last!
def make_coffee(size, type="Espresso"):
    print(f"Making a {size} {type}")

make_coffee("Large")             # Uses default "Espresso"
make_coffee("Medium", "Latte")   # Overrides default with "Latte"

#---------------------------------------
# Return Values:
# Functions can process data and send back a value using 'return'
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Sum is:", result)

# Note: Once 'return' is reached, the function stops executing!
def check_even(num):
    if num % 2 == 0:
        return True
    return False

#---------------------------------------
# Common Errors with Functions:

# 1: Forgetting parentheses when calling
# print(Hello) # Prints function memory reference instead of executing it!

# 2: Missing required positional arguments
# describe_pet("cat") # TypeError: missing 1 required positional argument

# 3: Using function return value without saving/printing it
def multiply(a, b):
    return a * b

multiply(3, 4) # Runs silently, nothing appears on screen unless printed!
print(multiply(3, 4))

"""Don't feel bad when a small fix takes a long time to find ; Tou are not alone in this experience."""
# The mission and I are done… we’re finished…