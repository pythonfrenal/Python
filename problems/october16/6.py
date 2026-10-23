def uppercase_decorator(func):
    def wrapper():
        name = name.upper()
        return func(name)
    return wrapper

@uppercase_decorator
def greet(name):
    print("Hello, ")


greet("shahin")




def remove_duplicates():
    
