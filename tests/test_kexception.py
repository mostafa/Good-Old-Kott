from kott.kcore.kexception import kException

@kException
def f(x):
    # always raises exception!
    print x/0

@kException
def g(x):
    # may raise exception (e.g. string is passed)
    print x/2

def else_func():
    print("else function is executed!")

def finally_func():
    print("finally function is executed!")

print ("---------- Testing kException Except & Else Block Execution  ----------")
g(2, else_function=else_func) # No exception is raised, so else_func is executed

print ("---------- Testing kException Finally Block Execution  ----------")
f(0, finally_function=finally_func) # ZeroDivisionError is raised, so finally_func is executed