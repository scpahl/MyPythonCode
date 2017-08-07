#coding=utf-8
class Person:
    def greet(self):
        self.age = 10;
        print("hello ,world! I'm %s ." % self.name);

p1 = Person();
p2 = Person();
p1.name="hl";
p2.name="bb";
p1.greet();
p2.greet();
p1.greet = lambda :print("hello");  #
p1.greet();
p2.greet();
print(p1.age);
print(".............................................")


foo = lambda x:x+1;
print(foo(1));