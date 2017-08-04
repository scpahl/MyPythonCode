#coding=utf-8
x = 1;
scope =vars();
print(scope);
scope["x"]+=1;
print(x);
#函数会创建作用域

def test(x):
    print(x+globals()["x"]);
test(2);

def test2():
    global x;
    x=x+1;
print(x);

def out_method(p1):
    def inner_menthod(p2):
        return p1*p2;
    return inner_menthod;

print(out_method(2)(3));

arr =[1,2,3,3,4,4,5,5,6,6,7,7,8]
print(list(filter(lambda x:x%2==0,arr)));