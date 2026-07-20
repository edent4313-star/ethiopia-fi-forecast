from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np


class Metrics:

    @staticmethod
    def evaluate(y_true, y_pred):

        print("MAE :", mean_absolute_error(y_true, y_pred))

        print("RMSE :", np.sqrt(

            mean_squared_error(y_true, y_pred)

        ))

        print("R² :", r2_score(

            y_true,

            y_pred

        ))