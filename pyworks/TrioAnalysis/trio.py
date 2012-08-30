#! /usr/local/bin/python
# coding:utf-8

#for debug
file1 = "/Users/ytanizaw/nigworks/TrioAnalysis/Enkore.unq.var.flt.vcf"
file2 = "/Users/ytanizaw/nigworks/TrioAnalysis/MeditMandarin.unq.var.flt.vcf"
file3 = "/Users/ytanizaw/nigworks/TrioAnalysis/KingMandarin.unq.var.flt.vcf"

#file1="/home/hnagasak/dir_exp/dir_citrus/dir_A3/dir_Enkore/Enkore.unq.var.flt.vcf"
#file2="/home/hnagasak/dir_exp/dir_citrus/dir_MeditMandarin/MeditMandarin.unq.var.flt.vcf"
#file3="/home/hnagasak/dir_exp/dir_citrus/dir_A2/dir_KingMandarin/KingMandarin.unq.var.flt.vcf"

with open(file1) as f1, open(file2) as f2, open(file3) as f3:

    print f1.readline(),
    print f2.readline(),
    print f3.readline(),
