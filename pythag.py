print("Welcome this program will classify your triangle as right, acute or obtuse")
print("enter the largest side length last")
a = int(input("enter side length 1"))
b = int(input("enter side length 2"))
c = int(input("enter side length 3"))
if a>c or b>c:
    print("please enter the largest side length last")