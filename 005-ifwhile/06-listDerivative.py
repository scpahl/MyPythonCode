#coding=utf-8
number = [x*x for x in range(4)];
print(number);
strlist= ["hl","xh","bb","wr"];
result = [(x,y) for x in number for y in strlist if x==y];
print(result);