x = 5
print(x)
def func():
    global x
    x=7
    print(x)

func()
print(x)

