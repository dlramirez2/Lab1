#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:09:53 2018

@author: dianaramirez
"""
import os
import random


def get_dirs_and_files(path):
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path + "/" + directory)]
    file_list = [directory for directory in os.listdir(path) if not os.path.isdir(path + "/" + directory)]
    return dir_list, file_list


def classify_pic(path):
    # To be implemented by Diego: Replace with ML model
    if "dog" in path:
        return 0.5 + random.random() / 2

    return random.random() / 2


def process_dir(path):
    dir_list, file_list = get_dirs_and_files(path)
    
    cat_list = []
    dog_list = []
    
    ##no more pictures left, if not check pictures
    ##has to be done regardless of recursion and base cases
    if len(file_list) == 0:
        print("No pictures found")
    else:
        ##checks all files in file_list with classify_pic method, and appends to cat or dog list based on 
        ##returned probability
        
        for i in range(len(file_list)):
            if classify_pic(file_list[i]) >= .5:
                dog_list.append(file_list[i])
            else:
                cat_list.append(file_list[i])
    ## no more directories left in the path, base case            
    if len(dir_list) == 0:
        print("No more directories in this path")
    ##recursion case    
    else:
        for i in range(len(dir_list)):
            ##print the directories that we are in
            print(path + "/"+ dir_list[i])
            
            ##merge 2 lists
            cat2_list, dog2_list = process_dir(path + "/" + dir_list[i])
            cat_list += cat2_list
            dog_list += dog2_list
    # Your code goes here
    return cat_list, dog_list


def main():
    start_path = './' # current directory


    get_dirs_and_files(start_path)
    cat2_list,dog2_list = process_dir(start_path)
    print("Cat list:")
    print(cat2_list)
    print("Dog list:")
    print(dog2_list)
    

main()


