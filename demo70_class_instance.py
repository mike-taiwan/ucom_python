class Car:
    vender = 'Lexus'
    valid = True

print Car.vender, Car.valid
Car.function = True
print Car.function
c1 = Car()
c1.color='red'
print c1.vender, c1.valid, c1.function, c1.color
c2 = Car()
c2.capacity=7
print c2.vender, c2.valid, c2.function, c2.capacity
Car.maximum = 10000
print Car.maximum, c1.maximum, c2.maximum
