#coding=utf-8
import string;
print(string.digits;
print(string.letters;
print(string.lowercase;
print(string.uppercase;
print(string.printable;
print(string.punctuation;


myStr = "this is a python a program ";
print(myStr.find("a",9,100)); 
print(myStr.rfind('a')); 
print(myStr.index("a",9,100));
print(myStr.rindex("a"));
print(myStr.startswith("a"));
print(myStr.endswith("m"));
print(myStr.count('a'));
print(','.join(["a","b","c"])); #注意：只能join字符串列表
print(myStr.lower());
print(myStr.upper());
print(myStr.islower());
print(myStr.isupper());
print(myStr.title());
print(myStr.capitalize());
print(myStr.replace("a","A"));
print(myStr.split());
print(myStr.strip());
print(string.capwords(myStr));
from string import maketrans;
table= string.maketrans("is","as");
print(myStr.translate(table));