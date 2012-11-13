#!/usr/local/bin/python
# coding:utf8
from fastaReader import Fasta
import os

fileList=["/Users/ytanizaw/Desktop/fastaplot/Fasta1.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta2.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta3.fa"]
outFileNameList=["test1","test2","test3"]

borderList=[100000,50000,10000,5000,1000,0]
dirName="/Users/ytanizaw/Desktop/splittedFASTA/"  # must be ended with /


def writeFasta(FASTA, outputFile):
    outputFile.write(FASTA.header+"\n")
    BasesPerRow=60
    for i in range((FASTA.length)/BasesPerRow + 1):
        outputFile.write(FASTA.seq[i*BasesPerRow:(i+1)*BasesPerRow]+"\n")



#initializeDictionary and directory
if not os.path.exists(dirName):
    os.mkdir(dirName)

dictDistri={}
for border in borderList:
    dictDistri[border]=[0]*len(fileList)

#
for i,fastafile in enumerate(fileList):

    #open output files
    tmpFilePrefix=outFileNameList[i] + "_"
    outputFiles=[open(dirName + tmpFilePrefix + str(border) + ".fa","w") for border in borderList]




    fastaSeqs=Fasta.FASTAreader(fastafile)
    for seq in fastaSeqs:

        if seq.length >= borderList[0]:
            dictDistri[borderList[0]][i] += 1
            writeFasta(seq,outputFiles[0])

        for j in range(len(borderList)-1):
            if borderList[j+1] <= seq.length < borderList[j]:
                dictDistri[borderList[j+1]][i] += 1
                writeFasta(seq,outputFiles[j+1])

    for outputFile in outputFiles:
        outputFile.close()



#print out Summary
tmpstr="---"
for name in outFileNameList:
    tmpstr += "\t"+name
print tmpstr

for border in borderList:
    tmpstr=str(border)
    for i in range(len(fileList)):
        tmpstr += "\t"+str(dictDistri[border][i])
    print tmpstr