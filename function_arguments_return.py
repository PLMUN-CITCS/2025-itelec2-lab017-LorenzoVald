import math

def circle_area(radius):
    """Calculate and return the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# Define the radius value
radius_value = 5

# Call the function
area_result = circle_area(radius_value)

# Print the result
print(f"The area of a circle with radius {radius_value} is: {area_result:.2f}")