#coding=utf-8
def checkIndex(key):
    """
    检查索引的合法性
    """
    if not isinstance(key,int):raise TypeError;
    if key<0:raise IndexError;

class MySequeuce:
    def __init__(self,start=0,step=1):
        self.start=0;
        self.step = step;
        self.change={};
    def __getitem__(self, key):
        checkIndex(key);
        try:self.change[key];
        except KeyError:
            return self.start + key*self.step;
    
    def __setitem__(self, key, value):
        checkIndex(key);
        self.change[key] = value;

ss = MySequeuce(0,2);
print(ss[4]);