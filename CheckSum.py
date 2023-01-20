import os
from sys import *
import hashlib

def hashfile(path,blocksize = 1024):
    afile = open(path,'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def DisplayChecksum(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for dirName ,subdirs ,filelist in os.walk(path):
            print("current folder is :"+dirName)
            for filen in filelist:
                path = os.path.join(dirName,filen)
                file_hash = hashfile(path)
                print(path)
                print(file_hash)
                print(" ")
    else:
        print("Invalid path")

def main():
    print("Application name is :",argv[0])

    if(len(argv)< 2 ):
        print("Error : invalid number of argument")
        exit()

    if(argv[1]=="-h" or argv [1]=="-H"):
        print("This script is used to traverse specific directoory")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usages : ApplicationName absolutepath of directory")
        exit()

    try:
        DisplayChecksum(argv[1])

    except ValueError as E:
        print("Error Invalid datatype of input",E)

if __name__ =="__main__":
    main()