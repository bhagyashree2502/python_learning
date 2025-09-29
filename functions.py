# A function is a block of reusable code that performs a specific task.
# Instead of writing the same code again and again, we put it inside a function and call it whenever needed.
# Defining a Function:

# We use the def keyword to define a function.

def greet():
    print("Hello, welcome to Python!")

'''
def → keyword to define a function
greet → function name
() → parentheses (can hold parameters)
: → indicates the start of the function body
print() → function body (code to execute)
'''
#calling a function
greet()

#functions with Parameters>> Parameters allow us to pass data to the function.

def greet_user(name):
    print("Hello,", name, "!")
    
greet_user("Alice")
greet_user("Bob")

#Functions with return value>>Sometimes, we want a function to return a result instead of just printing. We use the return keyword.

def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("Sum is:", result)

#Default Parameter>>You can set default values for parameters so they are optional.

def greet_user(name="Guest"):
    print("Hello,", name)

greet_user()          # No argument passed  output: Hello Guest
greet_user("Bhavya")  # Argument passed     output: Hello Bhavya

#Functions with multiple return values>> A function can return more than one value as a tuple.
def calculate(a, b):
    return a + b, a - b

sum_result, diff_result = calculate(10, 5)
print("Sum:", sum_result)
print("Difference:", diff_result)

#Scope of variables>> Variables inside a function are local and cannot be accessed outside.
x = 10  # Global variable

def display():
    x = 5  # Local variable
    print("Inside function:", x)   #output: Inside function: 5

display()
print("Outside function:", x)      #output: Inside function: 10
