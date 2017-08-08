#coding=utf-8
#raise Exception;
try:
    ss=1/0;
except (TypeError,NameError) as e: #2.7中为,e
    print(e);
except ZeroDivisionError as e:
    print(e);
else:
    print("SS");
finally:
    print("大SB");