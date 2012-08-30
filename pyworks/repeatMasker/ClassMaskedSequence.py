#coding:utf-8

def getMaskedSequenceSet(resultFileName):
        resultFile=open(resultFileName)
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
