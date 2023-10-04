class MyStudentClass:
    "Common base class for all students"
    StdCount = 0
    def __init__(self, Name, RegNo, Dept, Age):
        self.Name = Name
        self.RegNo = RegNo
        self.Dept = Dept
        self.Age = Age
        MyStudentClass.StdCount += 1

    def displayCount(self):
        print("Total Number of Student is",MyStudentClass.StdCount)

    def displayStudents(self):
        print("Name:",self.Name)
        print("Reg Number:",self.RegNo)
        print("Department:",self.Dept)
        print("Age:",self.Age)

stud1 = MyStudentClass("Stephen", "CSC/2016/069", "Computer Science", 20)
stud1.displayCount()
stud1.displayStudents()
