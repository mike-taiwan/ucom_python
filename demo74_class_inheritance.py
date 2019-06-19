class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass


class RD(Emp):
    pass


class PM(Emp):
    pass


print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
RD.gradeLevel = 7
print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
Emp.gradeLevel = 8
print "RD, PM, Emp grade level=", RD.gradeLevel, PM.gradeLevel, Emp.gradeLevel
