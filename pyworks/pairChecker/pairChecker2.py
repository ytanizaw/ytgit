#!/usr/local/bin/python
#coding:utf-8
class FASTQseq:

    def __init__(self, queryFile):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()

    def showMySelf(self):
        print self.header1
        print self.baseSeq
        print self.header2
        print self.qvSeq

    def getSeqName(self):
        return self.header1[1:].split(" ")[0]

    def whichPair(self):
        return self.header1[1:].split(" ")[1]

    @classmethod
    def countSequences(tmpCls,inputFileName):
        count=0
        with open(inputFileName) as f:
            while f.readline():
                count += 1
        return count / 4


import sys
fileName1=sys.argv[1]
fileName2=sys.argv[2]
flagInvalid=False

file1=open(sys.argv[1])
file2=open(sys.argv[2])
i=1
while True:

    seq1=FASTQseq(file1)
    seq2=FASTQseq(file2)
    if seq1.header1=='': break
    #mySeq.showMySelf()



    if seq1.getSeqName()==seq2.getSeqName() and seq1.whichPair()=='1:N:0:' and seq2.whichPair()=='2:N:0:':
        pass
    else:
        print "pair mismatch in " + str(i) + "th sequence"
        flagInvalid=True
    i += 1

if flagInvalid:
    print "mismatch"
else:
    print "OK"


