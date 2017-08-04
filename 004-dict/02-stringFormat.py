#coding=utf-8
phonebook = {"Alice":"123","hl":"234"};
print "hl's phoneNO is %(hl)s" % phonebook;
template = r'''
<head>%(title)s</head>
''';
data = {"title":"尼玛"};
print template % data;