class exploratory_data_analysis:

    def __init__(self,data):

        self.data=data.copy()

    def observations(self):

        return self.data[
            self.data["record_type"]=="observation"
        ]

    def events(self):

        return self.data[
            self.data["record_type"]=="event"
        ]

    def targets(self):

        return self.data[
            self.data["record_type"]=="target"
        ]

    def summary(self):

        return self.data.describe(include="all")

    def record_counts(self):

        return self.data["record_type"].value_counts()

    def pillar_counts(self):

        return self.data["pillar"].value_counts()

    def source_counts(self):

        return self.data["source_type"].value_counts()

    def confidence_counts(self):

        return self.data["confidence"].value_counts()

    def indicators(self):

        return self.data["indicator_code"].value_counts()

    def temporal_range(self):

        df=self.observations()

        return (

            df["observation_date"].min(),

            df["observation_date"].max()

        )