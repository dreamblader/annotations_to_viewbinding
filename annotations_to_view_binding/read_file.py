import os
import logging

java_files = []


def read_dir(dir_path):
    project_path = dir_path if dir_path != None else os.path.abspath(os.getcwd())
    
    for dirpath, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith('.java'):
                java_files.append(os.path.join(dirpath, file))
                logging.debug("Detected {} file at {}".format(file, dirpath))