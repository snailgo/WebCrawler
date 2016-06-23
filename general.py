"""
 This model contains file ops used in this projects

    def createWorkDir
    def writeFile
    def readFile
"""

import os
import csv


__author__ = 'Pengfei Wu'


def createWorkDir(project_name):
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        writeFile(os.path.join(project_name, 'queue.csv'), {})
        writeFile(os.path.join(project_name, 'crawled.csv'), {})

def writeFile(file_name, urlRecs):
    with open(file_name, 'wb') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for k, v in urlRecs.iteritems():
            csvwriter.writerow([k, v])

def readFile(file_name):
    res = dict()
    with open(file_name, 'rb') as csvfile:
        filereader = csv.reader(csvfile, delimiter=',')
        for row in filereader:
             res[row[0]] = (row[1]. row[2])
    return res

def appendFile(file_name, i1, i2):
    with open(file_name, 'a') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerrow([i1, i2])
