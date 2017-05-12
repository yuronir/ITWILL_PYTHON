class student(object):
    def __init__(self,name,year,class_num,student_id):
        self.name = name
        self.year = year
        self.class_num = class_num
        self.student_id = student_id

    def introduce_myself(self):
        return '{}, {}학년 {}반 {}번'.format(self.name, self.year, self.class_num, self.student_id)

student_1 = student('김인호',2,3,35)
student_2 = student('최영희',3,1,23)
print(student.introduce_myself(student_1))