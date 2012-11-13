#!/usr/local/bin/python
# coding:utf-8
from itertools import *
import sys


class SAM:
    def __init__(self,SAMFile,isPaired=True):
        self.seq1 = SAMFile.readline().strip()
        if isPaired:
            self.seq2 = SAMFile.readline().strip()

    @classmethod
    def SAMreader(cls,fileName,isPaired=True):
        with open(fileName) as f:
            for num,line in enumerate(f):
                if line.startswith("@"): continue
                else: break
        with open(fileName) as f:
            for _ in range(num):
                f.readline()   #skip header for "num" times
            while True:
                sam=SAM(f,isPaired)
                if sam.seq1=="":break
                yield sam