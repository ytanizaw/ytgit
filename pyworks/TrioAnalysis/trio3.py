#!/usr/local/bin/python
#coding:utf-8
class Scaf:
    def __init__(self):
        self.name = ''
        self.num = 0
        self.data = {}

    @classmethod
    def genScaf(cls, inputfile,filenum):

        #sub routine for add data
        def updateScaf(line):
            pos, ref, alt = int(line.split('\t')[1]), line.split('\t')[3], line.split('\t')[4]
            tempdic={filenum:alt, 0:ref}
            scaf.data[pos] = tempdic

        current = ""
        for line in inputfile:
            if line.startswith('#'): #skip header
                continue

            if current == "":    #first line
                scaf = Scaf()
                scaf.name = line.split('\t')[0]
                scaf.num = int(scaf.name.split("_")[1])
                updateScaf(line)
                current = scaf.name
                continue

            if current != line.split('\t')[0]:     #Enter New Chromosome
                yield scaf
                scaf = Scaf()
                scaf.name = line.split('\t')[0]
                scaf.num = int(scaf.name.split("_")[1])
                updateScaf(line)
                current = scaf.name
            elif current == line.split('\t')[0]:
                updateScaf(line)
            else:
                print "error"
        else:
            yield scaf

#for debug
file1 = "/Users/ytanizaw/nigworks/TrioAnalysis/Enkore.unq.var.flt.vcf"
file2 = "/Users/ytanizaw/nigworks/TrioAnalysis/MeditMandarin.unq.var.flt.vcf"
file3 = "/Users/ytanizaw/nigworks/TrioAnalysis/KingMandarin.unq.var.flt.vcf"
fileout="/Users/ytanizaw/nigworks/TrioAnalysis/out.text"
fw=open(fileout,'w')
with open(file1) as f1, open(file2) as f2, open(file3) as f3:
    while True:
        scaf1, scaf2, scaf3 = Scaf.genScaf(f1,1).next(), Scaf.genScaf(f2,2).next(), Scaf.genScaf(f3,3).next()


        if scaf1.name == scaf2.name == scaf3.name:
            print "execute" + str(scaf1.num)
            dic={}
            for key in scaf2.data:
                scaf1.data.setdefault(key,{}).update(scaf2.data[key])
#            print len(dic)
            for key in scaf3.data:
                scaf1.data.setdefault(key,{}).update(scaf3.data[key])
#            print len(dic)

            if scaf1.num == 8:
                for key in sorted(scaf1.data.keys()):
                    basedic=scaf1.data[key]
                    refBase=basedic[0]
                    base1=basedic.setdefault(1,"-")
                    base2=basedic.setdefault(2,"-")
                    base3=basedic.setdefault(3,"-")
                    fw.write(scaf1.name+"\t" + str(key) + "\t"+ refBase  + "\t" + base1 + "\t" + base2 + "\t"+ base3 + "\t"+"\n" )

        else:
            break

    else:
        print scaf1.data




a = 0
if a == 1:
    for i, scaf in enumerate(Scaf.genScaf(f3)):
        if i == 230:

            print i, scaf.name, len(scaf.data)
            print scaf.data
            for key in sorted(scaf.data.keys()):
                print scaf.data[key]



