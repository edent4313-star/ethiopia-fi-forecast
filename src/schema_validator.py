import pandas as pd

from src.logger import logger

from src.exceptions import ValidationError


class SchemaValidator:

    """
    Validate unified financial inclusion schema.
    """

    def __init__(self, df):

        self.df = df


    def required_columns(self):

        required = [

            "record_id",
            "parent_id",
            "record_type",
            "category",
            "pillar",
            "indicator",
            "indicator_code",
            "value_numeric",
            "observation_date",
            "source_name",
            "source_url",
            "confidence"

        ]

        missing = [

            col

            for col in required

            if col not in self.df.columns

        ]

        if len(missing) > 0:

            raise ValidationError(

                f"Missing columns : {missing}"

            )

        logger.info("Required columns exist.")


    def duplicate_records(self):

        dup = self.df.duplicated(

            subset=["record_id"]

        )

        logger.info(

            f"Duplicate Record IDs : {dup.sum()}"

        )

        return self.df.loc[dup]


    def missing_values(self):

        return self.df.isna().sum()


    def validate_record_types(self):

        allowed = [

            "observation",

            "event",

            "impact_link",

            "target"

        ]

        invalid = self.df.loc[

            ~self.df["record_type"].isin(allowed)

        ]

        return invalid


    def run_all(self):

        self.required_columns()

        self.duplicate_records()

        self.validate_record_types()

        logger.info("Schema validation complete.")