import os
import sys
import hashlib

dir1 = sys.argv[1]
dir2 = sys.argv[2]

dir1Hash = list()
 
def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def compare():
    count = 0
    os.system("mkdir leftovers")
    for i in os.scandir(dir2):
        fileHash = hashfile(i)
        for item in dir1Hash:
            if fileHash == item:
                print("hit: " + str(i.name))
                count = count + 1
                dir1Hash.remove(item)
                break
    return count

def createComparison(dir):

    for file in os.scandir(dir):
        hash = hashfile(file)
        dir1Hash.append(hash)
    return dir1Hash

def main():
    count = 0
    comp = createComparison(dir1)
    count = compare()
    count1 = 0
    count2 = 0
    for file2 in os.scandir(dir1):
        count1 = count1 + 1
    for file2 in os.scandir(dir2):
        count2 = count2 + 1
    print("Files in Directory 1: " + str(count1))
    print("Files in Direcotry 2: " + str(count2))
    print("Matched Files: " + str(count))

if __name__ == "__main__":
    main()

