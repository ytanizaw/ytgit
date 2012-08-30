#coding:utf-8

# usage
# removeMasked.py <inputFASTQfile> <repeatMaskerResultFile,out> <outputFile.fastq>
#

class FASTQseq:
    def __init__(self, queryFile):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()

    def getSequenceName(self):
        return self.header1[1:].split()[0]


    def writeMySelf(self,outputFile):
        outputFile.write(self.header1+"\n")
        outputFile.write(self.baseSeq+"\n")
        outputFile.write(self.header2+"\n")
        outputFile.write(self.qvSeq+"\n")

    def showMySelf(self):
        print self.header1
        print self.baseSeq
        print self.header2
        print self.qvSeq


def getMaskedSequenceSet(resultFileName):
        resultFile=open(resultFileName)
        lines=resultFile.readlines()
        resultFile.close()
        maskedSequenceSet=set()
        for line in lines[3:]:
            maskedSequenceSet.add(line.split()[4])
        return maskedSequenceSet


import sys

if len(sys.argv)!=4:
    print "Invalid Parameters.\nUsage : removeMasked.py <inputFASTQfile> <repeatMaskerResultFile.out> <outputFile.fastq>"
    exit()
#maskedSequenceSet=getMaskedSequenceSet('/Users/ytanizaw/Desktop/repealMasker/test.fa.out')
#outputFile=open('/Users/ytanizaw/Desktop/repealMasker/MaskedFastQ.fastq','w')
#fastqFile=open('/Users/ytanizaw/Desktop/repealMasker/test.fq')
fastqFile=open(sys.argv[1])
maskedSequenceSet=getMaskedSequenceSet(sys.argv[2])
outputFile=open(sys.argv[3],'w')

while True:

    mySeq=FASTQseq(fastqFile)
    if mySeq.header1=='': break
    #mySeq.showMySelf()

    if mySeq.getSequenceName() not in maskedSequenceSet:
        mySeq.writeMySelf(outputFile)


fastqFile.close()
outputFile.close()
