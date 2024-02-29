#Default Argument Values(rememnber Non default argument cannot follow default argumen)

def defArg(prompt = 'Give Input!! ', retries=4, reminder='Please try again!'):
    '''In Python, when defining a function, you can set default values for some or all of the arguments. This allows you to call the function with fewer arguments than it's defined to accept.'''
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)
#print(defArg.__doc__)
#print(defArg())

i = 6
def consArgEval(arg = i):
    '''Default values are evaluated at the time of function definition in the defining scope meaning first we set the value to i=6 -> then the function def is there -> the def stores the value of the default arg from i and this value will be used by the def throughout the entire execution(unless a new value is passed to the ).'''
    return arg
i = 5
#print(consArgEval.__doc__)
#print(consArgEval())

def mutArgEval(a,L=[]):
    '''If the default value is a mutable object like a list or dictionary, it's important to note that the default is evaluated only once. This can lead to unexpected behavior, especially with mutable objects that retain their state between function calls.'''
    L.append(a)
    return L
# print(mutArgEval.__doc__)
# print(mutArgEval(5))
# print(mutArgEval(5))

def mutArgEval2(a,L = None):
    '''To avoid this shared state between calls, you can use None as a default and create a new mutable object inside the function. This ensures that a new list is created for each function call, preventing unexpected shared state.'''
    if(L == None):
        L=[]
    L.append(a)
    return L
# print(mutArgEval2.__doc__)
# print(mutArgEval2(5))
# print(mutArgEval2(5))

def multiArgs(constant = 3, *args, **kwargs):
    '''
    Using a '*' signifies that the argument excepts multiple paraeters as input all the inputs taken by the arguments are stored in a tuple, even if the the parameter is a single list it will be stored in a tuple since tuples are immutable
    Using '**' signifies that it is a keyword args meaning when we pass a named paraeter it gets stored in a dictionary as key value pair 
    NOTE: If we pass a parameter with the same name as argument it does not get stored in kwargs rather it gets stored as the argument
    NOTE: A position is always followed first the constant arg then *args and then **kwargs
    NOTE: There are ways to restrict how we want to pass the parameters as positional only or keyword only with the help of * and \ refer to the docs '''
    return args #change according to need to understand
print(multiArgs.__doc__)
temp = multiArgs(1,1,2,3,3,constant2=2)
print(temp)