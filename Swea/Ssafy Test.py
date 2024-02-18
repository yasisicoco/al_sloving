import math

start = (1, 1)
end = (2, 2)

a = abs(end[0] -start[0])
b = abs(end[1] - start[1])

r = math.sqrt(a**2 + b**2)
print(r)

radian = math.atan(b/a)
print(radian)

print(r, math.degrees(radian))