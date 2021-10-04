from src.utils.all_utils import create_directory, read_yaml, save_local_df
import argparse
import pandas as pd
import os
from sklearn.model_selection import train_test_split

def split_and_save(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)
    remote_data_path = config["data_source"]

    #print(df.head())
    # save this data to local
    # Create a path to directory : artifacts/raw_local_dir/data.csv

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    raw_local_dir = config["artifacts"]["raw_local_dir"]
    raw_local_file = config["artifacts"]["raw_local_file"]

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)
    df = pd.read_csv(raw_local_dir_path)

    split_ratio = params["base"]["test_size"]
    randomstate = params["base"]["random_state"]

    train, test = train_test_split(df, test_size = split_ratio, random_state=randomstate)

    split_data_dir = config["artifacts"]["split_data_dir"]

    create_directory([os.path.join(artifacts_dir, split_data_dir)])

    train_filename = config["artifacts"]["train"]
    test_filename = config["artifacts"]["test"]

    train_data_path = os.path.join(artifacts_dir, split_data_dir, train_filename)
    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_filename)

    for data, datapath in (train, train_data_path), (test, test_data_path):
        save_local_df(data, datapath)
       


if __name__=='__main__':
    args = argparse.ArgumentParser() # adding arguments from cmd line
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")


    parsed_args = args.parse_args()
    split_and_save(config_path=parsed_args.config, params_path= parsed_args.params)
