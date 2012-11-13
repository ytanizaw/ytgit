#coding:utf-8

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

    def writeAsFasta(self,outputFile):
        outputFile.write(self.header1+"\n")
        BasesPerRow=60
        for i in range(len(self.baseSeq)/BasesPerRow + 1):
            outputFile.write(self.baseSeq[i*BasesPerRow:(i+1)*BasesPerRow]+"\n")
    def showAsFasta(self):
        print(self.header1)
        BasesPerRow=60
        for i in range(len(self.baseSeq)/BasesPerRow + 1):
            print(self.baseSeq[i*BasesPerRow:(i+1)*BasesPerRow])

    @classmethod
    def countSequences(tmpCls,inputFileName):
        count=0
        with open(inputFileName) as f:
            while f.readline():
                count += 1
        return count / 4

def getMaskedSequenceSet(*resultFileNames):
    maskedSequenceSet=set()
    for resultFileName in resultFileNames:
        resultFile=open(resultFileName)
        lines=resultFile.readlines()
        resultFile.close()
        for line in lines[3:]:
            maskedSequenceSet.add(line.split()[4])
    return maskedSequenceSet

def getMaskedSequenceSet_Pair(resultFileName1,resultFileName2):
        resultFile=open(resultFileName1)
        lines=resultFile.readlines()
        resultFile.close()
        maskedSequenceSet=set([])
        for line in lines[3:]:
            maskedSequenceSet.add(line.split()[4])
        return maskedSequenceSet

### Following part is no longer used.
class MaskedSequence:
    def __init__(self, resultFile):
        lines=resultFile.readlines()
        self.maskedSequenceSet=set([])
        for line in lines[3:]:
            self.maskedSequenceSet.add(line.split()[4])
        print len(self.maskedSequenceSet)

