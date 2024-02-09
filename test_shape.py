import shape

my_shape1 = shape.Shape()
my_shape1.set_fillColor("Red")

print(my_shape1.get_fillColor())

my_shape2 = shape.Rectangle()
my_shape2.set_fillColor("Blue")

my_shape2_area = my_shape2.calculate_area()
print("Area of the shape is ", my_shape2_area)
print("Perimeter of the shape is ", my_shape2.calculate_perimeter())

print(my_shape2.get_fillColor())

my_shape3 = shape.Triangle()
print("Area of the triange is ", my_shape3.calculate_area())
print("Perimeter of the triangle is ", my_shape3.calculate_perimeter())