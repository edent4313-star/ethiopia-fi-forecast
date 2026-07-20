import pandas as pd


class ImpactAnalysis:

    def __init__(self, merged):

        self.data = merged.copy()

    def impact_by_pillar(self):

        return self.data.groupby(

            "pillar"

        ).size()

    def impact_direction(self):

        return self.data["impact_direction"].value_counts()

    def impact_magnitude(self):

        return self.data["impact_magnitude"].value_counts()

    def average_lag(self):

        return self.data.groupby(

            "impact_direction"

        )["lag_months"].mean()

    def evidence_summary(self):

        return self.data["evidence_basis"].value_counts()