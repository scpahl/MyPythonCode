#coding=utf-8
phonebook = {"Alice":"123","hl":"234","sbss":[1,2,3]};
#phonebook.clear();
#print phonebook;
dic = phonebook.copy();
phonebook["hl"] = "456";
phonebook["sbss"].remove(1);
print dic;

from copy import deepcopy
dicdeep = deepcopy(phonebook);
phonebook["sbss"].remove(2);
print phonebook;
print dicdeep;
print dict.fromkeys(phonebook);
print phonebook.get("sb","N/A"); #键不存在返回N/A,不指定第二个参数返回None
print phonebook.has_key("hl");
print phonebook.items();  #以元组列表返回
print phonebook.iteritems(); #返回迭代器
print phonebook.keys(); #键的列表
print phonebook.iterkeys(); #键的迭代器
print phonebook.values(); #值的列表
print phonebook.itervalues(); #值的迭代器
print phonebook.pop("hl"); #弹出指定键的值并移除
print phonebook;
print phonebook.popitem(); #随机弹出一个元组并移除（因为字典没有序号）
print phonebook.setdefault("hl","234");
print phonebook;
x = {"hl":"789","sbss":"456"};
phonebook.update(x);
print phonebook;