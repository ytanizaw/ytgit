a=(8,8,8)
b=(306,2156,2156)
c=(10,10,3)

print min(a)
print a.index(min(a))

myset=set()
myset.add(10)
myset.add(5)
myset.add(2)
myset.add(9)
myset.add(11)
myset.add(12)
myset.add(9)

print sorted(myset)

L1=[1,5,6]
L2=[1,3,5,6]
L3=[1,3,6]

import re
line="scaffold_1    8    .    GAA    GAAA    14.4    .    INDEL;DP=2;VDB=0.0192;AF1=1;AC1=2;DP4=0,0,2,0;MQ=29;FQ=-40.5    GT:PL:GQ    1/1:53,6,0:10"
pat=re.compile("DP*=\\d+")
pat=re.compile("(DP.?=\\d+).*?(DP.*?=\\d+)")
pat=re.compile(r"FQ=\-?\d+\.?\d*")

m= pat.search(line)
print m.group(0)
#print m.group(1)

test="REF"
#print "".join([["\t" + name + str(i) for i in range(1,12)] for name in ["ALT","DEPTH","QUAL","FQ"]])
print "".join(["\t"+test + str(i) for i in range(1,11)])
fileList=[1,4,6,7,7]
print "".join(["".join(["\t"+name + str(i+1) for i in range(len(fileList))]) for name in ["ALT","DEPTH","QUAL","FQ"]])
print "\t".join(["\t".join([name + str(i+1) for i in range(len(fileList))]) for name in ["ALT","DEPTH","QUAL","FQ"]])
