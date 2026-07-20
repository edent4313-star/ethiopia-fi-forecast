import os
import io
import pandas as pd

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
    def __init__(self,data):

        self.data=data

    def record_type(self):

        plt.figure(figsize=(8,5))

        sns.countplot(

            data=self.data,

            x="record_type"

        )

        plt.show()

    def pillar(self):

        plt.figure(figsize=(10,5))

        sns.countplot(

            data=self.data,

            x="pillar"

        )

        plt.xticks(rotation=45)

        plt.show()

    def confidence(self):

        plt.figure(figsize=(8,5))

        sns.countplot(

            data=self.data,

            x="confidence"

        )

        plt.show()

    def source(self):

        plt.figure(figsize=(10,5))

        sns.countplot(

            data=self.data,

            x="source_type"

        )

        plt.xticks(rotation=45)

        plt.show()

    def indicator(self):

        plt.figure(figsize=(14,6))

        self.data["indicator_code"].value_counts().plot.bar()

        plt.xticks(rotation=90)

        plt.show()

    def correlation(self,corr):

        plt.figure(figsize=(10,8))

        sns.heatmap(

            corr,

            annot=True,

            cmap="Blues"

        )

        plt.show()

    def __init__(self, data):
        self.data = data

    def pillar_plot(self):
        plt.figure(figsize=(10,5))
        sns.countplot(data=self.data, x="pillar")
        plt.xticks(rotation=45)
        plt.title("Pillar Distribution")
        # IMPORTANT: We do NOT call plt.show() here, 
        # otherwise the image is cleared before we can save it.

    def upload_plt_to_gcs(self, num_fig, step):
        """
        Now a method inside the class. 
        Note: we use 'self' and we fixed 'plt.step' to just 'step'.
        """
        # Define the local path
        local_dir = f'../reports/figures/{step}'
        os.makedirs(local_dir, exist_ok=True)
        local_path = os.path.join(local_dir, f'figure_{num_fig}.png')

        # Save the current active plot (plt)
        plt.savefig(local_path, format='png', bbox_inches='tight')

        print(f'Saved figure_{num_fig}.png to {local_path}')

        # Clear and close after saving
        plt.clf()
        plt.close()
    
    def __init__(self, merged):

        self.data = merged

    def impact_direction(self):

        plt.figure(figsize=(6,4))

        sns.countplot(

            data=self.data,

            x="impact_direction"

        )

        plt.title("Impact Direction")

        plt.show()

    def impact_magnitude(self):

        plt.figure(figsize=(6,4))

        sns.countplot(

            data=self.data,

            x="impact_magnitude"

        )

        plt.title("Impact Magnitude")

        plt.show()

    def lag_distribution(self):

        plt.figure(figsize=(8,5))

        sns.histplot(

            self.data["lag_months"],

            bins=10

        )

        plt.title("Lag Distribution")

        plt.show()

    def event_heatmap(self):

        matrix = pd.crosstab(

            self.data["category"],

            self.data["related_indicator"]

        )

        plt.figure(figsize=(12,6))

        sns.heatmap(

            matrix,

            annot=True,

            cmap="Blues"

        )

        plt.show()


class ForecastVisualization:

    def __init__(self, history, future):

        self.history = history

        self.future = future

    def forecast_plot(self):

        plt.figure(figsize=(10,5))

        plt.plot(

            self.history["year"],

            self.history["value_numeric"],

            marker="o",

            label="Historical"

        )

        plt.plot(

            self.future["year"],

            self.future["base"],

            marker="s",

            label="Forecast"

        )

        plt.fill_between(

            self.future["year"],

            self.future["pessimistic"],

            self.future["optimistic"],

            alpha=0.25,

            label="Forecast Range"

        )

        plt.xlabel("Year")

        plt.ylabel("Account Ownership (%)")

        plt.title("Financial Inclusion Forecast")

        plt.legend()

        plt.grid(True)

        plt.show()