import random
while 0==0:
    number = random.randint(1, 10)
    guess = int(input("Enter a number 1-10:"))
    
    if guess == number:
        print ("you picked the right number!")
        print("the number is", number)
        
    if guess>10:
        print("number is too large")
        
    if guess<0:
        print("number is too small")
        
    if guess !=number:
        print("wrong number")
        
        
    grade = float(input("enter your grade 0-100"))
    
    if grade>89.5:
        print("nice work! that's an A")
        
    elif grade>=79.5:
        print("solid work. that's a B")
        
    elif grade>=69.5:
        print("do better... that's a C")
        
    elif grade>=59.5:
        print("study more... that's a D")
        
    if grade>100:
        print("wow")
        
    else:
        print("that's an F.")
        
        