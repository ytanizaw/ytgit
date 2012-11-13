#!/usr/local/bin/python
# coding:utf8
import ngs.Cdf as Cdf
import Pmf
from ngs.fastaReader import Fasta
import myplot


'''配列の長さを積算していった分布グラフ（0.5のところがN50に該当）

'''
fileList=["/Users/ytanizaw/Desktop/fastaplot/Fasta1.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta2.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta3.fa"]
nameList=["test1","test2","test3"]


for fasta,name in zip(fileList,nameList):

    reader=Fasta.FASTAreader(fasta)

    L=[]
    for seq in reader:
        L.append(seq.length)
    hist=Pmf.MakeHistFromList(L, name)
    print hist.Values()
    print hist.Freqs()
    for val in hist.Values():
        hist.Mult(val, val)
    print hist.Values()
    print hist.Freqs()
    cdf=Cdf.MakeCdfFromHist(hist, name)
    myplot.Cdf(cdf, complement=False, transform=None)




#myplot.Show(xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/fastaplot/figure2',title='CDF of contig length',xlabel='log(length)',ylabel='probability',xscale="log",yscale="linear")
myplot.Save(root='/Users/ytanizaw/Desktop/fastaplot/figure2_loglog',title='CDF of contig length',xlabel='log(length)',ylabel='log(probability)',xscale="log",yscale="log")
