import pandas as pd
import numpy as np


class EventFeatureEngineering:

    """
    Create ML-ready event features.
    """

    def __init__(self, observations, impacts):

        self.observations = observations.copy()
        self.impacts = impacts[
          [
             "parent_id",
             "observation_date",
             "category",
             "confidence",
             "impact_estimate",
             "lag_months"
            ]
          ].copy()
    def prepare_dates(self):

        self.observations["observation_date"] = pd.to_datetime(
            self.observations["observation_date"]
        )

        return self.observations

    def yearly_events(self):

        events = self.impacts.copy()

        events["observation_date"] = pd.to_datetime(
            events["observation_date"]
        )

        events["year"] = events["observation_date"].dt.year

        return events.groupby("year").size().reset_index(
            name="event_count"
        )

    def yearly_observations(self):

        obs = self.prepare_dates()

        obs["year"] = obs["observation_date"].dt.year

        return obs

    def merge_event_counts(self):

        obs = self.yearly_observations()

        yearly_events = self.yearly_events()

        merged = obs.merge(

            yearly_events,

            on="year",

            how="left"

        )

        merged["event_count"] = merged["event_count"].fillna(0)

        return merged

    def build_features(self):

        # -------------------------
        # Convert dates
        # -------------------------

        self.observations["observation_date"] = pd.to_datetime(
            self.observations["observation_date"]
        )

        self.impacts["observation_date"] = pd.to_datetime(
            self.impacts["observation_date"]
        )

        # -------------------------
        # Extract years
        # -------------------------

        self.observations["year"] = (
            self.observations["observation_date"].dt.year
        )

        self.impacts["year"] = (
            self.impacts["observation_date"].dt.year
        )

        # -------------------------
        # Event Count
        # -------------------------

        event_count = (

            self.impacts

            .groupby("year")

            .size()

            .reset_index(name="event_count")

        )

        # -------------------------
        # Average Impact
        # -------------------------

        avg_impact = (

            self.impacts

            .groupby("year")["impact_estimate"]

            .mean()

            .reset_index(name="avg_impact")

        )

        # -------------------------
        # Average Lag
        # -------------------------

        avg_lag = (

            self.impacts

            .groupby("year")["lag_months"]

            .mean()

            .reset_index(name="avg_lag")

        )

        # -------------------------
        # High Confidence Events
        # -------------------------

        high = self.impacts[
            self.impacts["confidence"] == "high"
        ]

        high = (

            high

            .groupby("year")

            .size()

            .reset_index(name="high_confidence_events")

        )

        # -------------------------
        # Merge
        # -------------------------

        df = self.observations.copy()

        df = df.merge(

            event_count,

            on="year",

            how="left"

        )

        df = df.merge(

            avg_impact,

            on="year",

            how="left"

        )

        df = df.merge(

            avg_lag,

            on="year",

            how="left"

        )

        df = df.merge(

            high,

            on="year",

            how="left"

        )

        # -------------------------
        # Missing Values
        # -------------------------

        df["event_count"] = df["event_count"].fillna(0)

        df["avg_impact"] = df["avg_impact"].fillna(0)

        df["avg_lag"] = df["avg_lag"].fillna(0)

        df["high_confidence_events"] = (

            df["high_confidence_events"]

            .fillna(0)

        )

        return df