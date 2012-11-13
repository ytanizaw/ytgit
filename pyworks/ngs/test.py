import fastaReader

fileList=["/Users/ytanizaw/Desktop/fastaplot/Fasta1.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta2.fa",
          "/Users/ytanizaw/Desktop/fastaplot/Fasta3.fa"]

for f in fileList:
    fastaReader.stat(f, 0)