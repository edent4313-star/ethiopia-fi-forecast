import pandas as pd


class EventModel:

    """
    Handle event and impact-link relationships.
    """

    def __init__(self, data, impact,observation,impact2):

        self.data = data
        self.impact = impact
        self.observation = observation
        self.impact2 = impact2

    def events(self):

        return self.data[
            self.data["record_type"] == "event"
        ]

    def observations(self):

        return self.data[
            self.data["record_type"] == "observation"
        ]

    def impact_links(self):

        return self.impact

    def merge_event_impacts(self):

        events = self.events()[
            [
            "record_id",
            "category",
            "indicator",
            "observation_date",
            "source_name",
            "source_type"
            ]
            ]

        impacts = self.impact[
            [
            "record_id",
            "parent_id",
            "pillar",
            "related_indicator",
            "relationship_type",
            "impact_direction",
            "impact_magnitude",
            "impact_estimate",
            "lag_months",
            "evidence_basis",
            "confidence",
            "comparable_country"

         ]
        ]

        merged = impacts.merge(
            events,
            left_on="parent_id",
            right_on="record_id",
            how="left",
            suffixes=("_impact", "_event")
            )

        return merged

    def event_summary(self):

        merged = self.merge_event_impacts()

        return merged[
            [
                "parent_id",
                "observation_date",
                "category",
                "related_indicator",
                "impact_direction",
                "impact_magnitude",
                "lag_months",
                "evidence_basis",
                "comparable_country"
            ]
        ]