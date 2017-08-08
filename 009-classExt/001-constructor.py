#coding=utf-8
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age= age;

p1 = Person("hl",12);
print(p1.name);

class Student(Person):
    def __init__(self):
        Person.__init__(self,"hl",12);
        self.No="0701405";

st = Student();
print(st.age);