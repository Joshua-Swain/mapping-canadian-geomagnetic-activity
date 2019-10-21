# CSA Challenge 2: Mapping the variation of the Earth's magnetic field

## Team Name: Magneto AI

## Team Members
|			Name        				|   Email ID   					| Organisation				|
| --------------------------------------|-------------------------------|---------------------------|
| Joshua Swain		      				| joshua.thomas.swain@dal.ca 	|Dalhousie University	 	|
| Vismay Revankar      					| vismayhr@hotmail.com 		    |Dalhousie University		|
| Jivitesh Gudekar 						| gudekar.jivitesh@gmail.com    |Dalhousie University 		|
| Sabareeshnath Kadamgode Puthenveedu 	| sabareeshnathkp@gmail.com     |Saint Mary's University 	|
| Abdul Basit Syed		 				| ab652165@dal.ca     			|Dalhousie University 		|

## Project Structure
* **[data/](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/data)** : This folder contains the raw (txt) and cleaned (csv) datasets.
* **[output/](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/output)** : This folder contains the outputs generated by the script. The plots generated are stored in [output/plots](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/output/plots). The complete list of predictions for the test dataset can be found in the file [output/prediction/predictions.txt](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/blob/master/output/prediction/predictions.txt).
* **[ppt](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/ppt)** : This folder contains the PPT we presented to describe our solution at the end of the NASA Spaceapps Hackathon (Halifax).
* **[src](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/src)** : This folder contains the source code of the project in the form of Python notebooks.

## Executing the code
### Dependencies
The dependencies required to run the [MagnetoAI_GoCanada_Challenge2_Code python notebook](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/blob/master/src/MagnetoAI_GoCanada_Challenge2_Code.ipynb) are:
* pandas
* numpy
* pykrige
* folium
* webbrowser

### Execution steps and output
1. Open the python notebook (.ipynb) in a Jupyter Lab/Anaconda Navigator or any other application.<br>
2. Run all the cells in order
3. If you set the flags as 'test' and 'False' in the last cell, then just running the cell will generate the required outputs in [output/prediction](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/output/prediction).
4. Any other settings of the flags will prompt you to provide a day number and hour in the form of DD-HH. Valid day values are 1-31, and valid hour values are 1-24. Once you enter the input, 2 browser windows tabs will be opened. These tabs will containing the spatial visualisation of magnetic field variations at the [specific magnetometer sites](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/output/plots/sites) and also [across Canada](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/output/plots/across_canada).
5. If you wish to run the scripts used for data cleaning, you can repeat steps 1 and 2 for the python notebooks in [this folder](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/src/data_cleaning_scripts).

## Presentation (PPT)
The PPT can be found [here](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/master/ppt).
