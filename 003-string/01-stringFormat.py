#coding=utf-8

#d,i 带符号整数
#u 不带符号整数
#f 浮点数
#o 8进制
#x 16进制  X（大写16进制）
#e 科学计数 E（大写科学计数）
#g 如果指数大于-4或者小于精度值则和e相同，其他情况与f相同  G同上
#c 单个字符
#r repr字符串
#s str字符串
format = "hello %s,%s enouth for ya?";
values =("world","hot"); #不能用列表代替元组
print format % values;

format = "this is a number %-5.2f";  #-号表示左对齐（正号为结果前面加数字符号），5代表字符宽度，2代表精度
print format % 10.2222

from string import Template
format = Template("${x}，你个大${x}SS"); #如果变量为单词的一部分，必须用{}括起来
s= format.substitute(x="SB");
print s;
d={"x":"SB"};
s = format.substitute(d);
print s;
print '%.*s' % (5,"dafasdfasdf"); #如果精度或者宽度为*，则从元组中读取
print '%05.2f' % 0.32;  #不足5位，前面补0
