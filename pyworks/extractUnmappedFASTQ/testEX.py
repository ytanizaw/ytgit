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
            for i in range(num):
                f.readline()   #skip header for "num" times
            while True:
                sam=SAM(f,isPaired)
                if sam.seq1=="":break
                yield sam


filename1="/Users/ytanizaw/Desktop/extractUnmappedFASTQ/ecoli/ecolitest_A.fastq"
filename2="/Users/ytanizaw/Desktop/extractUnmappedFASTQ/ecoli/ecolitest_B.fastq"
samfilename="/Users/ytanizaw/Desktop/extractUnmappedFASTQ/ecoli/sam/out.sam"

gen1, gen2, genSAM = FASTQ.FASTQreader(filename1),FASTQ.FASTQreader(filename2),SAM.SAMreader(samfilename, isPaired=True)
i=0
for i,(fastq1,fastq2,sam) in enumerate(izip(gen1, gen2, genSAM)):
    #print fastq1.getSequenceName(), fastq2.getSequenceName(),sam.seq1.split("\t")[0],sam.seq2.split("\t")[0]

    if (fastq1.getSequenceName() != sam.seq1.split("\t")[0]) or (fastq2.getSequenceName() != sam.seq2.split("\t")[0]):
        print "PAIR MISMATCH!!"
    if sam.seq1.split("\t")[2]!="*" or sam.seq2.split("\t")[2]!="*":  #remove seq if either read of the pair is mapped
        pass

        print i,"remove"
    else:
        pass
        #print "KEEP",fastq1.header1,fastq2.header1
#for fastq1,fastq2,sam in izip(genL):
#    i +=1
#    print fastq1.getSequenceName(),fastq2.getSequenceName(),sam.seq1[:10]
#    if i==10:break