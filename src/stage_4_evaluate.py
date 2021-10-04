from src.utils.all_utils import create_directory, read_yaml, save_local_df, save_reports
import argparse
import pandas as pd
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import joblib
import numpy as np

def evaluate_metrics(actual, predicted):
    rmse = np.square(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    r2 = r2_score(actual, predicted)
    return rmse, mae, r2

def evaluate(config_path, params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts_dir = config["artifacts"]["artifacts_dir"]
    split_data_dir = config["artifacts"]["split_data_dir"]
    test_filename = config["artifacts"]["test"]

    test_data_path = os.path.join(artifacts_dir, split_data_dir, test_filename)

    test_data = pd.read_csv(test_data_path)

    test_y = test_data["quality"]
    test_X = test_data.drop(["quality"], axis =1)
    
    model_dir = config["artifacts"]["model_dir"]
    model_filename =config["artifacts"]["model_file"]

    model_path = os.path.join(artifacts_dir, model_dir, model_filename)

    elastic_model = joblib.load(model_path)

    prediction = elastic_model.predict(test_X)

    rmse, mae, r2 = evaluate_metrics(test_y, prediction)
    print(rmse, mae, r2)

    scores_dir = config["artifacts"]["reports_dir"]
    scores_filename = config["artifacts"]["scores"]

    scores_dir_path = os.path.join(artifacts_dir, scores_dir)
    create_directory([scores_dir_path])
    scores_file_path = os.path.join(scores_dir_path, scores_filename)

    scores = {
        "rmse": rmse,
        "mae": mae,
        "r2_score": r2
    }
    save_reports(scores=scores, report_path=scores_file_path)

if __name__=='__main__':
    args = argparse.ArgumentParser() # adding arguments from cmd line
    args.add_argument("--config", "-c", default="config/config.yaml")
    args.add_argument("--params", "-p", default="params.yaml")


    parsed_args = args.parse_args()
    evaluate(config_path=parsed_args.config, params_path= parsed_args.params)
