#!/usr/local/bin/python
#coding:utf-8
import re
pat=re.compile(r"DP=\d*")
pat2=re.compile(r"FQ=\-?\d+\.?\d*")

fileList = [
          "/Users/ytanizaw/nigworks/TrioAnalysis/Enkore.unq.var.flt.vcf",
          "/Users/ytanizaw/nigworks/TrioAnalysis/MeditMandarin.unq.var.flt.vcf",
          "/Users/ytanizaw/nigworks/TrioAnalysis/KingMandarin.unq.var.flt.vcf"
          ]
fileout = "/Users/ytanizaw/nigworks/TrioAnalysis/out.text"


class Scaf:
    def __init__(self, name, filenum):
        self.name = name
        self.num = int(name.split("_")[1])
        self.filenum = filenum
        self.data = {}

def genScaf(inputfile, filenum):
    def updateScaf(line):
        pos, ref, alt, qual = int(line.split('\t')[1]), line.split('\t')[3], line.split('\t')[4], line.split('\t')[5]
        depth=pat.search(line).group().split("=")[1]
        FQ=float(pat2.search(line).group().split("=")[1])
        if abs(FQ)>=0:
            tempdic = {filenum + 1:alt, 0:ref, "DP_"+str(filenum + 1):depth, "Q_"+str(filenum + 1):qual,"FQ_"+str(filenum + 1):FQ}
            scaf.data[pos] = tempdic

    current = ""
    for line in inputfile:
        if line.startswith('#'): continue   #skip header

        scafName = line.split('\t')[0]
        if current == "":    #For first line
            scaf = Scaf(scafName, filenum)
            updateScaf(line)
            current = scaf.name

        elif current != scafName:     #Enter New Chromosome
            yield scaf
            scaf = Scaf(scafName, filenum)
            updateScaf(line)
            current = scaf.name
        elif current == scafName:
            updateScaf(line)
    else:   # For last
        yield scaf

def upd2(scaf):
    if scaf == None:return
    if scaf.num == minimum:
        try:
            return genL[scaf.filenum].next()
        except StopIteration:
            return
    return scaf

#============================== Main Part starts from here. ==============================
fw = open(fileout, 'w')
fL = [open(f) for f in fileList]
genL = [genScaf(f, i) for i, f in enumerate(fL)]
scafL = [g.next() for g in genL]

for i,f in enumerate(fileList):
    fw.write("#FILE"+str(i+1)+":\t" + f +"\n")

tmpTitle="#SCAFFOLD\tPOS\tREF"
fw.write("#SCAFFOLD\tPOS\tREF\t" + "\t".join(["\t".join([name + str(i+1) for i in range(len(fileList))]) for name in ["ALT","DEPTH","QUAL","FQ"]]) + "\n")
while True:
    minimum = min([scaf.num for scaf in scafL if scaf != None])
    targetScafL = [scaf for scaf in scafL if scaf != None and scaf.num == minimum]
    # debug
    print "Target:" + str([scaf.num for scaf in targetScafL])+"\tCurrent:"+str([scaf.num if scaf != None else None for scaf in scafL])

    # Merge Dictionary
    tempDic = {}
    for scaf in targetScafL:  #Loop by file
        tmpName = scaf.name
        for pos, item in scaf.data.items():   #Loop by position
            tempDic.setdefault(pos, {}).update(item)

    # Output to File
    for pos in sorted(tempDic.keys()):  #Loop for DataDictionary by position
        tmpString = tmpName + "\t" + str(pos)
        for i in range(len(scafL) + 1):    #Loop for Variation by filenum
            tmpString += "\t" + tempDic[pos].setdefault(i, ".")
        for i in range(1,len(scafL) + 1):    #Loop for depth by filenum
            tmpString += "\t" + tempDic[pos].setdefault("DP_"+str(i), ".")
        for i in range(1,len(scafL) + 1):    #Loop for quality by filenum
            tmpString += "\t" + tempDic[pos].setdefault("Q_"+str(i), ".")
        for i in range(1,len(scafL) + 1):    #Loop for quality by filenum
            tmpString += "\t" + str(tempDic[pos].setdefault("FQ_"+str(i), "."))
        fw.write(tmpString + "\n")

    # Update List   If List is null, exit while Loop.
    scafL = [upd2(scaf) for scaf in scafL]
    if len([scaf for scaf in scafL if scaf != None]) == 0:
        break

[f.close() for f in fL]
fw.close()
