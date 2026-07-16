import pandas as pd

class Statistics:

    def __init__(self,data):

        self.data=data.copy()

    def growth_rate(self,column):

        df=self.data.sort_values(

            "observation_date"

        )

        df["growth"]=df[column].pct_change()*100

        return df

    def correlation(self):

        numeric=self.data.select_dtypes(

            include="number"

        )

        return numeric.corr()

    def missing(self):

        return self.data.isnull().sum()