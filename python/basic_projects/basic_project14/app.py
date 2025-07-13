import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f"file name {filename} created successfully")
    except FileExistsError:
        print(f"file name {filename} already exist")
    except Exception as E:
        print("an error occured")

def view_all_files():
    files = os.listdir()
    if not files:
        print("no files found")
    else:
        print("files in directory")
        for file in files:
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully")
    except FileNotFoundError:
        print("file not found ")
    except Exception as e:
        print("an error occured")   

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content = f.read()
            print(f"content of {filename} : \n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn't exist") 
    except Exception as e:
        print("an error occured")

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input("enter data to add")
            f.write(content + "\n") 
            print(f"content added to {filename} successfully")
    except FileNotFoundError:
        print(f"{filename} doesn't exist") 
    except Exception as e:
        print("an error occured")

def main():
    while True:
        print("\nfile management app")
        print("1.create a file")
        print("2.view a file")
        print("3.delete a file")
        print("4.read a file")
        print("5.edit a file")
        print("6.exit a file \n")

        choice = input("enter your choice : ")
        if choice =='1':
            filename = input("enter file name to create a file : ")
            create_file(filename)

        elif choice == '2':
            view_all_files()

        elif choice == '3':
            filename = input("enter the file name to delelte : ")
            delete_file(filename)
        
        elif choice == '4':
            filename = input("enter a file name to read : ")
            read_file(filename)

        elif choice == '5':
            filename = input("enter file name to edit : ")
            edit_file(filename)
        
        elif choice == '6':
            print("closing the program . . . . ")
            break

        else:
            print("invalid choice")

if __name__ == "__main__":
    main() 