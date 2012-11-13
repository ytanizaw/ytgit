#!/usr/local/bin/python
# coding:utf8
from fastaReader import Fasta


fileList=["/Users/ytanizaw/Desktop/fastaplot/Fasta1.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta2.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta3.fa"]
nameList=["test1","test2","test3"]

borderList=[100000,50000,10000,5000,1000,0]

#makeDictionary
dictDistri={}
for border in borderList:
    dictDistri[border]=[0]*len(fileList)

for i,fastafile in enumerate(fileList):

    fastaSeqs=Fasta.FASTAreader(fastafile)
    for seq in fastaSeqs:

        if seq.length >= borderList[0]:
            dictDistri[borderList[0]][i] += 1
        for j in range(len(borderList)-1):
            if borderList[j+1] <= seq.length < borderList[j]:
                dictDistri[borderList[j+1]][i] += 1


tmpstr="---"
for name in nameList:
    tmpstr += "\t"+name
print tmpstr

for border in borderList:
    tmpstr=str(border)
    for i in range(len(fileList)):
        tmpstr += "\t"+str(dictDistri[border][i])
    print tmpstr