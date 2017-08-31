#coding=utf-8
arr = list("helloSSS");
arr1 = list("BBB");
print(arr.count("S"));
arr.extend(arr1);
arr.pop(0);
arr.index("e");
arr.insert(0,"s");
arr.remove("S"); #改变了原集合
arr.reverse(); #改变了原集合
arr.sort(); #改变了原集合
temp= sorted(arr) #不改变原集合
ss= sorted("python");
print(ss);
ss.sort(cmp=cmp, key=len,reverse=True); #高级排序