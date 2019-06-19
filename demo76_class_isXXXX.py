class Emp:
    pass


class Engineer(Emp):
    pass


class Pm(Emp):
    pass


class Hr(Emp):
    pass


emp1 = Emp()
engineer1 = Engineer()
pm1 = Pm()
hr1 = Hr()
staffs = [(emp1, "First Employee"), (engineer1, "First Engineer"), (pm1, "First PM"), (hr1, "First HR")]
emp_classes = [Emp, Pm, Hr, Engineer]

for staff, name in staffs:
    print '----------------------------'
    for emp_class in emp_classes:
        isA = isinstance(staff, emp_class)
        msg1 = 'is a' if isA else 'is not a'
        print name, msg1, emp_class.__name__

for c1 in emp_classes:
    for c2 in emp_classes:
        isSubclass = issubclass(c1, c2)
        message = '{0} a subclass of'.format('is' if isSubclass else 'is not')
        print c1.__name__, message, c2.__name__
