import numpy as np
import yaml
import argparse


def load_config(filename):
    with open(filename, "r") as file:
        config = yaml.safe_load(file)
    return config


def generate_linear(num_points, slope, intercept, noise_std):
    X = np.linspace(0, 10, num_points)
    y = slope * X + intercept + np.random.normal(0, noise_std, num_points)
    return X, y


def generate_quadratic(num_points, a, b, c, noise_std):
    X = np.linspace(0, 10, num_points)
    y = a * X**2 + b * X + c + np.random.normal(0, noise_std, num_points)
    return X, y


def main(config_dict):
    target = config_dict["target"]
    data_type = config_dict["type"]
    data_type_to_func = {
        "linear": generate_linear,
        "quadratic": generate_quadratic
    }
    X, y = data_type_to_func[data_type](**config_dict["args"])
    np.savetxt(target,
               np.column_stack([X, y]),
               delimiter=",",
               header="X,y",
               comments="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic data")
    parser.add_argument("config", type=str, help="Path to the config file")
    config_dict = load_config(parser.parse_args().config)
    main(config_dict)
