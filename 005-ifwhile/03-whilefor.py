#coding=utf-8
a=10;
while a:
    print(a);
    a-=1;

# name = '';
# while not name.strip():
#     name = input("输入个名字哇");
# print(name);

words = list("你是一个大SB");
for word in words:
    print(word);

for num in range(1,11):
    print(num);
d = {"name":"hl","age":16};
for key in d:
    print(key+"_"+str(d[key]));