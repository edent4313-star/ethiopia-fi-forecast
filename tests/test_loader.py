from src.data_loader import DataLoader
from src.config import RAW_DATA


def test_data_loading():

    loader=DataLoader(RAW_DATA)

    df=loader.load_excel(

        "ethiopia_fi_unified_data.xlsx"

    )

    assert len(df)>0