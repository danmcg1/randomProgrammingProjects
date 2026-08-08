
from pathlib import Path

base_dir = Path('/home/danmcg/NetworkDrive/Media/Music')

def find_dir_contents(base_dir):
    for path in base_dir.rglob("*.sh"):
        if path.is_file():
            print(f"File: {path}")
        elif path.is_dir():
            print(f"Dir:  {path}")

def files_by_extension(base_dir, extension):
        for path in base_dir.rglob(f"*.{extension}"):
            print(f"{path}")
    

def main():
    print(files_by_extension(base_dir, 'txt'))

if __name__ == '__main__':
    main()
            
    


