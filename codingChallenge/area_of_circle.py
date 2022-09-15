# radius = int(input('Please provide radius : '))
# area = 22/7*pow(radius,2)
#
# print(area)

# area of triangle

a = int(input('Provide one side: '))
b = int(input('Provide second side: '))
c = int(input('Provide third side: '))

s = (a+b+c)/2
squared_area = s*(s-a)*(s-b)*(s-c)

area = pow(squared_area, 1/2)

print(area)