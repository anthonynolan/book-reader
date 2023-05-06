import pickle

data_dir = "./data"


def load_data(name):
    path = f"{data_dir}/data_{name}.pkl"
    print(path)
    with open(path, "rb") as f:
        content = pickle.load(f)
    return content


def save_data(name, content):
    path = f"{data_dir}/data_{name}.pkl"
    print(path)
    with open(path, "wb") as f:
        pickle.dump(content, f)
    return "data saved"
