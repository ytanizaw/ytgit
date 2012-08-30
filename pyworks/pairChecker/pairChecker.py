#coding:utf-8
class FASTQseq:

    @classmethod
    def generateFastqSeq(cls,inputFile):
        while True:
            tmpSeq=FASTQseq()
            tmpSeq.header1=inputFile.readline().strip()
            if tmpSeq.header1=='':
                break
            tmpSeq.baseSeq=inputFile.readline().strip()
            tmpSeq.header2=inputFile.readline().strip()
            tmpSeq.qvSeq=inputFile.readline().strip()
            yield tmpSeq

    def whichPair(self):
        return self.header1[1:].split(" ")[1]

    def showMySelf(self):
        print self.header1
        print self.baseSeq
        print self.header2
        print self.qvSeq

    def getSeqName(self):
        return self.header1[1:].split(" ")[0]

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
with open(fileName1) as file1, open(fileName2) as file2:
    genseq2=FASTQseq.generateFastqSeq(file2)

    for i,seq1 in enumerate(FASTQseq.generateFastqSeq(file1)):
        seq2=genseq2.next()
        #   print i, seq1.getSeqName(), seq2.getSeqName()
        if seq1.getSeqName()==seq2.getSeqName() and seq1.whichPair()=='1:N:0:' and seq2.whichPair()=='2:N:0:':

            pass
        else:
            print "pair mismatch in " + str(i) + "th sequence"
            flagInvalid=True
if flagInvalid:
    print "mismatch"
else:
    print "OK"


