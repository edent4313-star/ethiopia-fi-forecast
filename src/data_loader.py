import pandas as pd

from src.logger import logger

from src.exceptions import DataLoadError


class DataLoader:

    def __init__(self,data_path):

        self.data_path=data_path


    def load_excel(self,file_name,sheet_name=0):

        try:

            file=self.data_path/file_name

            df=pd.read_excel(file,sheet_name=sheet_name)

            logger.info(f"{file_name} loaded successfully")

            return df

        except Exception as e:

            raise DataLoadError(e)


    def load_markdown(self,file_name):

        file=self.data_path/file_name

        with open(file,"r",encoding="utf-8") as f:

            return f.read()