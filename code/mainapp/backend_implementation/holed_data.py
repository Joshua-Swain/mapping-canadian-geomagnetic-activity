import pandas as pd
import numpy as np
import logging
from .data import Data
from .filepaths import holed_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import *

class HoledData(Data):
	def __init__(self):
		Data.__init__(self)

		# Load the holed_dataset csv file into a DataFrame and retain only the relevant columns
		self.holed_dataset_df = pd.read_csv(holed_dataset_filepath)
		self.holed_sites = holed_dataset_site_names
		self.holed_df = self.holed_dataset_df[holed_dataset_site_names]
		#self.holed_data_target = self.holed_data[target_columns]
		self.holed_data_longitudes = []
		self.holed_data_latitudes = []
		for site in holed_dataset_site_names:
			self.holed_data_longitudes.append(self.holed_dataset_df[site + '_lon'][0])
			self.holed_data_latitudes.append(self.holed_dataset_df[site + '_lat'][0])

	def get_index_of_timestamp(self, timestamp):
		try:
			index = self.holed_dataset_df.index[self.holed_dataset_df['DD-HH'] == timestamp].to_list()[0]
		except:
			print(f"The timestamp {timestamp} is not present in the holed dataset. Instead, fetching the index for the timestamp 01-01")
			index = self.holed_dataset_df.index[self.holed_dataset_df['DD-HH'] == "01-01"].to_list()[0]
		print(f"holed data index is: {index}", flush=True)
		return index	