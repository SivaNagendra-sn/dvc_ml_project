import yaml
import os
import json

def read_yaml(path_yaml: str) -> dict:
    with open(path_yaml) as ymlfile:
        content = yaml.safe_load(ymlfile)
    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory created at {dir_path}")

def save_local_df(data, data_path, index_status = False):
    data.to_csv(data_path, index = index_status)
    print(f"data is saved at {data_path}")

def save_reports(scores: dict, report_path: str, indentation = 4):
    with open(report_path, "w+") as f:
        json.dump(scores, f, indent=indentation)
    print(f"Reports are saved at {report_path}")