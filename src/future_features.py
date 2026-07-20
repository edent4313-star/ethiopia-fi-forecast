import pandas as pd
import numpy as np


class FutureFeatureGenerator:
    """
    Generate future features (2025–2027) for scenario-based forecasting.
    """

    def __init__(self, historical_data):

        self.data = historical_data.copy()

    def generate(self):

        # -----------------------------
        # Last historical year
        # -----------------------------

        latest = self.data.sort_values("year").iloc[-1]

        future_years = [2025, 2026, 2027]

        records = []

        for i, year in enumerate(future_years, start=1):

            records.append({

                "year": year,

                # More financial inclusion events each year
                "event_count":
                    latest["event_count"] + i,

                # Events become slightly stronger
                "avg_impact":
                    latest["avg_impact"] * (1 + 0.05 * i),

                # Better implementation reduces lag
                "avg_lag":
                    max(
                        latest["avg_lag"] - 0.5 * i,
                        1
                    ),

                # Better quality evidence
                "high_confidence_events":
                    latest["high_confidence_events"] + i,

            

            })

        return pd.DataFrame(records)
    


    