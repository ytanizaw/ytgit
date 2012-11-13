#!/usr/local/bin/python
#coding:utf-8
import sys
class Fasta():
    '''a class which expresses each Fasta sequence.
    This class has 3 informations. Header, Base Sequence, Sequence Length
    '''
    def __init__(self):
        self.seq=''
        self.header=''
        self.length=0

    def __str__(self):
        return self.header

    @classmethod
    def FASTAreader(cls,inputfile):
        with open(inputfile) as f:
            firstEntry=True
            for line in f:
                if len(line.strip())==0:
                    #empty line
                    continue

                if firstEntry:
                    fasta=Fasta()
                    fasta.header=line.strip()
                    firstEntry=False
                    continue

                if line.startswith('>'):
                    fasta.length=len(fasta.seq)
                    yield fasta
                    fasta=Fasta()
                    fasta.header=line.strip()
                else:
                    fasta.seq += line.strip()
        #eof
        fasta.length=len(fasta.seq)
        yield fasta

    def writeSeq(self, outputFile,basePerLine=80):
        outputFile.write(self.header+"\n")
        for i in range((self.length)/basePerLine + 1):
            outputFile.write(self.seq[i*basePerLine:(i+1)*basePerLine]+"\n")

def main(inputFileName,outputFileName,basePerLine=80):
    outputFile=open(outputFileName,"w")
    for fastaSeq in Fasta.FASTAreader(inputFileName):
        fastaSeq.writeSeq(outputFile,basePerLine)
    outputFile.close()

if __name__=="__main__":
    if len(sys.argv) != 4:
        print "INVALID PARAMETER:  <input FASTA filename> <output FASTA filename> <bases per line>"
        exit()
    inputFileName,outputFileName,basePerLine=sys.argv[1:4]
    main(inputFileName,outputFileName,int(basePerLine))

