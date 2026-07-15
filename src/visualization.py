import matplotlib.pyplot as plt

import seaborn as sns


class Visualizer:

    def __init__(self, df):

        self.df = df


    def record_type_plot(self):

        plt.figure(figsize=(8,5))

        sns.countplot(

            data=self.df,

            x="record_type"

        )

        plt.title("Record Type Distribution")

        plt.tight_layout()

        plt.show()


    def pillar_plot(self):

        plt.figure(figsize=(10,5))

        sns.countplot(

            data=self.df,

            x="pillar"

        )

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()


    def confidence_plot(self):

        plt.figure(figsize=(8,5))

        sns.countplot(

            data=self.df,

            x="confidence"

        )

        plt.tight_layout()

        plt.show()


    def indicator_plot(self):

        plt.figure(figsize=(12,6))

        self.df["indicator_code"].value_counts().plot.bar()

        plt.xticks(rotation=90)

        plt.tight_layout()

        plt.show()


    def yearly_observations(self):

        obs = self.df[

            self.df.record_type == "observation"

        ]

        yearly = (

            obs

            .groupby(

                obs["observation_date"].dt.year

            )

            .size()

        )

        yearly.plot(

            marker="o"

        )

        plt.ylabel("Number of Observations")

        plt.title("Observation Timeline")

        plt.grid(True)

        plt.show()