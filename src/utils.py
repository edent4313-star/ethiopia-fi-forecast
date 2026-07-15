import pandas as pd

def missing_summary(df):

    summary = pd.DataFrame()

    summary["Missing"] = df.isna().sum()

    summary["Percent"] = (

        df.isna().sum()/len(df)

    )*100

    return summary.sort_values(

        by="Percent",

        ascending=False

    )


def unique_values(df,column):

    return df[column].unique()


def dataframe_info(df):

    print(df.info())

    print(df.head())

    print(df.describe(include="all"))