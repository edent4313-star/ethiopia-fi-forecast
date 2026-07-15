from src.data_loader import DataLoader

from src.config import RAW_DATA


def test_columns():

    loader=DataLoader(RAW_DATA)

    df=loader.load_excel(

        "ethiopia_fi_unified_data.xlsx"

    )

    required=[

        "record_type",

        "record_id"

    ]

    for col in required:

        assert col in df.columns