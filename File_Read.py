import os



def Read_file(fileName):
    
    if(os.path.exists(fileName)):
        fd = open(fileName,"r")
        Data = fd.read()
        print("Data from the file is:")
        print(Data)

        fd.close()

    else:
        print("file is not existing:")
        return





def main():
    print("Enter the file name to read:")
    Name = input()

    Read_file(Name)

if __name__ == "__main__":
    main()

