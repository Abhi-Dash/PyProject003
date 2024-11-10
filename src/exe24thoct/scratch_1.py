##Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).

a = int(input("Enter first length of triangle: "))
b = int(input("Enter second length of triangle: "))
c = int(input("Enter third length of triangle: "))

if a==b==c:
    print ("This is an equilateral triangle as all sides are simillar")
elif a==b or b==c or c==a:
    print("This is an isosceles triangle as two sides are simillar")
else:
    print("This is an scalene triangle as no sides are simillar")

