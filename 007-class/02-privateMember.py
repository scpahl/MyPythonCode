#coding=utf-8
class Person:
    def __privateMethod():
        print("private");
    _age=0; ##import*不会导入_开头的成员 
p = Person();
#p.__privateMethod() 无法访问
Person._Person__privateMethod();
print(p._age);