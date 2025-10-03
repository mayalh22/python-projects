print("welcome!  this program will tell you what point your quadrant is in")
x = int(input("type your x coordinate:"))
y = int(input("type your y coordinate:"))

if x>0 and y>0:
    print("your point is in quadrant I")
if x<0 and y<0:
    print("your point is in quadrant III")
if x>0 and y<0:
    print("your point is in quadrant IV")
if x<0 and y>0:
    print("your point is in quadrant II")
if x==0 and y!=0:
    print("your point is on the y-axis")
if y==0 and x!= 0:
    print("your point is on the x-axis")
if x==0 and y==0:
    print("your point is on the origin")
