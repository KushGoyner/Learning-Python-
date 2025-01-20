username = "kush"

def hello():
    username = "shyam"
    print(username)

hello()

print(username)


def hello2():
    print(username)  # find username in upper heriarcy

hello2()

x = 99  #Global variable it can be accessed from anywhere

def fun(y):
    z = x+y
    return z

print(fun(1))

def fun2():
    x = 88  # Ghar ka X not golbally X

print(x)


def func3():
    global x  # not the global X is present here
    x = 11

func3()
print(x)

def func4():
    x = 88
    def f1():
        print(x)
    f1()
func4()


# CLOSERS

def func5():
    x = 77
    def f2():
        print(x)
    return f2

myResult  = func5()

myResult()




def func6(num):
    def f3(x):
        return x**num
    return f3

f = func6(2)
g = func6(3)


print(f(3))
print(g(3))
