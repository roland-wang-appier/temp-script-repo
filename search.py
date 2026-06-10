import os
import glob
files = glob.glob('/**/ph.zuscoffee.com*', recursive=True)
print("Found files:", files)
