import shutil
import os

import time
import threading

from tkinter import *
import tkinter.messagebox
path = 'C:\\Users\\Dell T3600'

def find_file(root_folder,folder_name):
    j=0
    file1 = open("names_db.txt", "r")
    text = file1.read().split('^')
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for folder in os.scandir(dirpath):
            if folder.is_dir() and folder.name == folder_name:
                copy_path=str(os.path.join(dirpath, folder))
                return copy_path


def find_and_copy_folder(folder_name):
    folder_path = find_file(path,folder_name)
    if folder_path is not None:
        i = 1
        destination = 'E:copied_files_' + folder_name
        while os.path.exists(destination):
            destination = 'E:copied_files_' + folder_name + '__' + str(i)
            i += 1
        shutil.copytree(folder_path, destination)


def allocating_important_files():
    file1 = open("names_db.txt", "r")
    folder_names = file1.read().split('^')


    threads = []
    for folder_name in folder_names:
        thread = threading.Thread(target=find_and_copy_folder, args=(folder_name,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


def main():
    start_time = time.time()
    allocating_important_files()
    tkinter.messagebox.showinfo("files was copied :p")
    end_time = time.time()
    total_time = end_time - start_time
    print("Total time taken by the program: ", total_time)

if __name__ == '__main__':
    main()