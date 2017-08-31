class MyException(Exception):
    pass;

try:
    raise MyException;
except (MyException) as e:
    print("ss");

