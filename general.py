"""
 This model contains file ops used in this projects

    def createWorkDir
    def writeFile
    def readFile
"""

import os


__author__ = 'Pengfei Wu'


def createWorkDir(project_name):
    if not os.path.exist(project_name):
        os.mkdir(project_name)

def writeFile(file_name, data):
    with open(file_name, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimite=',')
        for d in data:
            csvwriter.writerow([d.key, d.value[0], d.value[1]])

def readFile(file_name):
    res = dict()
    with open(file_name, 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimite=',')
        for row in filereader:
             res[row[0]] = (row[1]. row[2])
    return res
