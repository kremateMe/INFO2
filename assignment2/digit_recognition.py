
import numpy as np
import pandas as pd
from pandas import DataFrame
import scipy
import matplotlib as mpl
import plotly
import sklearn
import zipfile
import os
from pathlib import Path

#class DatasetPreprocessor:

    #@property
    #def zip_file_path(self):



    #def __init__(self, zip_file_path) -> None:
        #self.zip_file_path = zip_file_path
        #with zipfile.ZipFile(self.zip_file_path) as myzip:
            #with myzip.open("AirQualityUCI.csv") as data_file:
                #self._data_raw = data_file.read()

    #def to_csv(self, csv_file_path) -> None:




class DatasetPreprocessor:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path
        self._data = self._preprocess_data()

    def _preprocess_data(self):
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(Path(self.zip_file_path).with_suffix(''))

        csv_files = Path(self.zip_file_path).with_suffix('').glob('*.csv')
        data_frames = [pd.read_csv(file) for file in csv_files]
        data = pd.concat(data_frames, ignore_index=True)
        numeric_cols = data.select_dtypes(include='number').columns
        data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].mean())
        return data

    def to_csv(self, csv_file_path):
        if self._data.empty:
            return
        data = self._data.copy()
        if 'target_variable' in data.columns:
            data = data[[col for col in data.columns if col != 'target_variable'] + ['target_variable']]
        data.to_csv(csv_file_path, index=False)

#test:

zip_file_path = r'C:\Users\Anna\OneDrive\Dokumente\Info_Assignment_02\INFO2-main\INFO2-main\assignment2\air+quality.zip'
preprocessor = DatasetPreprocessor(zip_file_path)
processed_data = preprocessor._data
print(processed_data.head())

csv_output_path = r'C:\Users\Anna\OneDrive\Dokumente\Info_Assignment_02\INFO2-main\INFO2-main\assignment2\processed_data.csv'

preprocessor.to_csv(csv_output_path)
