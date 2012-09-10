#!/usr/local/bin/python
# coding:utf8
import Cdf
from fastaReader import Fasta
import myplot

reader=Fasta.FASTAreader("/Users/ytanizaw/Desktop/ParaRubber/PR_320_128_contig.fa")

L=[]
for seq in reader:
    L.append(seq.length)

cdf=Cdf.MakeCdfFromList(L, "ContigLength")
myplot.Cdf(cdf, complement=False, transform=None)
#myplot.Show(xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/ParaRubber/PlatunusContig80M20M',title='CDF of contig length',xlabel='log(length)',ylabel='probability',xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/ParaRubber/PlatunusContig80M20M_loglog',title='CDF of contig length',xlabel='log(length)',ylabel='log(probability)',xscale="log",yscale="log")
