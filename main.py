def add():
    num1 = input("enter a number ")
    num2 = input("enter a number ")
    ans1 = float(num1) + float(num2)
    print(ans1)


def subtract():
    num3 = input("enter a number ")
    num4 = input("enter a number ")
    ans2 = float(num3) - float(num4)
    print(ans2)


def multiply():
    num5 = input("enter a number ")
    num6 = input("enter a number ")
    ans3 = float(num5) * float(num6)
    print(ans3)


def divide():
    num7 = input("enter a number ")
    num8 = input("enter a number ")
    ans4: float = float(num7) / float(num8)
    print(ans4)


question = input("add subtract multiply or divide ")
if question == "add":
    add()
if question == "subtract":
    subtract()
if question == "multiply":
    multiply()
if question == 'divide':
    divide()
