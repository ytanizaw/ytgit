#!/usr/local/bin/python
# coding:utf-8
from itertools import *
import sys

class FASTQ:
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

    @classmethod
    def FASTQreader(cls,fileName):
        with open(fileName) as f:
            while True:
                seq = FASTQ(f)
                if seq.header1=="": break
                yield seq

class SAM:
    def __init__(self,SAMFile,isPaired=True):
        self.seq1 = SAMFile.readline().strip()
        if isPaired:
            self.seq2 = SAMFile.readline().strip()

    @classmethod
    def SAMreader(cls,fileName,isPaired=True):
        with open(fileName) as f:
            for num,line in enumerate(f):
                if line.startswith("@"): continue
                else: break
        with open(fileName) as f:
            for _ in range(num):
                f.readline()   #skip header for "num" times
            while True:
                sam=SAM(f,isPaired)
                if sam.seq1=="":break
                yield sam

###################################
#### Main Part Start From Here. ###
###################################

if len(sys.argv)!=6:
    print "Invalid Parameters.\nUsage : extractUnmappedFASTQ.py <inputFASTQfile_1> <inputFASTQfile_2> <SAMfile> <outputFASTQfile_1> <outputFASTQfile_2>"
    exit()

FASTQfileName1, FASTQfileName2, SAMfileName, outputFASTQ1, outputFASTQ2 = sys.argv[1:6]

outputFile1=open(outputFASTQ1,'w')
outputFile2=open(outputFASTQ2,'w')
gen1, gen2, genSAM = FASTQ.FASTQreader(FASTQfileName1),FASTQ.FASTQreader(FASTQfileName2),SAM.SAMreader(SAMfileName, isPaired=True)

for i,(fastq1,fastq2,sam) in enumerate(izip(gen1, gen2, genSAM)):

    if (fastq1.getSequenceName() != sam.seq1.split("\t")[0]) or (fastq2.getSequenceName() != sam.seq2.split("\t")[0]):
        print "PAIR MISMATCH!!   LINE",i,fastq1.getSequenceName()
    if sam.seq1.split("\t")[2]=="*" and sam.seq2.split("\t")[2]=="*":  #remove seq if either read of the pair is mapped
        fastq1.writeMySelf(outputFile1)
        fastq2.writeMySelf(outputFile2)

outputFile1.close()
outputFile2.close()
