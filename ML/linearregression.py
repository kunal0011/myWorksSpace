import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
    FunctionTransformer,
)
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import rbf_kernel


def load_housing_data():
    """Loads the housing dataset from a CSV file."""
    csv_path = "datasets/housing/housing.csv"  # Update with your file path
    return pd.read_csv(csv_path)


def shuffle_and_split_data(data, test_ratio):
    """Shuffles and splits the data into training and testing sets."""
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


def income_cat_proportions(data):
    """Calculates the proportions of income categories in the data."""
    return data["income_cat"].value_counts() / len(data)


class ClusterSimilarity(BaseEstimator, TransformerMixin):
    """
    Custom transformer to calculate similarity to cluster centers using RBF kernel.
    """

    def __init__(self, n_clusters=10, gamma=1.0, random_state=None):
        self.n_clusters = n_clusters
        self.gamma = gamma
        self.random_state = random_state

    def fit(self, X, y=None, sample_weight=None):
        self.kmeans_ = KMeans(self.n_clusters, n_init="auto",  # Use n_init="auto" for Scikit-Learn >= 1.4
                              random_state=self.random_state)
        self.kmeans_.fit(X, sample_weight=sample_weight)
        return self  # always return self!

    def transform(self, X):
        return rbf_kernel(X, self.kmeans_.cluster_centers_, gamma=self.gamma)

    def get_feature_names_out(self, names=None):
        return [f"Cluster {i} similarity" for i in range(self.n_clusters)]


def column_ratio(X):
    return X[:, [0]] / X[:, [1]]


def ratio_name(function_transformer, feature_names_in):
    return ["ratio"]  # feature names out


def ratio_pipeline():
    return make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(column_ratio, feature_names_out=ratio_name),
        StandardScaler())


def build_pipeline():
    num_pipeline = make_pipeline(SimpleImputer(
        strategy="median"), StandardScaler())
    cat_pipeline = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(handle_unknown="ignore", sparse_output=False),
    )
    log_pipeline = make_pipeline(
        SimpleImputer(strategy="median"),
        FunctionTransformer(np.log, feature_names_out="one-to-one"),
        StandardScaler())
    cluster_simil = ClusterSimilarity(n_clusters=10, gamma=1., random_state=42)
    default_num_pipeline = make_pipeline(
        SimpleImputer(strategy="median"), StandardScaler())

    preprocessing = ColumnTransformer(
        [
            ("bedrooms", ratio_pipeline(), ["total_bedrooms", "total_rooms"]),
            ("rooms_per_house", ratio_pipeline(),
             ["total_rooms", "households"]),
            ("people_per_house", ratio_pipeline(),
             ["population", "households"]),
            ("log", log_pipeline, [
             "total_bedrooms", "total_rooms", "population", "households", "median_income"]),
            ("geo", cluster_simil, ["latitude", "longitude"]),
            ("cat", cat_pipeline, make_column_selector(dtype_include=object)),
        ],
        remainder=default_num_pipeline,  # one column remaining: housing_median_age
    )

    full_pipeline = Pipeline([
        ("preprocessing", preprocessing),
        ("random_forest", RandomForestRegressor(random_state=42)),
    ])
    return full_pipeline


def main():
    """Main function to run the algorithm."""
    # 1. Load data and create income categories
    housing = load_housing_data()
    housing["income_cat"] = pd.cut(
        housing["median_income"],
        bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
        labels=[1, 2, 3, 4, 5],
    )

    # 2. Stratified split into training and testing sets
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    for train_index, test_index in split.split(housing, housing["income_cat"]):
        strat_train_set = housing.loc[train_index]
        # strat_test_set = housing.loc[test_index]  # not used for training evaluation

    housing_train = strat_train_set.drop("median_house_value", axis=1)
    housing_labels = strat_train_set["median_house_value"].copy()

    # 3. Build pipeline and train model
    full_pipeline = build_pipeline()
    full_pipeline.fit(housing_train, housing_labels)

    # 4. Evaluate on training set
    predictions = full_pipeline.predict(housing_train)
    mse = mean_squared_error(housing_labels, predictions)
    rmse = np.sqrt(mse)
    print(f"RMSE on training set: {rmse}")


if __name__ == "__main__":
    main()
