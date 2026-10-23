import pandas as pd
from sklearn.datasets import fetch_california_housing


def main():
    data = fetch_california_housing()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df["Price"] = data.target
    print("shape: ", df.shape)
    print(df.head())
    print(df.describe())


if __name__ == "__main__":
    main()
