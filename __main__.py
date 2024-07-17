import read_file
import argparse
import os


commands = ["-p"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', nargs='?', help='get files from path')
    #parser.add_argument('-d', '--detect', action='store_true', help='only detect which files are using Android Annotations')
    args = parser.parse_args()
    project_path =  args.path if args.path != None else os.path.abspath(os.getcwd())
    read_file.read_dir(project_path)



if __name__ == "__main__":
    main()

