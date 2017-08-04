#coding=utf-8
def myname(name):
    "这是一个很牛B的方法"
    print(name);    

def calculate_number(x,y=5):
    return x*y;

def show_name(*names):
    print(names);

def testParam(x,y,z,*p1,**p2):
    print(x,y,z);
    print(p1);
    print(p2);

myname("hl");
print(myname.__doc__);
help(myname);

print(calculate_number(x=2));
show_name("hl","gd");
testParam(1,2,3,4,5,ss=1,yy=2);
print(calculate_number(*[1,2])); #如果传字典用**{}