import os
from sys import *

def DirectoryWatcher(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    if exists:
        for folderName , subfolderName , FileName in os.walk(path):
            print("current foldername is"+folderName)

            for subf in subfolderName:
                print("sub folder of "+folderName+"is:"+subf)

            for filen in FileName:
                print("file inside:"+folderName+"\t is\t"+filen)

                print("With size:",os.path.getsize(os.path.join(folderName,filen)))
                print(" ")
    else:
        print("Invalid path")

def main():

    print("Application Name is:",argv[0])

    if(len(argv) < 2):
        print("Error : Insufficient Argument")
        exist()

    if((argv[1])=="-h" or (argv[1])=="-H"):
        print("")
        exist()

    if(argv[1]=="-u" or (argv[1]=="-U")):
        print("")
        exist()

    try:
        DirectoryWatcher(argv[1])

    except ValueError:
        print("Error : invalid datatype input")


if __name__ =="__main__":
    main()
