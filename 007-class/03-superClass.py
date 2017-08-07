#coding=utf-8
class Person:
    def getName(self):
        print("");
    def getAge(self):
        print (10);
class Student(Person):
    def getNo(self):
        print("07041050807");

stu = Student();
stu.getName();
stu.getAge();
stu.getNo();
print(issubclass(Student,Person));
print(Student.__bases__);