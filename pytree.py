#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here


def myTree(path):
    result = [os.path.basename(path)]
    if os.path.isdir(path) and os.listdir(path):
        allContent = os.listdir(path)
        # sort all the files in alphabetical order
        sortedContent = sorted(allContent, key=lambda e: e.lstrip('_').lower())
        for i in range(len(sortedContent)):
            if sortedContent[i][0] != '.':
                subtree = myTree(path + "/" + sortedContent[i])

                indent = ""
                for j in range(len(subtree)):
                    if j == 0:
                        if i == len(allContent) - 1:
                            indent = "`-- "
                        else:
                            indent = "|-- "
                    elif i == len(allContent) - 1:
                        indent = "    "
                    else:
                        indent = "|   "
                    result.append(indent + subtree[j])
        global totalDirCount
        totalDirCount += 1
    else:
        global totalFileCount
        totalFileCount += 1
    return result


def printDirectory():
    if totalDirCount == 1:
        return '1 directory'
    else:
        return '{} directories'.format(totalDirCount)


def printFiles():
    if totalFileCount == 1:
        return '1 file'
    else:
        return '{} files'.format(totalFileCount)

def prettyDisplay(tree, path):
    for line in tree:
        print(line)
    print('')

    if os.path.isdir(path):
        global totalDirCount
        totalDirCount -= 1
    else:
        global totalFileCount
        totalFileCount -= 1

    print(printDirectory() + ', ' + printFiles())


totalDirCount = 0
totalFileCount = 0
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = "."
prettyDisplay(myTree(path), path)

