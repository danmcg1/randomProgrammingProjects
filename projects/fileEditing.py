
import pathlib 
import os

base_dir = pathlib.Path('/home/danmcg/Programs')

# def find_empty_directories(base_dir):
#      for path in pathlib.Path.glob(base_dir,"*"):
#           if path.is_dir():
#                return(f"{path} is empty")


def using_walk(base_dir):
    for root, dirs, files in os.walk(base_dir):
        print("Current directory:", root)
        print("Subdirectories:", dirs)
        print("Files:", files)
               

def find_dir_contents(base_dir):
    for path in base_dir.rglob("."):
        if path.is_file():
            print(f"File: {path}")
        elif path.is_dir():
            print(f"Dir:  {path}")


def files_by_extension(base_dir, extension):
        for path in base_dir.rglob(f"*.{extension}"):
            print(f"{path}")



def find_empty_dirs(base_dir):
    empty = [root for root, dirs, files, in os.walk(base_dir)
        if not len(dirs) and not len(files)]
    return(empty)

def delete_dirs(directories):
    for items in directories:
        os.removedirs(items)

def find_empty_dirs_then_remove(base_dir):
    dirs = find_empty_dirs(base_dir)
    print(dirs)
    response = input(f"Do you want to delete the directories listed?: Y/N ")
    if response == 'y' or response == 'Y':
        delete_dirs(dirs)
        print(f"{dirs} Deleted")
    else:
        print(f"Directories NOT deleted")


def main():
    base_dir = input(f"What directory do you want to analyse?: ")
    find_empty_dirs_then_remove(base_dir)
    

if __name__ == '__main__':
    main()
            
    


