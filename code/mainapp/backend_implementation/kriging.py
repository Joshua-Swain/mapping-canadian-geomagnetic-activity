import pandas as pd
import numpy as np
import logging
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
from .filepaths import full_dataset_filepath, holed_dataset_filepath
from .canadas_coordinates import *
from .dataset_columns import *

class Kriging():

	def __init__(self, day, hour, dataset="test"):
		pass



