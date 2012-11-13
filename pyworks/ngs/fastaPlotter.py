#!/usr/local/bin/python
# coding:utf8
import Cdf
from fastaReader import Fasta
import myplot

fileList=["/Users/ytanizaw/Desktop/fastaplot/Fasta1.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta2.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta3.fa"]
nameList=["test1","test2","test3"]


for fasta,name in zip(fileList,nameList):

    reader=Fasta.FASTAreader(fasta)

    L=[]
    for seq in reader:
        L.append(seq.length)

    cdf=Cdf.MakeCdfFromList(L, name)
    myplot.Cdf(cdf, complement=False, transform=None)




#myplot.Show(xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/fastaplot/figure',title='CDF of contig length',xlabel='log(length)',ylabel='probability',xscale="linear",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/fastaplot/figure_loglinear',title='CDF of contig length',xlabel='log(length)',ylabel='probability',xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/fastaplot/figure_loglog',title='CDF of contig length',xlabel='log(length)',ylabel='log(probability)',xscale="log",yscale="log")
