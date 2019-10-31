import pandas as pd
import numpy as np
import logging
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
from .filepaths import full_dataset_filepath, holed_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import *
from backend_implementation.holed_data import HoledData
from backend_implementation.full_data import FullData

class Kriging():

	def __init__(self, index, data):
		self.moving_avg_size = 2
		self.sites_output_df = None
		self.data_moving_avg = self.calculate_moving_average(data)
		self.kriging_output  = self.perform_kriging(index, data)
		print(f"The results of kriging are: {self.kriging_output}", flush=True)


	def calculate_moving_average(self, data):
		# After experiementing with different sizes, it was found that using a moving 
		# average over every 2 samples led to the best performing kriging model.
		# Moving average: https://en.wikipedia.org/wiki/Moving_average
		return data.df.rolling(self.moving_avg_size).mean()

	def perform_kriging(self, index, data):
		# Since we are using a rolling average, the average of the first moving_avg_size - 1 rows will be NaN.
		# Hence, we use the first non-NaN row from the dataset to determine the magnetic field.
		if index < (self.moving_avg_size - 1):
			index = self.moving_avg_size - 1

		# Perform Ordinary Kriging: https://pykrige.readthedocs.io/en/latest/overview.html#ordinary-kriging-example
		OK = OrdinaryKriging(data.longitudes, data.latitudes, data.df.loc[index], variogram_model='spherical', 
			verbose=False, enable_plotting=False, coordinates_type='geographic')
		z1, ss1 = OK.execute('grid', data.longitude_grid, data.latitude_grid)

		# These values are the indinces (long,lat) which correspond to the magnetic field reading at the site MEA
		index_of_mea_longitude = np.where(data.longitude_grid == mea_longitude)[0][0]
		index_of_mea_latitude = np.where(data.latitude_grid == mea_latitude)[0][0]

		# z1 is a masked array of size len(latitude_grid) x len(longitude_grid) containing the interpolated values.
		# Hence, we access the value at MEA's coordinates as z1[lat][long] instead of z1[long][lat].
		predicted_value = round(z1.data[index_of_mea_latitude][index_of_mea_longitude], 2)
		target_value = data.target.loc[index]['MEA']
		#print(f"The target value is: {target_value} and the predicted value is {predicted_value}", flush=True)
		#print(f"The object is of type: {type(data)}", flush=True)

		if isinstance(data, FullData):
			print("YES", flush=True)
			sites_output_df = self.build_sites_output_dataframe(index, data, full_dataset_site_names, predicted_value)
		else:
			print("NO", flush=True)
			self.sites_output_df = self.build_sites_output_dataframe(index, data, holed_dataset_site_names, predicted_value)

		# Return z1.data, sites_output_df, predicted value and target_value as a dictionary. This information will
		# be passed onto the user's browser, where is will be used to visualise the data on maps.
		return_values = {}
		return_values['prediction_grid'] = z1.data
		return_values['sites_output_df'] = sites_output_df
		return_values['predicted_value'] = predicted_value
		return_values['target_value'] = target_value
		return return_values


	def build_sites_output_dataframe(self, index, data, sites, predicted_value):
		sites_df = pd.DataFrame(columns=['site_name', 'magnetic_field_variation', 'longitude', 'latitude'])

		# Create a dataframe containing information about each site and it's magnetic field variation value
		# on the given DD-HH. This information will be visualised on a map in the browser window.
		for site in sites:
			name = site
			value = data.dataset_df[site][index]
			longitude = data.dataset_df[site + "_lon"][index]
			latitude = data.dataset_df[site + "_lat"][index]
			sites_df = sites_df.append(pd.Series([name, value, longitude, latitude], index=sites_df.columns), ignore_index=True)

		# Explicitly add a row for the MEA site as the column has been removed/is unavailable in the datasets
		name = target_columns[0] # MEA
		value = predicted_value
		longitude = mea_longitude
		latitude = mea_latitude
		sites_df = sites_df.append(pd.Series([name, value, longitude, latitude], index=sites_df.columns), ignore_index=True)
		return sites_df
