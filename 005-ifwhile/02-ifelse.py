#coding=utf-8
#[] None 0 "" () {} False都视作为假，其它都为真
print(bool(""));
if {}:
    print("sb");
else:
    print("ss");
a = 10;
if a<10:
    print("you");
elif a==10:
    print("SB");
else:
    print("SS");

x=y={"hl":"ss"};
print(x is y);
print(x is not y);
name = {} or "SBSS";
print(name);
age =101;
assert 0<age<100;