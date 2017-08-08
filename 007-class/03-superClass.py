#coding=utf-8
class Person:
    def getName(self):
        print("");
    def getAge(self):
        print (10);

class Test:
    def test(self):
        print("test");

class Student(Person,Test):
    def getNo(self):
        print("07041050807");



stu = Student();
stu.getName();
stu.getAge();
stu.getNo();
stu.name = "hl";
print(issubclass(Student,Person));
print(Student.__bases__);
print(isinstance(stu,Person));
print (hasattr(stu,"test"));
print(getattr(stu,"name"));
setattr(stu,"age",12);
print(stu.age);