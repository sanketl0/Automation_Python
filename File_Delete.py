import os

def Delete_file(fileName):
    if(os.path.exists(fileName)):
        os.remove(fileName)
        print("File delete sucessfully")
        
    else:
        print("There is no file:")
        

def main():
    print("Enter the file name to Delete:")
    Name = input()

    Delete_file(Name)

if __name__ == "__main__":
    main()

