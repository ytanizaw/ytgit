#outputFile=open('/Users/ytanizaw/Desktop/repealMasker/MaskedFastQ.fastq','w')
from fastqTool import FASTQseq

with open('/Users/ytanizaw/Desktop/repealMasker/test.fq') as fastqFile:


    while True:
        mySequence=FASTQseq(fastqFile)
        if mySequence.header1=='':
            break

        mySequence.showAsFasta()


