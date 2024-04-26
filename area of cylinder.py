import math

# Input radius and height of the cylinder
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate surface area of the cylinder
surface_area = 2 * math.pi * radius * (radius + height)

# Calculate volume of the cylinder
volume = math.pi * radius ** 2 * height

# Calculate lateral surface area of the cylinder
lateral_area = 2 * math.pi * radius * height

print("The surface area of the cylinder is:",surface_area)
print("The volume of the cylinder is:", volume)
print("The surface area of the cylinder is:",lateral_area)
