import pandas as pd
class Insight:

    def __init__(self,data):

        self.data=data

    def generate(self):

        insights=[]

        insights.append(
            "Account ownership has steadily increased across survey years."
        )

        insights.append(
            "Digital payment adoption accelerated after major mobile money initiatives."
        )

        insights.append(
            "High-confidence observations dominate the dataset."
        )

        insights.append(
            "Events are strongly connected to ACCESS and USAGE indicators."
        )

        insights.append(
            "Infrastructure indicators appear to be leading indicators for financial inclusion."
        )

        return insights
    import pandas as pd


    def __init__(self, data):

        self.data = data.copy()
        
    def generate(self):
        observations = self.data[self.data["record_type"] == "observation"].copy()
    
        # 1. Convert with flexibility
        observations["observation_date"] = pd.to_datetime(
        observations["observation_date"], 
        errors='coerce'
    )
    
        # 2. Drop any rows that failed to convert (NaT)
        observations = observations.dropna(subset=["observation_date"])
    
        # 3. Now min/max will work perfectly
        start = observations["observation_date"].min()
        end = observations["observation_date"].max()
    
        insights = []
    
        # Check for NaT (Not a Time) to prevent crashes if data is empty
        if pd.notnull(start) and pd.notnull(end):
            insights.append(
            f"The dataset contains observations from {start.date()} to {end.date()}."
            )

        # Most common pillar
        pillar = observations["pillar"].value_counts().idxmax()

        events = self.data[self.data["record_type"] == "event"]

        insights.append(
            f"The {pillar} pillar has the largest number of observations."
        )

        # Most frequent indicator
        indicator = observations["indicator"].value_counts().idxmax()

        insights.append(
            f"The most frequently reported indicator is '{indicator}'."
        )

        # Confidence
        confidence = self.data["confidence"].value_counts().idxmax()

        insights.append(
            f"Most records have '{confidence}' confidence, indicating reliable data."
        )

        # Events
        insights.append(
            f"The dataset contains {len(events)} financial inclusion events that can be used to explain historical changes."
        )

        return insights