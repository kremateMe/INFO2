import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy
import matplotlib
import plotly
import sklearn
import zipfile
import os

class DatasetPreprocessor:

    #@property
    #def zip_file_path(self):



    def __init__(self, zip_file_path) -> None:
        self.zip_file_path = zip_file_path
        with zipfile.ZipFile(self.zip_file_path) as myzip:
            with myzip.open("AirQualityUCI.csv") as data_file:
                self._data_raw = data_file.read()
                
    #def to_csv(self, csv_file_path) -> None:
        



a=2
