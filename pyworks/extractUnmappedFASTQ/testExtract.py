import os.path
FASTQfileName1="/tst/os/hhhhan.vat"
basename= os.path.basename(FASTQfileName1)
print basename
print os.path.splitext(basename)
outputFile1=os.path.splitext(basename)[0]+".Unmapped.fastq"
print outputFile1