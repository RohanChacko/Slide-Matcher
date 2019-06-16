#!/usr/bin/env python3

""" Move script for dataset """
import os
import shutil


if not os.path.exists("./full_test"):
    os.mkdir("./full_test")
    os.mkdir("./full_test/slides")
    os.mkdir("./full_test/frames")

DEST_DIR = "./full_test/"
f =  open('match_output.log', 'w+')

test_count = 1
ppt_count = 1
dir_count = -1
for folder in sorted(os.walk('./Dataset')):
    dir_count += 1
    for file in folder[2]:
        file_src = folder[0] + "/" + file
        if 'ppt' in file:
            file_dest = DEST_DIR + "slides/" + folder[0].split('/')[-1] + "_ppt" + str(ppt_count) + '.jpg'
            ppt_count += 1

        else:
            file_dest = DEST_DIR + "frames/" + folder[0].split('/')[-1] + "_"+ str(test_count) + '.jpg'
            f.write(folder[0].split('/')[-1] + "_"+ str(test_count) + '.jpg '+ folder[0].split('/')[-1] + "_ppt" + str(dir_count) + '.jpg\n')
            test_count += 1
        shutil.copyfile(file_src, file_dest)
