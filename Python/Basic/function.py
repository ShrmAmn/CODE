def my_func(param1='default'):
    """
    Docstring goes here.
    """
    print(param1)
    
print(my_func)
# <function __main__.my_func>

my_func()
# default

my_func('new param')
# new param

my_func(param1='new param')
# new param

def square(x):
    return x**2
  
out = square(2)
print(out)
# 4
