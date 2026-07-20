import pandas as pd


class ScenarioForecast:

    """
    Create optimistic, baseline and pessimistic forecasts.
    """

    def __init__(self, forecast):

        self.forecast = forecast.copy()

    def generate(self):

        self.forecast["base"] = self.forecast["forecast"]

        self.forecast["optimistic"] = self.forecast["forecast"] * 1.05

        self.forecast["pessimistic"] = self.forecast["forecast"] * 0.95

        return self.forecast