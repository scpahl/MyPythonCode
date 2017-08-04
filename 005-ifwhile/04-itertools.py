#coding=utf-8
names = ["hl","xh","bb","wr"];
ages = [29,25,31,29];
for name,age in zip(names,ages): 
    print(name+"_"+str(age));
#zip可以压缩任意多的序列，以最短的为标准
# tem= zip(names,xrange(1,100));
# print(tem);
for index,value in enumerate(names):
    print(index);
    print(value);

for i in range(1,10):
    if i>10:
        break;
else:
    print("没找到得哇");