import pandas as pd
import numpy as np
import logging
from .data import Data
from .filepaths import full_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import *

class FullData(Data):
	def __init__(self):
		Data.__init__(self)

		# Load the full_dataset csv file into a DataFrame and retain only the relevant columns
		self.full_dataset_df = pd.read_csv(full_dataset_filepath)
		self.full_sites = full_dataset_site_names
		self.full_df = self.full_dataset_df[full_dataset_site_names]
		#self.full_data_target = self.full_dataset[target_columns]
		self.full_data_longitudes = []
		self.full_data_latitudes = []
		for site in full_dataset_site_names:
			self.full_data_longitudes.append(self.full_dataset_df[site + '_lon'][0])
			self.full_data_latitudes.append(self.full_dataset_df[site + '_lat'][0])

	def get_index_of_timestamp(self, timestamp):
		try:
			index = self.full_dataset_df.index[self.full_dataset_df['DD-HH'] == timestamp].to_list()[0]
		except:
			print(f"The timestamp {timestamp} is not present in the full dataset. Instead, fetching the index for the timestamp 01-01")
			index = self.full_dataset_df.index[self.full_dataset_df['DD-HH'] == "01-01"].to_list()[0]
		print(f"full data index is: {index}", flush=True)
		return index