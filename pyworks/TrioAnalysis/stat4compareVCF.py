#!/usr/local/bin/python
#coding:utf-8

targetList=[
           {1:True,2:True,3:True,4:None,5:None},
           {1:True,2:True,3:False,4:None,5:None},
           {1:True,2:False,3:True,4:None,5:None},
           {1:False,2:True,3:True,4:None,5:None},
           {1:True,2:False,3:False,4:None,5:None},
           {1:False,2:True,3:False,4:None,5:None},
           {1:False,2:False,3:True,4:None,5:None},
           {1:False,2:False,3:False,4:None,5:None},
           {1:None,2:None,3:None,4:None,5:None}

            ]


fileList = [
          "/Users/ytanizaw/nigworks/TrioAnalysis/Enkore.unq.var.flt.vcf",
          "/Users/ytanizaw/nigworks/TrioAnalysis/MeditMandarin.unq.var.flt.vcf",
          "/Users/ytanizaw/nigworks/TrioAnalysis/KingMandarin.unq.var.flt.vcf"
          ]

#specify the output file of compareVCF.py
filein = "/Users/ytanizaw/nigworks/TrioAnalysis/out.text"
fileout="/Users/ytanizaw/nigworks/TrioAnalysis/stat.text"
REFnum=3
REFrange=range(3,3+REFnum)


class Scaf:
    def __init__(self, name):
        self.name = name
        self.data = {}

def genScaf(inputfile):
    def updateScaf(line):
        col=line.split('\t')
        pos=col[1]
        tempdic={}
        for i in range(REFnum):
            if col[i+3] != ".":
                tempdic.update({i+1:col[i+3]})
        scaf.data.update({pos:tempdic})

    current = ""
    for line in inputfile:
        if line.startswith('#'): continue   #skip header

        scafName = line.split('\t')[0]
        if current == "":    #For first line
            scaf = Scaf(scafName)
            updateScaf(line)
            current = scaf.name

        elif current != scafName:     #Enter New Chromosome
            yield scaf
            scaf = Scaf(scafName)
            updateScaf(line)
            current = scaf.name
        elif current == scafName:
            updateScaf(line)
    else:   # For last
        yield scaf



#============================== Main Part starts from here. ==============================
fw = open(fileout, 'w')
f = open(filein)


def toBeCounted(data):
    #print data,
    #print all([k in data for k in TrueList]) and all([k not in data for k in FalseList])
    return all([k in data for k in TrueList]) and all([k not in data for k in FalseList])


for scaf in genScaf(f):


#for data in mydic.values():
#    print toBeCounted(data)
    tmpString=scaf.name

    for target in targetList:
        FalseList= set((k for k,v in target.items() if v==False))
        TrueList= set(k for k,v in target.items() if v==True)
        #print len(scaf.data)
        tmpString += "\t"+str(len([pos for pos,data in scaf.data.items() if toBeCounted(data)]))
    print tmpString





f.close()
fw.close()
