import json
import os
import sys
from prettytable import PrettyTable

# Directory for Features
featureLog = {}

#Directory for file Arch
archLog = {}

#Directory for file Type
typeLog = {}

featureInstances = {}

# Check and Update File Type Log
def getType(data):      
    type = data['meta']['analysis']['format']
    if type in typeLog:
            typeLog[type] = typeLog[type] + 1
    else:
        typeLog.update({type:1})

# Check and Update File Arch Type
def getArch(data):
    arch = data['meta']['analysis']['arch']
    if arch in archLog:
            archLog[arch] = archLog[arch] + 1
    else:
        archLog.update({arch:1})

# Check and Update Feature Log
def getRules(data):
    for i in data['rules']:
        if i in featureLog:
            featureLog[i] = featureLog[i] + 1
        else:
            featureLog.update({i:1})

# Find Files that Contain Certain Feature
def findFeature(data, feature):
    for i in data['rules']:
        if i == feature:
            return True
        else:
            return False
            

def printTables():
    # Feature Table
    featureTable = PrettyTable()
    featureTable.field_names = ["Feature", "Instances"]
    for k in featureLog:
        featureTable.add_row([k, featureLog[k]])

    # Arch Table
    archTable = PrettyTable()
    archTable.field_names = ["Arch", "Instances"]
    for a in archLog:
        archTable.add_row([a, archLog[a]])

    # Type Table
    typeTable = PrettyTable()
    typeTable.field_names = ["File Type", "Instances"]
    for t in typeLog:
        typeTable.add_row([t, typeLog[t]])

    # Print out Tables
    print(archTable)
    print(typeTable)
    print(featureTable)

def scan(directory):
    for filename in os.scandir(directory):
        try:
            # Open File
            f = open(filename, "r")
            data = json.loads(f.read())

            #Get Data
            getRules(data)
            getArch(data)
            getType(data)

            # Close File
            f.close()
        except:
            pass
    printTables()

def scanForFeature(directory, inspect):
    for filename in os.scandir(directory):
        try:
            # Open File
            f = open(filename, "r")
            data = json.loads(f.read())
            result = findFeature(data, inspect)
            if result == True:
                print(filename.name)
        except:
            pass 

def main():
    # Directory of JSON Files
    directory = sys.argv[1]

    scan(directory)
    inspect = input('Enter a feature to see which files contain that feature:')
    print(inspect)
    scanForFeature(directory, inspect)

if __name__ == "__main__":
    main()