# import required module
import os
import sys

directory = sys.argv[1]
newDirectory = str(directory) + 'Data'
capaPath = "./Capa/capa -j"
filenum = 0
count = 1

def execute():
    for filename in os.scandir(directory):
        if filename.is_file():
            os.system(capaPath + " " + filename.path + " > " "./" + newDirectory + "/" + str(filename.name) + "_capa.json")
            count = count + 1
        else:
            print("pass")
        exit

def main():
    execute()


if __name__ == "__main__":
    main()