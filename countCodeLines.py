#!/usr/bin/env python
import sys
import os
if len(sys.argv) == 1:
	print("usage: countCodeLines.py rootDir fileType1 fileType2 ..... fileTypeN")
	exit()
lineCount = 0
fileTypes = sys.argv[2:]
result = {}
for fileType in fileTypes:
	result[fileType] = 0;
def countCodeLines():
	list_dirs = os.walk(sys.argv[1])
	for root, dirs, files in list_dirs:
		for fileName in files:
			countFileLines(root + "/" + fileName)
			
def countFileLines(filePath):
	global result
	suffix = os.path.basename(filePath).split(".")[-1]
	codeFile = open(filePath)
	if suffix not in fileTypes:
		return
	for line in codeFile:
		result[suffix] = result[suffix] + 1
countCodeLines()
for key in result.keys():
	print key, ":", result[key], "lines"
