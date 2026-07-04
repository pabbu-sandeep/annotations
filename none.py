x=30
def fun():
    print(x)

    def fun3():

        print(x)
    return fun3()
fun()
print(x)
