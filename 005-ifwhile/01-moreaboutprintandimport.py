#coding=utf-8
print('age:'+",",42);
#import module
#from module import func1,func2,func3
#from module import *
#import module as alias
#from module import func as alias

import math as sbss
print(sbss.sqrt(4));

x,y,z = 1,2,3;
print(x,y,z);
x,y = y,x;  #交换变量的值
print(x,y);
phonebook = {"Alice":"123","hl":"234","sbss":[1,2,3]};
key,value = phonebook.popitem();
print(key,value);
# a,b,c* = [1,2,3,4,5];
# print(a,b,c);