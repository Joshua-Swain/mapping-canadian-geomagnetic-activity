import pandas as pd
import numpy as np
import logging
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
from .filepaths import full_dataset_filepath, holed_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import *

class Kriging():

	def __init__(self, index, data):
		self.moving_avg_size = 2
		self.data_moving_avg = self.calculate_moving_average(data)
		self.perform_kriging(index, data)


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
		print(f"The actual value is: {data.target.loc[index]['MEA']}", flush=True)
		print(f"The predicted value is: {predicted_value}", flush=True)
		print(f"The object is of type: {type(data)}", flush=True)







