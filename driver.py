# Name: Dylan Corbari
# Student Number: 20341171
# I acknowledge all terms of DCU's Academic Integrity Policy

import sys

def drive():
    filename = sys.argv[1]
    with open(filename, "r") as file:
        dic = {}
        txtFile  = file.readlines()
        for lines in txtFile:
            line = lines.strip().split()
            dic[line[0].split(",")[0]] = (int(line[1].split(",")[0]), int(line[2]))
        dicCon = dic.items()
    
    return dicCon