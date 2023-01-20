
from sys import *
from os import *

def script_Task(No):
    if ((No % 2)==0):
        print("Its even number")
    else:
        print("Its even number")

def main():

    print("Automation scriot start with name:",argv[0])
    
    if(len(argv) != 2):
        print("Error: Insufficient arguments")
        print("Use -h for help and use -u for usages of the script")
        exit()

    if((argv[1]=="-h") or (argv[1]=="-H")):
        print("Help : This script is used to perform__________")
        exit()

    if((argv[1]=="-u") or (argv[1]=="-U")):
        print("usages : provide____number of argument as")
        print("first Argument as : _____")
        print("second Argument as : ______")
        exit()

    #else:
        # print("There is no such option in the script as :",argv[1])
        # exit()

    else:
        script_Task(int(argv[1]))

if __name__ == "__main__":
    main()