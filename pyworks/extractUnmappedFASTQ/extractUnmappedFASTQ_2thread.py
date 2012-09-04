#!/usr/local/bin/python
# coding:utf-8
import sys
import threading
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


class extract(threading.Thread):
    def __init__(self, inputFASTQ, mappedSequenceSet, outputFASTQ):
        threading.Thread.__init__(self)
        #self.setDaemon(True)
        self.inputFASTQ=inputFASTQ
        self.mappedSequenceSet=mappedSequenceSet
        self.outputFASTQ=outputFASTQ

    def run(self):
        infile=open(self.inputFASTQ)
        outfile=open(self.outputFASTQ, "w")

        while True:
            seq=FASTQseq(infile)
            if seq.header1=='':   break
            if seq.getSequenceName() not in self.mappedSequenceSet:
                seq.writeMySelf(outfile)

        infile.close()
        outfile.close()

###################################
#### Main Part Start From Here. ###
###################################

if len(sys.argv)!=6:
    print "Invalid Parameters.\nUsage : extractUnmappedFASTQ.py <inputFASTQfile_1> <inputFASTQfile_2> <SAMfile> <outputFASTQfile_1> <outputFASTQfile_2>"
    exit()

FASTQfileName1, FASTQfileName2, SAMfileName, outputFASTQ1, outputFASTQ2 = sys.argv[1:6]

mappedSequenceSet=getMappedSequenceSet(SAMfileName)

thread1=extract(FASTQfileName1, mappedSequenceSet, outputFASTQ1)
thread2=extract(FASTQfileName2, mappedSequenceSet, outputFASTQ2)
thread1.start()
thread2.start()
