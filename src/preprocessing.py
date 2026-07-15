import pandas as pd


class Preprocessor:

    def __init__(self, df):

        self.df = df.copy()


    def convert_dates(self):

        self.df["observation_date"] = pd.to_datetime(

            self.df["observation_date"],

            errors="coerce"

        )

        return self.df


    def fill_missing(self):

        text_cols = self.df.select_dtypes(

            include="object"

        ).columns

        self.df[text_cols] = self.df[text_cols].fillna("")

        return self.df


    def extract_observations(self):

        return self.df[

            self.df.record_type == "observation"

        ]


    def extract_events(self):

        return self.df[

            self.df.record_type == "event"

        ]


    def extract_targets(self):

        return self.df[

            self.df.record_type == "target"

        ]


    def extract_impacts(self):

        return self.df[

            self.df.record_type == "impact_link"

        ]


    def summary(self):

        print(self.df.shape)

        print(self.df.head())

        return self.df.describe(include="all")