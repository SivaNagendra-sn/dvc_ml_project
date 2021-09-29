import yaml
import os

def read_yaml(path_yaml: str) -> dict:
    with open(path_yaml) as ymlfile:
        content = yaml.safe_load(ymlfile)
        
    return content