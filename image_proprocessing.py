#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 12:01:09 2018

@author: keyur-r
"""

# Image Preprocessing for train, test and validation sets

import os
import random
import glob
import shutil # Added to make sure copy is possible

# Function to move files (original intent seems to be to 'prepare' a subset)
def prepare_data(source_dir, destination_dir, n):
    for class_name in ['circles', 'squares', 'triangles']:
        source_path = os.path.join("shapes", source_dir, class_name)
        file_list = glob.glob(os.path.join(source_path, "*"))
        
        # Calculate number of files to select (to move/remove)
        files_to_select = min(n, len(file_list))

        if files_to_select > 0:
            selected_files = random.sample(file_list, files_to_select)
            
            # The original functions removed files. Assuming the goal is 
            # to make a random subset available for test/validation, 
            # the current logic of selecting and removing is maintained.
            for file_to_remove in selected_files:
                os.remove(file_to_remove)
            
            print(f"Removed {len(selected_files)} files from {source_path}")


def prepare_test_data(n):
    """Removes 'n' random images from each class in the test set."""
    prepare_data("test", None, n) # destination_dir is None for removal


def prepare_validation_data(n):
    """Removes 'n' random images from each class in the validation set."""
    prepare_data("validation", None, n) # destination_dir is None for removal

# The original code structure for prepare_test_data and prepare_validation_data:

# def prepare_test_data(n):
#     base_path = "shapes"
#     f1 = random.sample(glob.glob(os.path.join(base_path, "test/circles") + "/*"), n)
#     f2 = random.sample(glob.glob(os.path.join(base_path, "test/squares") + "/*"), n)
#     f3 = random.sample(glob.glob(os.path.join(base_path, "test/triangles") + "/*"), n)
#     for c in f1:
#         os.remove(c)
#     for s in f2:
#         os.remove(s)
#     for t in f3:
#         os.remove(t)

# def prepare_validation_data(n):
#     base_path = "shapes"
#     f1 = random.sample(glob.glob(os.path.join(base_path, "validation/circles") + "/*"), n)
#     f2 = random.sample(glob.glob(os.path.join(base_path, "validation/squares") + "/*"), n)
#     f3 = random.sample(glob.glob(os.path.join(base_path, "validation/triangles") + "/*"), n)
#     for c in f1:
#         os.remove(c)
#     for s in f2:
#         os.remove(s)
#     for t in f3:
#         os.remove(t)