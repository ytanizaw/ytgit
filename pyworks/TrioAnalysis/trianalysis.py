#!/usr/local/bin/python
#coding:utf-8
class ItemVCF:

    @classmethod
    def getItem(cls,f):
        for line in f:
            if line!=None and (not line.startswith("#")):
                vcfitem=ItemVCF()
                vcfitem.ch=line.split("\t")[0]
                vcfitem.pos=line.split("\t")[1]
                vcfitem.ref=line.split("\t")[3]
                vcfitem.alt=line.split("\t")[4]
                yield vcfitem

#for debug
file1 = "/Users/ytanizaw/nigworks/TrioAnalysis/Enkore.unq.var.flt.vcf"
file2 = "/Users/ytanizaw/nigworks/TrioAnalysis/MeditMandarin.unq.var.flt.vcf"
file3 = "/Users/ytanizaw/nigworks/TrioAnalysis/KingMandarin.unq.var.flt.vcf"

scafoldList=[]
posSet=set()
with open(file1) as f1, open(file2) as f2,open(file3) as f3:
    vcfprev=ItemVCF.getItem(f1).next()
    for vcfitem in ItemVCF.getItem(f1):
        print vcfitem.pos,vcfprev.pos
        if vcfitem.pos==vcfprev.pos:
            print vcfitem.ch,vcfitem.pos
            print vcfprev.ch,vcfprev.pos
        vcfprev=vcfitem

print vcfitem.ch

#with open(file1) as f1, open(file2) as f2,open(file3) as f3:
#f1=open(file1)

#print f1.readline(),
