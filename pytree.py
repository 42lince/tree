#!/usr/bin/env python3
import subprocess
import sys
import os

# YOUR CODE GOES here
:

def indent(i, j, iLastIndex):
    if j == 0:
        if i == iLastIndex:
            return "└── "
        else:
            return "├── "
    elif i == iLastIndex:
        return "    "
    else:
        return "|   "


def myTree(path):
    result = [os.path.basename(path)]
    if os.path.isdir(path):
        allContent = os.listdir(path)
        # sort all the files in alphabetical order
        sortedContent = sorted(allContent, key=lambda e: e.lstrip('_').lower())
        for i in range(len(sortedContent)):
            if sortedContent[i][0] != '.':
                subtree = myTree(path + "/" + sortedContent[i])

                for j in range(len(subtree)):
                    result.append(indent(i, j, len(sortedContent) - 1) + subtree[j])
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
