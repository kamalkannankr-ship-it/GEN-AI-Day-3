#circumference and radius of the circle using dictionary
circle={}

for i in range (3):
    radius =float(input("Enter a radius of a circle:"))
    circumference=2*3.14*radius
    circle[radius]=circumference

print("\n dictinary containg radius and circumferance")

print(circle)
