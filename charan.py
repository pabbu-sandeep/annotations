def dec(x):
    def inner(m):
        print("Hello")
        x(m)
        print("bye")
        x(m)
    return inner
@dec
def fun(name):
    print(f"Darling,{name}")

fun("sandeep")
