
import os


def find_empty_dirs(base_dir) -> list[str]:
    empty_dirs = [root for root, dirs, files in os.walk(base_dir)
        if not len(dirs) and not len(files)]
    return(empty_dirs)

def delete_dirs(directories):
    for items in directories:
        os.removedirs(items)

def find_empty_dirs_then_remove(base_dir):
    dirs = find_empty_dirs(base_dir)
    if not dirs:
        print(f"No empty directories found")
    elif dirs:
        print(dirs)
        response = input(f"Do you want to delete the directories listed?: Y/N ")
        if response == 'y' or response == 'Y':
            delete_dirs(dirs)
            print(f"{dirs} Deleted")
        else:
            print(f"Directories NOT deleted")
    

def main():
    base_dir = input(f"What directory do you want to scan?: ")
    find_empty_dirs_then_remove(base_dir)
    

if __name__ == '__main__':
    main()
            
    


