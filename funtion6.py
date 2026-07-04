def dec(x):
    def inner(m):
        print("helo")

        x(m)
        print("welcome to india")
        x(m)
    return inner




@dec #fun=def(fun)
def fun(name):
    print(f"Hello world:{name}")
fun("sandeeep")