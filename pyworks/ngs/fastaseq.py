import TopN
import sys
class Fasta():
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

                if not line:
                    fasta.length=len(fasta.seq)
                    print fasta.seq
                    yield fasta


class TopN_FASTA(TopN.TopN):

    def add(self,FASTAseq):
        key=FASTAseq.length
        TopN.TopN.add(self,key, FASTAseq)
    def __str__(self):
        return str([item.header for item in self._items])


def testTopN():
    fileName='/Users/ytanizaw/Desktop/ParaRubber/PR_80_20_contig.fa'

    top5=TopN_FASTA(5)

    for i,seq in enumerate(Fasta.FASTAreader(fileName)):
        #print i,seq.header,seq.length
        top5.add(seq)
        if i==100:break

    print top5
    print top5[0].length

def n50(fileName=None,threshold=100):
    if fileName is None:
        fileName='/Users/ytanizaw/Desktop/ParaRubber/PR_80_20_contig.fa'
    seqList=[]
    for seq in Fasta.FASTAreader(fileName):
        if seq.length >= threshold:
            seqList.append(seq.length)
    seqList.sort(reverse=True)
    print seqList[:30]

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
    if len(sys.argv)>1:
        fileName=sys.argv[1]
    else:
        fileName = None
    if len(sys.argv)>2:
        threshold=int(sys.argv[2])
    else:
        threshold = 1000

    n50(fileName,threshold)
