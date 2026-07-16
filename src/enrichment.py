from asyncio import events
import numpy as np
import pandas as pd
from datetime import datetime

def create_observations():
    # Adding new observation data (e.g., Findex microdata for a new year)
    new_obs_data = {
        'record_id': ['REC_0044', 'REC_0045'],
        'record_type': ['observation', 'observation'],
        'category': [np.nan, np.nan],
        'pillar': ['ACCESS', 'ACCESS'],
        'indicator': ['Account Ownership Rate', 'Account Ownership Rate'],
        'indicator_code': ['ACC_OWNERSHIP', 'ACC_OWNERSHIP'],
        'indicator_direction': ['higher_better', 'higher_better'],
        'value_numeric': [60.0, 50.0],
        'value_text': [np.nan, np.nan],
        'value_type': ['percentage', 'percentage'],
        'unit': ['%', '%'],
        'observation_date': [pd.to_datetime('2023-12-31'), pd.to_datetime('2023-12-31')],
        'period_start': [np.nan, np.nan],
        'period_end': [np.nan, np.nan],
        'fiscal_year': [2023, 2023],
        'gender': ['male', 'female'],
        'location': ['national', 'national'],
        'region': [np.nan, np.nan],
        'source_name': ['Global Findex 2023 (Hypothetical)', 'Global Findex 2023 (Hypothetical)'],
        'source_type': ['survey', 'survey'],
        'source_url': ['https://www.worldbank.org/en/publication/global-findex', 'https://www.worldbank.org/en/publication/global-findex'],
        'confidence': ['medium', 'medium'],
        'related_indicator': [np.nan, np.nan],
        'relationship_type': [np.nan, np.nan],
        'impact_direction': [np.nan, np.nan],
        'impact_magnitude': [np.nan, np.nan],
        'impact_estimate': [np.nan, np.nan],
        'lag_months': [np.nan, np.nan],
        'evidence_basis': [np.nan, np.nan],
        'comparable_country': ['Example_Trainee', 'Example_Trainee'],
        'collected_by': ['AI Agent', 'AI Agent'],
        'collection_date': ['2026-07-16', '2026-07-16'],
        'original_text': ['Account ownership for males in 2023', 'Account ownership for females in 2023'],
        'notes': ['Hypothetical data for enrichment', 'Hypothetical data for enrichment']
        }
    return pd.DataFrame(new_obs_data)

def create_events():
    #  Adding a new policy event
    new_event_data = {
        'record_id': ['EVT_0011'],
        'record_type': ['event'],
        'category': ['policy'],
        'pillar': [np.nan], # As per instruction, leave pillar empty for events
        'indicator': ['Digital Financial Services Regulation'],
        'indicator_code': ['EVT_DFSR'],
        'indicator_direction': [np.nan],
        'value_numeric': [np.nan],
        'value_text': ['Implemented'],
        'value_type': ['categorical'],
        'unit': [np.nan],
        'observation_date': [pd.to_datetime('2024-03-01')],
        'period_start': [np.nan],
        'period_end': [np.nan],
        'fiscal_year': [2024],
        'gender': ['all'],
        'location': ['national'],
        'region': [np.nan],
        'source_name': ['National Bank of Ethiopia'],
        'source_type': ['regulator'],
        'source_url': ['https://www.nbe.gov.et/'],
        'confidence': ['high'],
        'related_indicator': [np.nan],
        'relationship_type': [np.nan],
        'impact_direction': [np.nan],
        'impact_magnitude': [np.nan],
        'impact_estimate': [np.nan],
        'lag_months': [np.nan],
        'evidence_basis': [np.nan],
        'comparable_country': ['Example_Trainee'],
        'collected_by': ['AI Agent'],
        'collection_date': ['2026-07-16'],
        'original_text': ['New regulatory framework for digital financial services'],
        'notes': ['Hypothetical policy to encourage innovation']
        }
    return pd.DataFrame(new_event_data)

def create_impact_links():
    # Adding new impact link for the Digital Financial Services Regulation event
    new_impact_data = {
        'record_id': ['IMP_0015'],
        'parent_id': ['EVT_0011'], # Link to the new event
        'record_type': ['impact_link'],
        'category': [np.nan],
        'pillar': ['USAGE'],
        'indicator': ['Impact of DFS Regulation on Mobile Money Users'],
        'indicator_code': [np.nan],
        'indicator_direction': [np.nan],
        'value_numeric': [20.0],
        'value_text': [np.nan],
        'value_type': ['percentage'],
        'unit': ['%'],
        'observation_date': [pd.to_datetime('2024-03-01')], # Same as event date
        'period_start': [np.nan],
        'period_end': [np.nan],
        'fiscal_year': [np.nan],
        'gender': ['all'],
        'location': ['national'],
        'region': [np.nan],
        'source_name': [np.nan],
        'source_type': [np.nan],
        'source_url': [np.nan],
        'confidence': ['medium'],
        'related_indicator': ['USG_MM_USERS'], # Example: related to mobile money users
        'relationship_type': ['direct'],
        'impact_direction': ['increase'],
        'impact_magnitude': ['medium'],
        'impact_estimate': [20.0],
        'lag_months': [6],
        'evidence_basis': ['literature'],
        'comparable_country': ['Kenya'],
        'collected_by': ['AI Agent'],
        'collection_date': [pd.to_datetime('2026-07-16')],
        'original_text': [np.nan],
        'notes': ['Improved regulatory clarity leads to increased mobile money adoption']
        }
    return pd.DataFrame(new_impact_data)

def create_observations_2():

        observations = [

        {
            "record_id":"OBS_NEW_001",
            "parent_id":"",
            "record_type":"observation",
            "category":"",
            "pillar":"ACCESS",
            "indicator":"Female Account Ownership",
            "indicator_code":"ACC_FEMALE",
            "value_numeric":43.0,
            "observation_date":"2024-01-01",
            "source_type":"survey",
            "source_name":"Global Findex 2024",
            "source_url":"https://www.worldbank.org/en/publication/globalfindex",
            "confidence":"High",
            "original_text":"43% of women own an account.",
            "collected_by":"Your Name",
            "collection_date":datetime.today().strftime("%Y-%m-%d"),
            "notes":"Useful for gender analysis."
            },

            {
            "record_id":"OBS_NEW_002",
            "parent_id":"",
            "record_type":"observation",
            "category":"",
            "pillar":"ACCESS",
            "indicator":"Male Account Ownership",
            "indicator_code":"ACC_MALE",
            "value_numeric":55,
            "observation_date":"2024-01-01",
            "source_type":"survey",
            "source_name":"Global Findex 2024",
            "source_url":"https://www.worldbank.org/en/publication/globalfindex",
            "confidence":"High",
            "original_text":"55% of men own an account.",
            "collected_by":"Your Name",
            "collection_date":datetime.today().strftime("%Y-%m-%d"),
            "notes":"Gender comparison."
            },

            {
            "record_id":"OBS_NEW_003",
            "parent_id":"",
            "record_type":"observation",
            "category":"",
            "pillar":"USAGE",
            "indicator":"Smartphone Penetration",
            "indicator_code":"INF_SMARTPHONE",
            "value_numeric":31,
            "observation_date":"2024-01-01",
            "source_type":"telecom",
            "source_name":"GSMA",
            "source_url":"https://www.gsma.com/",
            "confidence":"Medium",
            "original_text":"Estimated smartphone penetration.",
            "collected_by":"Your Name",
            "collection_date":datetime.today().strftime("%Y-%m-%d"),
            "notes":"Important predictor."
            }

            ]

        return pd.DataFrame(observations)
def create_events_2():

        events = [

        {

            "record_id":"EVT_NEW_001",

            "parent_id":"",

            "record_type":"event",

            "category":"policy",

            "pillar":"",

            "indicator":"National Digital Strategy",

            "indicator_code":"",

            "value_numeric":"",

            "observation_date":"2024-06-01",

            "source_type":"government",

            "source_name":"NBE",

            "source_url":"https://nbe.gov.et",

            "confidence":"High"

            },

            {

            "record_id":"EVT_NEW_002",

            "parent_id":"",

            "record_type":"event",

            "category":"partnership",

            "pillar":"",

            "indicator":"Telebirr and EthSwitch Integration",

            "indicator_code":"",

            "value_numeric":"",

            "observation_date":"2024-03-15",

            "source_type":"news",

            "source_name":"EthSwitch",

            "source_url":"https://ethswitch.com",

            "confidence":"High"

            }

            ]

        return pd.DataFrame(events)
def create_impact_links_2():

    impacts=[

        {

            "record_id":"IMP_NEW_001",

            "parent_id":"EVT_NEW_001",

            "record_type":"impact_link",

            "pillar":"ACCESS",

            "related_indicator":"ACC_OWNERSHIP",

            "impact_direction":"increase",

            "impact_magnitude":"medium",

            "lag_months":12,

            "evidence_basis":"Government policy"

            },

            {

            "record_id":"IMP_NEW_002",

            "parent_id":"EVT_NEW_002",

            "record_type":"impact_link",

            "pillar":"USAGE",

            "related_indicator":"USG_DIGITAL_PAYMENT",

            "impact_direction":"increase",

            "impact_magnitude":"high",

            "lag_months":6,

            "evidence_basis":"Integration increases interoperability"

         }

            ]

    return pd.DataFrame(impacts)
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




   