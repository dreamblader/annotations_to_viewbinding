import read_file
import argparse
import logging

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', nargs='?', help='get files from path')
    parser.add_argument('-v', '--verbose', action='store_true', help='log detailed script interactions')
    args = parser.parse_args()
    log_level= logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(message)s")
    read_file.read_dir(args.path)



if __name__ == "__main__":
    main()

