# Import
import math

# Input Point_1
x1, y1 = map(float, input().split())

# Input Point_2
x2, y2 = map(float, input().split())

# Distance
distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

# Print Result
print("%.4f"%distance)

