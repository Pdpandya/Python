pi = 3.14
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

sarea = 2 * pi * radius * (radius + height)
volume = pi * radius ** 2 * height
larea = 2 * pi * radius * height

print("The surface area of the cylinder is:",sarea)
print("The volume of the cylinder is:", volume)
print("The surface area of the cylinder is:",larea)
