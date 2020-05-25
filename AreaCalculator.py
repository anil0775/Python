# This program computes the area of following shapes
# Circle
# Triangle
print "Calculator Program is Starting"
print "Enter the shape whose area is to be calculated"
shape = raw_input("Enter C for Circle or T for Triangle: ")
if shape == "C" or shape == "c":
  radius = float(raw_input("Enter radius of the circle: "))
  area = 3.14159 * radius
  print "Area of Circle is: " + str(area)
elif shape == "T" or shape == "t" :
  base = float(raw_input("Enter base of the triangle: "))
  height = float(raw_input("Enter height of the triangle: "))
  area = 0.5 * base * height
  print "Area of Triangle is: " + str(area)
else:
  print "Invalid input"
print "Calculator Program is terminating"
