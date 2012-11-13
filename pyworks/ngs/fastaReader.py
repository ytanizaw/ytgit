#!/usr/local/bin/python
#coding:utf-8
import TopN
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

    def writeSeq(self, outputFile):
        outputFile.write(self.header+"\n")
        BasesPerRow=60
        for i in range((self.length)/BasesPerRow + 1):
            outputFile.write(self.seq[i*BasesPerRow:(i+1)*BasesPerRow]+"\n")

class TopN_FASTA(TopN.TopN):

    def add(self,FASTAseq):
        key=FASTAseq.length
        TopN.TopN.add(self,key, FASTAseq)
    def __str__(self):
        return str([item.header for item in self._items])


def getTopN(fileName,N=5):
#    fileName='/Users/ytanizaw/Desktop/ParaRubber/PR_80_20_contig.fa'

    topN=TopN_FASTA(N)

    for i,seq in enumerate(Fasta.FASTAreader(fileName)):
        #print i,seq.header,seq.length
        topN.add(seq)

    for fastaSeq in topN:
        print fastaSeq.header
        print fastaSeq.seq

def stat(fileName=None,threshold=100):
    if fileName is None:
        fileName='/Users/ytanizaw/Desktop/ParaRubber/PR_80_20_contig.fa'
    seqList=[]
    for seq in Fasta.FASTAreader(fileName):
        if seq.length >= threshold:
            seqList.append(seq.length)
    seqList.sort(reverse=True)
    print "LENGTH of 10 LONGEST SEQUENCES: ", seqList[:10]

    TotalLength=sum(seqList)
    print "For SEQUENCE LONGER THAN",threshold,"bp"
    print "TOTAL SEQUENCE LENGTH bp: ",TotalLength
    print "TOTAL SEQUENCE NUMBER #: ",len(seqList)
    tmpLength=0
    for x in seqList:
        tmpLength += x
        if tmpLength >= TotalLength/2:
            print "N50: ",x
            break

if __name__=="__main__":
    if len(sys.argv)!=4:
        print "INVALID NUMBER OF ARGS. Give command, int, filename"
        print "command { top  or  stat }"
        print "int { Num of Sequences for top  or   Minimum Sequence Length for stat }"
        print "filename { file name for FASTA }"
        exit()
    command, num, fileName = sys.argv[1:4]
    if command=="top":
        getTopN(fileName, int(num))
    elif command=="stat":
        stat(fileName, int(num))
    else:
        print "INVALID COMMAND NAME. Select top or stat."
        exit()
