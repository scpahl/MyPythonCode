#coding=utf-8
class Person:
    def greet(self):
        print("hello ,world! I'm %s ." % self.name);

p1 = Person();
p2 = Person();
p1.name="hl";
p2.name="bb";
p1.greet();
p2.greet();