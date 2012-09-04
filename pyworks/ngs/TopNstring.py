#!/usr/local/bin/python
#coding:utf8
from TopN import TopNstring

a="henry"
b="Tomson"
c="Cinderella"
d="Edward"
e="tom"
f="John"
g="Jonnathan"

top4=TopNstring(4)
top4.add(a)
top4.add(b)
top4.add(c)
top4.add(d)
top4.add(e)
top4.add(f)
top4.add(g)
print top4
del top4[2]
c="ccdderara"
print top4
#top4._items[0]="Cinderalla2"

print b
print c
print top4
top5=TopNstring(5)
top5.add("hanako")
top5.add("Ryoutarou")
gen= top5.items()
top5.add("Ken")
top5.add("Maika")
top5.add("Tom")
print top5

top5.add("Yasuhiro")
top5.add("Satomi")

print top5
iter(top5)
print top5.next()
for i,name in enumerate(top5):
    print i,name
