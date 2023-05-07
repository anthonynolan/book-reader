import pickle
import logging
from util import call_logger

data_dir = "./data"


@call_logger
def load_data(name):
    path = f"{data_dir}/data_{name}.pkl"
    print(path)
    with open(path, "rb") as f:
        content = pickle.load(f)
    print(f"content {content}")
    return content


@call_logger
def save_data(name, content):
    path = f"{data_dir}/data_{name}.pkl"
    print(path)
    with open(path, "wb") as f:
        pickle.dump(content, f)
    return "data saved"
