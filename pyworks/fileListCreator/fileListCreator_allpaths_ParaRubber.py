#coding:utf-8
import os
libs=open("in_libs_PR.csv","w")
groups=open("in_groups_PR.csv","w")

libs.write("library_name,  project_name,  organism_name,  type,  paired,  frag_size,  frag_stddev,  insert_size,  insert_stddev,  read_orientation,  genomic_start,  genomic_end\n")
groups.write("group_name,  library_name,  file_name\n")
for dirpath,dirnames,filenames in os.walk("/home/ytanizaw/repmask/ParaRubber_maskedfastq"):
    if dirpath.endswith('PairEnd'):
        print "illumina0,  Bri,  ParaRubber,  fragment,  1,  200,  20,  ,  ,  inward,  ,  "
        libs.write("illumina0,  Bri,  ParaRubber,  fragment,  1,  200,  20,  ,  ,  inward,  ,  " +"\n")
        for i,filename in enumerate(sorted([filename for filename in filenames if filename.startswith("PB260_WGS_200bp_insert_NoIndex_L004_R1")])):
#            print str(i+1) +",  illumina0,  "+dirpath +"/" +filename.replace("L004_R1","L004_R?")
#            print "wc -l "+dirpath +"/" +filename.replace("L004_R1","L004_R?")
            groups.write(str(i+1) +",  illumina0,  "+dirpath +"/" +filename.replace("L004_R1","L004_R?")+"\n")

    if dirpath.endswith('MatePair_3k'):
        print "illumina4,  Bri,  ParaRubber,  jumping,  1,   ,   ,  3000,  500,  outward,  ,  "
        libs.write("illumina4,  Bri,  ParaRubber,  jumping,  1,   ,   ,  3000,  500,  outward,  ,  " +"\n")
        for i,filename in enumerate(sorted([filename for filename in filenames if filename.startswith("PB260_MatePair_3kB_NoIndex_L001_R1")])):
#            print str(400+i+1) +",  illumina4,  "+dirpath +"/" +filename.replace("L001_R1","L001_R?")
#            print "wc -l "+dirpath +"/" +filename.replace("L001_R1","L001_R?")
            groups.write(str(400+i+1) +",  illumina4,  "+dirpath +"/" +filename.replace("L001_R1","L001_R?")+"\n")

    if dirpath.endswith('MatePair_5k'):
        print "illumina5,  Bri,  ParaRubber,  jumping,  1,   ,   ,  5000,  500,  outward,  ,  "
        libs.write("illumina5,  Bri,  ParaRubber,  jumping,  1,   ,   ,  5000,  500,  outward,  ,  " +"\n")
        for i,filename in enumerate(sorted([filename for filename in filenames if filename.startswith("PB260_MatePair_5kB_NoIndex_L002_R1")])):
#            print "wc -l "+dirpath +"/" +filename.replace("L002_R1","L002_R?")
#            print str(500+i+1) +",  illumina5,  "+dirpath +"/" +filename.replace("L002_R1","L002_R?")
            groups.write(str(500+i+1) +",  illumina5,  "+dirpath +"/" +filename.replace("L002_R1","L002_R?")+"\n")


    if dirpath.endswith('MatePair_10k'):
        print "illumina6,  Bri,  ParaRubber,  jumping,  1,   ,   ,  10000,  1000,  outward,  ,  "
        libs.write("illumina6,  Bri,  ParaRubber,  jumping,  1,   ,   ,  10000,  1000,  outward,  ,  " +"\n")
        for i,filename in enumerate(sorted([filename for filename in filenames if filename.startswith("PB260_MatePair_10kB_NoIndex_L003_R1")])):
#            print "wc -l "+dirpath +"/" +filename.replace("L003_R1","L003_R?")
#            print str(600+i+1) +",  illumina6,  "+dirpath +"/" +filename.replace("L003_R1","L003_R?")
            groups.write(str(600+i+1) +",  illumina6,  "+dirpath +"/" +filename.replace("L003_R1","L003_R?")+"\n")

libs.close()
groups.close()

