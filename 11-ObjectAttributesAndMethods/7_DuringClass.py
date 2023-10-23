class Student():

    album = 100000

    def __init__(self, name,surname,field):
        self.name = name
        self.surname = surname
        self.field = field
        self.album = Student.album
        Student.album += 1
    def __str__(self):
        return f"{self.name},{self.surname},{self.album},{self.field}"
    
student = Student("Jan","Kowalski","AI")
print(student)
student2 = Student("Jan","Kowalski","AI")
print(student2)
student3 = Student("Jan","Kowalski","AI")
print(student3)