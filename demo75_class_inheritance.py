class Emp:
    gradeLevel = 6

    def startWork(self):
        pass

    def endWork(self):
        pass

    pass


class RD(Emp):
    def __init__(self):
        self.currentGrade = self.gradeLevel

    def startWork(self):
        print "[%d] start R&D work" % self.currentGrade

    def endWork(self):
        print "[%d] end R&D work" % self.currentGrade
rd1 = RD()
print Emp.gradeLevel, RD.gradeLevel, rd1.currentGrade, rd1.gradeLevel
# rd1.currentGrade = 8
Emp.gradeLevel = 8
print Emp.gradeLevel, RD.gradeLevel, rd1.currentGrade, rd1.gradeLevel
rd1.startWork()
rd1.endWork()
