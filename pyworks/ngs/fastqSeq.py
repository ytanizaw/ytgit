#coding:utf-8

class FASTQseq:
    def __init__(self, queryFile, qvType=33):
        self.header1 = queryFile.readline().strip()
        self.baseSeq = queryFile.readline().strip()
        self.header2 = queryFile.readline().strip()
        self.qvSeq = queryFile.readline().strip()
        self.qvType = qvType
        self.isRemoved = False

    @classmethod
    def FASTQreader(cls,fastqFileName, qvType=33):
        with open(fastqFileName) as f:
            while True:
                fastq=FASTQseq(f,qvType)
                if fastq.header1=="":
                    break
                yield fastq

    def subSequence(self,start, end):
        self.baseSeq=self.baseSeq[start:end]
        self.qvSeq=self.qvSeq[start:end]

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


def test():
    from itertools import izip
    file1="/Users/ytanizaw/Desktop/preprocess_QQVcheck_test/QVtest1.fastq"
    file2="/Users/ytanizaw/Desktop/preprocess_QQVcheck_test/QVtest2.fastq"
    reader1=FASTQseq.FASTQreader(file1)
    reader2=FASTQseq.FASTQreader(file1)
    for seq1,seq2 in izip(reader1, reader2):

        seq1.showMyself()
        seq1.subSequence(5,10)
        seq1.showMyself()

def trimMP(inputFile, outputFile, length):
    with open(outputFile, "w") as f:
        reader=FASTQseq.FASTQreader(inputFile)
        for seq in reader:
            seq.subSequence(0,length)
            seq.writeMySelf(f)
