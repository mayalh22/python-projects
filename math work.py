import math

while True:
    choice1 = input("what should i solve? (quadratic, add, sub, mul, div, exp, sqrt, sin, cos, tan, midpoint, distance) or type 'exit' to quit: ").strip().lower()
    
    if choice1 == "quadratic":
        a = int(input("enter a: "))
        b = int(input("enter b: "))
        c = int(input("enter c: "))
        top = (b**2) - (4 * a * c)
        if top < 0:
            print("no real roots.")
        else:
            sqrt_top = top**0.5
            ans1 = (-b + sqrt_top) / (2 * a)
            ans2 = (-b - sqrt_top) / (2 * a)
            print("the answers are", ans1, "and", ans2)

    elif choice1 == "add":
        add1 = int(input("what is your first number? "))
        add2 = int(input("what is your second number? "))
        total = add1 + add2
        print(f"{add1} + {add2} = {total}")

    elif choice1 == "sub":
        sub1 = int(input("what is your first number? "))
        sub2 = int(input("what is your second number? "))
        difference = sub1 - sub2
        print(f"{sub1} - {sub2} = {difference}")

    elif choice1 == "mul":
        mul1 = int(input("what is your first number? "))
        mul2 = int(input("what is your second number? "))
        product = mul1 * mul2
        print(f"{mul1} * {mul2} = {product}")

    elif choice1 == "div":
        div1 = int(input("what is your first number? "))
        div2 = int(input("what is your second number? "))
        if div2 == 0:
            print("no dividing by zero.")
        else:
            quotient = div1 / div2
            print(f"{div1} / {div2} = {quotient}")

    elif choice1 == "exp":
        base = int(input("what is your base? "))
        exponent = int(input("what is your exponent? "))
        result = base ** exponent
        print(f"{base} ^ {exponent} = {result}")

    elif choice1 == "sqrt":
        number = float(input("what number would you like to find: "))
        if number < 0:
            print("sqrts of negatives r not allowed.")
        else:
            result = math.sqrt(number)
            print(f"the square root of {number} is {result}")

    elif choice1 == "sin":
        angle = float(input("enter the angle in degrees: "))
        result = math.sin(math.radians(angle))  # Convert degrees to radians
        print(f"the sin of {angle} degrees is {result}")

    elif choice1 == "cos":
        angle = float(input("enter the angle in degrees: "))
        result = math.cos(math.radians(angle))  # Convert degrees to radians
        print(f"the cos of {angle} degrees is {result}")

    elif choice1 == "tan":
        angle = float(input("Enter the angle in degrees: "))
        result = math.tan(math.radians(angle))  # Convert degrees to radians
        print(f"The tangent of {angle} degrees is {result}")

    elif choice1 == "midpoint":
        x1 = int(input("Enter the first x coordinate: "))
        x2 = int(input("Enter the second x coordinate: "))
        y1 = int(input("Enter the first y coordinate: "))
        y2 = int(input("Enter the second y coordinate: "))
        midx = (x1 + x2) / 2
        midy = (y1 + y2) / 2
        print(f"the midpoint ({midx}, {midy})")

    elif choice1 == "distance":
        x1 = int(input("enter the first x coordinate: "))
        x2 = int(input("enter the second x coordinate: "))
        y1 = int(input("enter the first y coordinate: "))
        y2 = int(input("enter the second y coordinate: "))
        distance = (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
        print(f"the distance is {distance} units")

    elif choice1 == "exit":
        print("bye!!")
        break 

    else:
        print("Invalid choice. Please select a valid option.")

