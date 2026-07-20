import numpy as np
import pandas as pd

from sklearn.model_selection import LeaveOneOut
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class ForecastValidation:

    """
    Leave-One-Out Cross Validation
    for very small datasets.
    """

    def __init__(self):

        self.model = LinearRegression()

    def validate(self, X, y):

        loo = LeaveOneOut()

        predictions = []
        actuals = []

        for train_index, test_index in loo.split(X):

            X_train = X.iloc[train_index]
            X_test = X.iloc[test_index]

            y_train = y.iloc[train_index]
            y_test = y.iloc[test_index]

            self.model.fit(X_train, y_train)

            pred = self.model.predict(X_test)[0]

            predictions.append(pred)

            actuals.append(y_test.values[0])

        mae = mean_absolute_error(actuals, predictions)

        rmse = np.sqrt(
            mean_squared_error(actuals, predictions)
        )

        r2 = r2_score(actuals, predictions)

        result = pd.DataFrame({

            "Actual": actuals,

            "Predicted": predictions

        })

        return result, mae, rmse, r2