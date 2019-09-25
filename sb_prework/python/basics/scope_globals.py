message = "b"


def greet():
    if True:
        message = "a"
    print(message)


def modifier():
    global message
    message = "c"


greet()
print(message)
modifier()
print(message)
