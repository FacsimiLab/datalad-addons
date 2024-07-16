#!/usr/bin/env python3


"""Procedure to build a reproducible research dataset which is compatible with FacsimiLab and YODA philosophy.

This procedure assumes a clean dataset that was just created by
`datalad create`.
"""
#%%
import os
import sys
import shutil
import time
import re

import datalad.api as dl
from datalad.distribution.dataset import require_dataset

print(f"sys.arg: {sys.argv[1]}")

subdataset_name = sys.argv[1]

#%%
ds = require_dataset(
    subdataset_name,
    check_installed = True,
    purpose = 'Reproducible research with FacsimiLab'
)
#%%
current_dataset_name = os.path.basename(ds.path)

print(f"Current dataset: {current_dataset_name}")


dl.clone("https://github.com/FacsimiLab/project-template.git", path="./tmp-template")
# %%

# Remove the datalad UUID from the template
file_path = os.path.join('tmp-template', '.datalad', 'config')


# Define the regex pattern
pattern = re.compile(r'\[datalad "dataset"\]\n\sid = \S*$\n', re.MULTILINE)

# Read, replace, and write in a single block
with open(file_path, 'r+') as file:
    content = file.read()
    new_content = re.sub(pattern, '\n', content)
    file.seek(0)
    file.write(new_content)
    file.truncate()

# Migrate the datalad config

new_subdataset_config_path = '.datalad/config'
template_config_path = 'tmp-template/.datalad/config'

# Read the content from the second file
with open(template_config_path, 'r') as template_config:
    content_to_append = template_config.read()

# Append the content to the first file
with open(new_subdataset_config_path, 'a') as new_subdataset_config:
    new_subdataset_config.write('\n' + content_to_append)

os.remove(template_config_path)

print("Datalad config appended successfully from template.")



#%% move files

print("Moving Facsimilab Template files into the new dataset")

shutil.rmtree("./tmp-template/.git")
template_dir = './tmp-template'
destination_dir = os.path.dirname(template_dir)

# Iterate over each item in the source directory
for item in os.listdir(template_dir):
    item_path = os.path.join(template_dir, item)
    destination_path = os.path.join(destination_dir, item)
    
    # Move the item to the destination directory
    shutil.move(item_path, destination_path)


print("Cleanup")
shutil.rmtree("./tmp-template")

print("Run procedure completed.")

# # #%%

# # dl.create(
# #     path=
# # )