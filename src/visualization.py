import os
import io

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