class MyClass:
    pass
print "my class type:", type(MyClass)
i1 = MyClass()
print "i1 type:", type(i1)
print "i1 class:", i1.__class__
print "i1 class bases:", i1.__class__.__bases__
print "i1 type equal to myClass?", type(i1) == MyClass


print "********"
class MyClass2(object):
    pass


print "my class type:", type(MyClass2)
i2 = MyClass2()
print "i2 type:", type(i2)
print "i2 class:", i2.__class__
print "i2 class bases:", i2.__class__.__bases__
print "i2 type equal to myClass?", type(i2) == MyClass2
