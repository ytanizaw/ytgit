# coding:utf-8
import sys

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


def getMaskedSequenceSet(*resultFileNames):
    maskedSequenceSet=set()
    for resultFileName in resultFileNames:
        resultFile=open(resultFileName)
        lines=resultFile.readlines()
        resultFile.close()
        for line in lines[3:]:
            maskedSequenceSet.add(line.split()[4])
    return maskedSequenceSet

###################################
#### Main Part Start From Here. ###
###################################

if len(sys.argv)!=7:
    print "Invalid Parameters.\nUsage : removeMasked.py <inputFASTQfile_1> <inputFASTQfile_2> <repeatMaskerResultFile_1.out> <repeatMaskerResultFile_2.out> <outputFile_1.fastq> <outputFile_2.fastq>"
    exit()
#maskedSequenceSet=getMaskedSequenceSet('/Users/ytanizaw/Desktop/repealMasker/test.fa.out')
#outputFile=open('/Users/ytanizaw/Desktop/repealMasker/MaskedFastQ.fastq','w')
#fastqFile=open('/Users/ytanizaw/Desktop/repealMasker/test.fq')
fastqFile1=open(sys.argv[1])
fastqFile2=open(sys.argv[2])

maskedSequenceSet=getMaskedSequenceSet(sys.argv[3],sys.argv[4])
outputFile1=open(sys.argv[5],'w')
outputFile2=open(sys.argv[6],'w')

#print len(maskedSequenceSet)
while True:

    mySeq1=FASTQseq(fastqFile1)
    mySeq2=FASTQseq(fastqFile2)
    if mySeq1.header1=='': break
    #mySeq.showMySelf()

    if (mySeq1.getSequenceName() not in maskedSequenceSet) and (mySeq2.getSequenceName() not in maskedSequenceSet):
        mySeq1.writeMySelf(outputFile1)
        mySeq2.writeMySelf(outputFile2)


fastqFile1.close()
fastqFile2.close()
outputFile1.close()
outputFile2.close()
