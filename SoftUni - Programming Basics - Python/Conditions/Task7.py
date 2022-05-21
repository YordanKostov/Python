from math import pi
shape = input()

if shape == "square":
    side = float(input())
    print(side * side)
elif shape == 'rectangle':
    sidea = float(input())
    sideb = float(input())
    print(sidea * sideb)
elif shape == 'circle':
    radius = float(input())
    print(f"{pi * radius * radius:.3f}")
elif shape == 'triangle':
    side = float(input())
    height = float(input())
    print(0.5 * side * height)

