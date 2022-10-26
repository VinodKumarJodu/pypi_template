from email.utils import format_datetime
import os
from pathlib import Path
import logging

logging_format = "[%(asctime)s: %(levelname)s]: %(message)s"

logging.basicConfig(level=logging.INFO, format=logging_format)


while True:
    project_name = input("Enter the Project Name: ")
    logging.info(f"Creating Project: {project_name}")
    if project_name != "":
        break

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"tests/__init__.py",
    f"tests/unit/__init__.py",
    f"tests/integration/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "pyproject.toml",
    "setup.cfg",
    "tox.ini",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")
    if (not os.path.exists(filepath)) or (os.path.getsize == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating file: {file_name} at path: {filepath}")
    else:
        logging.info(f"file is already exists at: {filepath}")
