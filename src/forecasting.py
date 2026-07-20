import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


class ForecastModel:

    """
    Baseline forecasting model using Linear Regression.
    """

    def __init__(self):

        self.model = LinearRegression()

    def fit(self, X, y):

        self.model.fit(X, y)

    def predict(self, X):

        return self.model.predict(X)

    def forecast(self, future_df):

        predictions = self.model.predict(future_df)

        future_df = future_df.copy()

        future_df["forecast"] = predictions

        return future_df