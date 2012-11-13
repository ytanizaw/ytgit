from ngs.fastqSeq import FASTQseq
import glob

def statForOneFILE(fastqFileName,qvType=33):
    bases=0
    readNum = 0
    sum_QV=0
    for fastqSeq in FASTQseq.FASTQreader(fastqFileName, qvType):
        bases += len(fastqSeq.baseSeq)
        sum_QV += sum([ord(x)-qvType for x in fastqSeq.qvSeq])
        readNum += 1
    return readNum,bases,sum_QV

def main(dirPath,qvType=33):
    total_bases=0
    total_readNum=0
    total_sum_QV=0
    fileList=glob.glob(dirPath)

    for fastqFileName in fileList:
        readNum,bases,sum_QV = statForOneFILE(fastqFileName,qvType)
        total_bases +=bases
        total_readNum +=readNum
        total_sum_QV +=sum_QV
    print "Total Read Number #:", total_readNum
    print "Total Base Number:", total_bases
    print "Average Read Length (bp/read):",float(total_bases)/total_readNum
    print "Average QV :", float(total_sum_QV)/total_bases

if __name__=="__main__":
    import sys
    if len(sys.argv)==2:
        filePath=sys.argv[1]
        main(filePath)
    elif len(sys.argv)==3:
        filePath=sys.argv[1]
        qvType=int(sys.argv[2])
        if qvType not in (33, 64):
            print "invalid QVtype: QVtype must be 33 or 64"
            exit()
        main(filePath,qvType)
    elif len(sys.argv)==1:
        filePath="/Users/ytanizaw/Desktop/extractUnmappedFASTQ/ERR008647_?.fastq"
        main(filePath)
    else:
        print "invalid parameter:Give FILEPATH QVTYPE(33or64)"

