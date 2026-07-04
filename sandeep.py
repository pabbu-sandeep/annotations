def dec(x):
    def inner():
        print("Hii")
        x()
        print("Bye")
        x()
    return inner







@dec #fun=dec(fun)
def fun():
    print("sandeep")
fun()
