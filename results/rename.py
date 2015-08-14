#!/usr/bin/env python

import os
import shutil
import sys

index = sys.argv[1]
print("Appending {0} to every file".format(index))

for filename in os.listdir("."):
    dataset, filetype = filename.split(".")
    new_name = "{0}{1}.{2}".format(dataset, index, filetype)
    print("moving {0} to {1}".format(filename, new_name))
    shutil.move(filename, new_name)
