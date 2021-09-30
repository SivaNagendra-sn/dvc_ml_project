import yaml
import os

def read_yaml(path_yaml: str) -> dict:
    with open(path_yaml) as ymlfile:
        content = yaml.safe_load(ymlfile)
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory created at {dir_path}")