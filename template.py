import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:' \
'')

list_of_files = [
    "src/__init__.py",#method fun used to execute automatically,local package
    "src/helper.py",#we can write all functionalities in this file
    "src/prompt.py",#to write all the prompt related functions
    ".env",
    "setup.py",#to install the local package
    "app.py",
    "research/traits.ipynb"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for file {filename}")


    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file {filename}")
    else:
        logging.info(f"File {filename} already exists")
        

