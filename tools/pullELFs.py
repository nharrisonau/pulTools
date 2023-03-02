import os
import sys

directory = sys.argv[1]
outputFolder = sys.argv[2]

# ELF Header Key
key = b'\x7fELF'

def checkElf(signiture):
    if signiture == key:
        return True
    else:
        return False

#Search directory for files
def searchDir(wd):
    for item in os.scandir(wd):
        if item.is_file():
            if os.path.islink(item):
                try:
                    file = open(item, 'rb').read()
                    isELF = checkElf(file[0:4])

                    #If file is ELF file then copy it
                    if isELF:
                        path = os.getcwd() + '/' + str(outputFolder)
                        os.system("cp " + item.path + " " + path)
                except OSError:
                    pass
        if item.is_dir():
            try:
                searchDir(item)
            except OSError:
                pass
            except RecursionError:
                pass
            except PermissionError:
                pass

# Check if output directory exist and if it doesn't, create a new directory with that name
def setupOutputFolder(directory, outputFolder):
    path = os.getcwd() + '/' + str(outputFolder)
    isExist = os.path.exists(path)
    if isExist == False:
        os.mkdir(path)

def main():

    setupOutputFolder(directory, outputFolder)

    searchDir(directory)


if __name__ == "__main__":
    main()


