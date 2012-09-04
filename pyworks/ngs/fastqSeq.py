#coding:utf-8

class FASTQseq:
    def __init__(self, queryFile, qvType=33):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()
        self.qvType = qvType
        self.isRemoved = False

    def trim3(self, qvThreshold=20, lengthThreshold=25):
        '''Trimming bases for 3'end with QV <= qvThreshold'''
        for i, qvalue in enumerate(self.qvSeq[::-1]):
            if ord(qvalue) - self.qvType > qvThreshold:
                if i > 0:  #if i==o all bases are hold.
                    #print str(i) + " bases are trimmed from 3'end"
                    self.baseSeq = self.baseSeq[:-i]
                    self.qvSeq = self.qvSeq[:-i]
                    if len(self.qvSeq) <= lengthThreshold:self.isRemoved = True
                break
        else:  #if all bases' QV <=Threshold
            #print "all bases has been trimmed"
            self.baseSeq = ''
            self.qvSeq = ''
            self.isRemoved = True

    def trim5(self, qvThreshold=20, lengthThreshold=25):
        '''Trimming bases for 3'end with QV <= qvThreshold'''
        for i, qvalue in enumerate(self.qvSeq):
            if ord(qvalue) - self.qvType > qvThreshold:
                if i > 0:  #if i==o all bases are hold.
                    #print str(i) + " bases are trimmed from 5'end"
                    self.baseSeq = self.baseSeq[i:]
                    self.qvSeq = self.qvSeq[i:]
                    if len(self.qvSeq) <= lengthThreshold:  self.isRemoved = True
                break
        else:  #if all bases' QV <=Threshold
            #print "all bases has been trimmed"
            self.baseSeq = ''
            self.qvSeq = ''
            self.isRemoved = True

    def removeSeq(self, qvThreshold=15, removeRate=80):
        if len(self.qvSeq)==0:
            self.isRemoved=True
            return

        qvSeq_numeric = map(lambda x:ord(x) - self.qvType, self.qvSeq)
#        print [ord(char) - self.qvType for char in self.qvSeq if ord(char) - self.qvType <= qvThreshold]     bases with QV <=THERSHOLD
#        lowQualityBaseNum = len([ord(char) - self.qvType for char in self.qvSeq if ord(char) - self.qvType <= qvThreshold])
        lowQualityBaseNum = len([x for x in qvSeq_numeric if x <= qvThreshold])
        lowQualityBaseRate = float(lowQualityBaseNum)/len(self.qvSeq)*100
        if lowQualityBaseRate >= removeRate:
            self.isRemoved = True

    def writeMySelf(self,outputFile):
        outputFile.writelines(self.header1+"\n")
        outputFile.writelines(self.baseSeq+"\n")
        outputFile.writelines(self.header2+"\n")
        outputFile.writelines(self.qvSeq+"\n")

    def showMyself(self):
        print self.header1
        print self.baseSeq
        print self.header2
        print self.qvSeq
