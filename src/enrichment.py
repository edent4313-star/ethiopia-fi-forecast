import pandas as pd


class DataEnrichment:

    """
    Add additional observations,
    events,
    and impact links.
    """

    def __init__(self, df):

        self.df = df.copy()


    def add_observation(

        self,

        record

    ):

        self.df = pd.concat(

            [

                self.df,

                pd.DataFrame([record])

            ],

            ignore_index=True

        )

        return self.df


    def add_event(

        self,

        record

    ):

        self.df = pd.concat(

            [

                self.df,

                pd.DataFrame([record])

            ],

            ignore_index=True

        )

        return self.df


    def add_impact(

        self,

        record

    ):

        self.df = pd.concat(

            [

                self.df,

                pd.DataFrame([record])

            ],

            ignore_index=True

        )

        return self.df


    def save(

        self,

        path

    ):

        self.df.to_csv(

            path,

            index=False

        )

        print("Processed data saved.")