import pandas as pd
import matplotlib.pyplot as plt


class ModelExplainability:

    """
    Explain Linear Regression model.
    """

    def __init__(self, model, feature_names):

        self.model = model

        self.feature_names = feature_names

    def coefficients(self):

        coef = pd.DataFrame({

            "Feature": self.feature_names,

            "Coefficient": self.model.coef_

        })

        coef["Absolute"] = coef["Coefficient"].abs()

        coef = coef.sort_values(

            "Absolute",

            ascending=False

        )

        return coef

    def plot(self):

        coef = self.coefficients()

        plt.figure(figsize=(10,5))

        plt.barh(

            coef["Feature"],

            coef["Coefficient"]

        )

        plt.title(

            "Feature Importance (Linear Regression Coefficients)"

        )

        plt.xlabel("Coefficient")

        plt.grid(True)

        plt.tight_layout()

        plt.show()