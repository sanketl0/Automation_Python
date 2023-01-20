import os

def Delete_file(fileName):
    if(os.path.exists(fileName)):

        size = os.path.getsize(fileName)

        if(size == 0):
            os.remove(fileName)
            print("File delete sucessfully")
        
        else:
            print("Are you sure to delete the file? Y/N")
            option = input()
            
            if(option == "Y" or option == "y"):
                os.remove(fileName)

            else:
                print("file delection process stopped.")

    else:
        print("There is no file:")
        

def main():
    print("Enter the file name to Delete:")
    Name = input()

    Delete_file(Name)

if __name__ == "__main__":
    main()

