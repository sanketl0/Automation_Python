import os



def write_file(fileName):
    if(os.path.exists(fileName)):
        print("enter the data that you want to write in file")
        Data = input()

        fd = open(fileName,"a")
        fd.write(Data)
    else:
        print("file is not existing:")
        return





def main():
    print("Enter the file name to write:")
    Name = input()

    write_file(Name)

if __name__ == "__main__":
    main()

