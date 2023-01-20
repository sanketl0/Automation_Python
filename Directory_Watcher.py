import os
from sys import *


def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for folderName , subfolderName ,fileName in os.walk(path):
            print("current folder is : "+folderName)

        for subf in subfolderName:
            print("sub folder of "+folderName+"is:"+subf)

        for filen in fileName:
            print("file inside "+folderName+"is"+filen)
            print(" ")

    else:
        print("Invalid path")

def main():

    print("Application Name is :",argv[0])
    
    if(len(argv) < 2):
        print("Error : Insufficient Arguments")
        exit()

    if(argv[1]=="-h" or (argv[1]=="-H")):
        print("")
        exit()

    if(argv[1]=="-u" or argv[1]=="-U"):
        print("")
        exit()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : invald Datatype input")

if __name__ =="__main__":
    main()