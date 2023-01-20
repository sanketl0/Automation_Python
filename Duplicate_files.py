from sys import *
import os
import hashlib


def hashfile(path,blocksize=1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    afile.close()

    return hasher.hexdigest()


def findDuplicateFileDiplay(path):
    flag = os.path.isabs(path)

    if flag ==False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    dups = {}

    if exists:
        for dirName , SubDir, fileNames in os.walk(path):
            print("Current directory is : "+dirName)
            for files in fileNames:
                path = os.path.join(dirName,files)
                file_hash = hashfile(path)

                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups

    else:
        print("Invalid path")
        exit()

def printDuplicates(dict1):
    result = list(filter(lambda x : len(x)>1, dict1.values()))

    if len(result)>0:
        print("Duplicates found : ")
        print("The following files are identetical")

        icnt = 0
        for subres in result:
            icnt +=1
            if icnt >=2:
                print('')
                print('\t\t%s' % subres , "\n")

    else:
        print("No Duplicates are found ")

def main():
    print("Marvellous Infosystems ")
    print("Application Name : "+argv[0])

    if(len(argv)!=2):
        print("ERROR : INSUFFICIENT ARGUMENTS")
        exit()

    if(argv[1]=='-u') or (argv[1] == '-U'):
        print("USAGE : ApplicationName AbsolutePath_of_Directory Extension")
        exit()

    if(argv[1] == "-h" ) or (argv[1] == '-H'):
        print("HELP :The script is used to traverse specific directory and display all files which have given Extension ")
        exit()

    try:
        arr = {}
        arr = findDuplicateFileDiplay(argv[1])
        printDuplicates(arr)

    except ValueError as v:
        print("Error : Invalid Datatype of input",v)

    except Exception as E :
        print("Error : invalid input" ,E)

if __name__ == '__main__':
    main()