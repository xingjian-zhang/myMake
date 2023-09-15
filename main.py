import numpy as np
import argparse
import yaml
import json
import os
from model import LinearRegression, QuadraticRegression
import dataclasses


@dataclasses.dataclass
class Config:
    description: str
    data_config: dict
    model_config: dict
    filename: str

    @classmethod
    def from_yaml(cls, filename):
        with open(filename, "r") as f:
            config = yaml.safe_load(f)
        filename = os.path.basename(filename)
        filename = os.path.splitext(filename)[0]
        assert len(config["model"]) == 1, "Only one model type can be specified"
        return cls(config["desc"], config["data"], config["model"], filename)


def load_data(filename):
    data = np.loadtxt(filename, delimiter=",", skiprows=1)
    return data[:, :1], data[:, 1]


def mean_squared_error(y_true, y_pred):
    return ((y_true - y_pred)**2).mean()


def main(config: Config):
    # Load data.
    X, y = load_data(config.data_config["path"])

    # Load model.
    model_type = list(config.model_config.keys())[0]
    model_type_to_cls = {
        "linear": LinearRegression,
        "quadratic": QuadraticRegression
    }
    model = model_type_to_cls[model_type](**config.model_config[model_type])

    # Fit model.
    model.fit(X, y)
    predictions = model.predict(X)

    # Evaluate and save the metric.
    mse = mean_squared_error(y, predictions)
    print(model)
    print(f"Mean Squared Error: {mse:.4f}")
    os.makedirs("results", exist_ok=True)
    save_path = f"results/{config.filename}.json"
    metric = {"desc": config.description, "metric": {"mse": mse}}
    json.dump(metric, open(save_path, "w"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Train and evaluate a regression model")
    parser.add_argument("config", type=str, help="Path to the config file")
    config = Config.from_yaml(parser.parse_args().config)
    main(config)
