# coding:utf-8
import sys
import os.path
class FASTQseq:
    def __init__(self, queryFile):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()

    def getSequenceName(self):
        return self.header1[1:].split(" ")[0]


    def writeMySelf(self,outputFile):
        outputFile.write(self.header1 + "\n")
        outputFile.write(self.baseSeq + "\n")
        outputFile.write(self.header2 + "\n")
        outputFile.write(self.qvSeq + "\n")

    def showMySelf(self):
        print self.header1
        print self.baseSeq
        print self.header2
        print self.qvSeq


def getMappedSequenceSet(SAMfileName):
    mappedSequenceSet=set()
    with open(SAMfileName) as SAMfile:
        for line in SAMfile:
            if line.startswith("@"):continue  #skip header
            mappedSequenceSet.add(line.split("\t")[0])
    return mappedSequenceSet

###################################
#### Main Part Start From Here. ###
###################################

if len(sys.argv)!=4:
    print "Invalid Parameters.\nUsage : removeMasked.py <inputFASTQfile_1> <inputFASTQfile_2> <repeatMaskerResultFile_1.out> <repeatMaskerResultFile_2.out> <outputFile_1.fastq> <outputFile_2.fastq>"
    exit()

#maskedSequenceSet=getMaskedSequenceSet('/Users/ytanizaw/Desktop/repealMasker/test.fa.out')
#outputFile=open('/Users/ytanizaw/Desktop/repealMasker/MaskedFastQ.fastq','w')
FASTQfileName1=sys.argv[1]
FASTQfileName2=sys.argv[2]
SAMfileName=sys.argv[2]
fastqFile1=open(FASTQfileName1)
fastqFile2=open(FASTQfileName2)

mappedSequenceSet=getMappedSequenceSet(SAMfileName)

outputFile1=open(os.path.splitext(FASTQfileName1)[0]+".unmapped.fastq",'w')
outputFile2=open(os.path.splitext(FASTQfileName2)[0]+".unmapped.fastq",'w')

i=0
while True:

    mySeq1=FASTQseq(fastqFile1)
    mySeq2=FASTQseq(fastqFile2)
    if mySeq1.header1=='':
        break

    if mySeq1.getSequenceName() in mappedSequenceSet:
        print mySeq1.getSequenceName() + " Removed."


    if (mySeq1.getSequenceName() not in mappedSequenceSet) and (mySeq2.getSequenceName() not in mappedSequenceSet):
        mySeq1.writeMySelf(outputFile1)
        mySeq2.writeMySelf(outputFile2)
#        mySeq1.showMySelf()
#        mySeq2.showMySelf()
    i +=1
    if i==10:break
fastqFile1.close()
fastqFile2.close()
outputFile1.close()
outputFile2.close()
