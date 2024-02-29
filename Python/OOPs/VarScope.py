def printSpace():
    print()
    print()

'''
Global and NonLocal keywords
In python the function creates a new symbol table for the arguents in the function thus the modifications made in the function are only valid till the end of the block, However we can change this with the help of the Keywords
'''
print("WIthout the use of the Keywords")
x=10
print(f"I am the x variable value before function call {x}")
def printLocal(x):
    x+=1
    print(f"I am the x variable value in function after update {x}")
printLocal(x)
print(f"I am the x variable value after fucntion call {x}")
printSpace()

print("Global Keyword")
glob_var = 10
print(f"I am the glob_var variable value before function call {glob_var}")
def printGlobal():
    '''In python if we want to change the value of a varible whose scope is global from inside the function block then we need to define the variable as global inside the function block
The global keyword then changes they symbol table of the function in which it was called.'''
    global glob_var
    glob_var+=1
    print(f"I am the x variable value in function after update {glob_var}")
printGlobal()
print(f"I am the x variable value after fucntion call {glob_var}")
printSpace()

print("NonLocal Keyword")
glob_var2 = 20
def outerFunction():
    '''In python we can define a fucntion within a funtion  if we want to update the value of the variable of the outer function in the inner function then we need to define it with nonlocal keyword'''
    global glob_var2
    outer_var = 10
    print(f"Value of the global glob_var2 in outer function {glob_var2}")
    print(f"Value of the outer function outer_var in outer function {outer_var}")
    def innerFunction():
        nonlocal outer_var
        outer_var+=1
        global glob_var2
        glob_var2+=1
        print(f"Value of the global glob_var2 in inner function {glob_var2}")
        print(f"Value of the inner function outer_var in outer function {outer_var}")
    innerFunction()
    print(f"Value of the outerFunction outer_var {outer_var}")
outerFunction()
print(f"Value to the glob_var outside function {glob_var2}")