def hi() -> object:
    print("hello from function")


def hiByName(name):
    print("Hi Mr " + name)


def innerFunc(name):
    print("starting inner function")
    name = "Mr. " + name

    def helloByName():
        print("Hello from inner function: " + name)

    helloByName()


hi()
hiByName("Zakir")
innerFunc("Zak")
