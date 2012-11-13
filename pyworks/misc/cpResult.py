#!/usr/local/bin/python
#coding:utf-8
import os
import glob
import os.path

dirList=[
    #    "/home/w3pipeline/refdata/result/tshimizu/4546/4360/17220/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4547/4361/17221/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4548/4362/17222/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4549/4363/17223/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4550/4364/17224/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4551/4365/17225/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4552/4366/17226/uniqsam/",
    #    "/home/w3pipeline/refdata/result/tshimizu/4553/4367/17227/uniqsam/"
        "/home/w3pipeline/refdata/result/tshimizu/4560/4374/17234/uniqsam/",
        "/home/w3pipeline/refdata/result/tshimizu/4561/4375/17235/uniqsam/",
        "/home/w3pipeline/refdata/result/tshimizu/4562/4376/17236/uniqsam/"
        ]

nameList=[
#        "A1_Unshu",
#        "A1_s34",
#        "A1_s56",
#        "A1_s78",
#        "A2_s12",
#        "A2_s34",
#        "A2_s56",
#        "A2_s78"
        "A3_s12",
        "A3_s34",
        "A3_s56"
        ]


for prefix, dirName in zip(nameList,dirList):
    #print "Processing JOB:" + prefix
    for fileName in glob.glob(dirName + "*"):
        if fileName.endswith("uniqout.sam"):
            tmpstr= "cp " + fileName + " ./" + prefix +"_uniq.sam"
            print tmpstr
        elif fileName.endswith("out2.bam"):
            tmpstr= "cp " + fileName + " ./" + prefix +"_uniq_sorted.bam"
            print tmpstr
        elif fileName.endswith("out2.bam.bai"):
            tmpstr= "cp " + fileName + " ./" + prefix +"_uniq_sorted.bam.bai"
            print tmpstr

    #print "NEXT JOB"

