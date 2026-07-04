def login (func):
    def inner():
        username=input("username:")
        password=input("password:")
        if username=="sandeep" and password=="sandy":
            return func()
        else:
            return "invalid credentials"
    return inner
@login
def securefile():
    return "securefile"
print(securefile())
