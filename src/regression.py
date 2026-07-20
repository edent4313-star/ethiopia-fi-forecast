from sklearn.linear_model import LinearRegression


class EventRegression:

    """
    Simple baseline regression for forecasting.
    """

    def __init__(self):

        self.model = LinearRegression()

    def fit(self, X, y):

        self.model.fit(X, y)

    def predict(self, X):

        return self.model.predict(X)

    def score(self, X, y):

        return self.model.score(X, y)