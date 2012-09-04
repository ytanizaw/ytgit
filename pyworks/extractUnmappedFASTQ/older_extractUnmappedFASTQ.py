#!/usr/local/bin/python
# coding:utf-8
import sys

class FASTQseq:
    def __init__(self, queryFile):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()

    def getSequenceName(self):
        if " " in self.header1:
            return self.header1[1:].split(" ")[0]
        else:
            return self.header1[1:-2]

    def writeMySelf(self,outputFile):
        outputFile.write(self.header1+"\n")
        outputFile.write(self.baseSeq+"\n")
        outputFile.write(self.header2+"\n")
        outputFile.write(self.qvSeq+"\n")


def getMappedSequenceSet(SAMfileName):
    mappedSequenceSet=set()
    with open(SAMfileName) as SAMfile:
        for line in SAMfile:
            if line.startswith("@") or line.split("\t")[2]=="*":  continue  #skip header and unmapped read
            if line.endswith("/2\n"):
                line = line[:-3]
            mappedSequenceSet.add(line.split("\t")[0])
    return mappedSequenceSet

###################################
#### Main Part Start From Here. ###
###################################

if len(sys.argv)!=6:
    print "Invalid Parameters.\nUsage : extractUnmappedFASTQ.py <inputFASTQfile_1> <inputFASTQfile_2> <SAMfile> <outputFASTQfile_1> <outputFASTQfile_2>"
    exit()

FASTQfileName1, FASTQfileName2, SAMfileName, outputFASTQ1, outputFASTQ2 = sys.argv[1:6]

fastqFile1=open(FASTQfileName1)
fastqFile2=open(FASTQfileName2)
mappedSequenceSet=getMappedSequenceSet(SAMfileName)
outputFile1=open(outputFASTQ1,'w')
outputFile2=open(outputFASTQ2,'w')

while True:

    mySeq1=FASTQseq(fastqFile1)
    mySeq2=FASTQseq(fastqFile2)
    if mySeq1.header1=='':   break

#    if mySeq1.getSequenceName() in mappedSequenceSet:
#        print mySeq1.getSequenceName() + " Removed."

    if (mySeq1.getSequenceName() not in mappedSequenceSet) and (mySeq2.getSequenceName() not in mappedSequenceSet):
        mySeq1.writeMySelf(outputFile1)
        mySeq2.writeMySelf(outputFile2)

fastqFile1.close()
fastqFile2.close()
outputFile1.close()
outputFile2.close()
