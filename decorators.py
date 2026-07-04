def dec(func):
    def inner(n):
        print("starting this Function")
        print(func.__name__)
        func(n)
        print("ending this Function")
    return inner

@dec
def greet(name):
    print(f"hello {name}")
    print(greet.__name__)
greet("Sandeep")