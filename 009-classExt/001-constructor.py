#coding=utf-8
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age= age;

p1 = Person("hl",12);
print(p1.name);

class Student(Person):
    def __init__(self):
        super(Student,self).__init__("hl",21);
        self.No="0701405";

st = Student();
print(st.age);