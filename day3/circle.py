import argparse
import math

parser = argparse.ArgumentParser(description="Perform calculations for a circle")
parser.add_argument("radius", type=float, help="Radius of the circle")

args = parser.parse_args()
radius = args.radius
circumference=2*(math.pi)*radius
area=((math.pi)*radius**2)

print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")