# CSA GO Canada Challenge 2: Mapping Canadian Geomagnetic Activity

## Team Name: Magneto AI

## Accessing the application
The application is hosted on the cloud (Heroku) and can be accessed here: [http://team-magnetoai-csa-challenge.herokuapp.com/magnetic-field-canada](http://team-magnetoai-csa-challenge.herokuapp.com/magnetic-field-canada).

## What is this application?
This application was built as a solution to the GO Canada challenge #2 posed by the Canadian Space Agency (CSA) during NASA SpaceApps 2019. Our solution won the regional competition in Halifax, Nova Scotia, recognized [here](https://twitter.com/SpaceAppsHFX/status/1186023504472367106).<br><br>
We have developed a web application that visualizes the maximum variation in geomagnetic fields at given observatories. Using this data, we interpolate the magnetic field variation at the missing site (MEA – marked in red). Also, the application displays a second map that shows a heat map of Canada’s geomagnetic variations for the given day and time. Hovering over any of the markers on the map will indicate the value of the magnetic field variation at that specific coordinate.

## Who built the application? (The Team)
Our team is name Magneto AI. The team consists of:

|			Name        |   Email ID   					| Organisation				|
| ----------------------|-------------------------------|---------------------------|
| Joshua Swain		    | joshua.thomas.swain@dal.ca 	|Dalhousie University	 	|
| Vismay Revankar      	| vismayhr@hotmail.com 		    |Dalhousie University		|
| Jivitesh Gudekar 		| gudekar.jivitesh@gmail.com    |Dalhousie University 		|
| Sabareeshnath K P 	| sabareeshnathkp@gmail.com     |Saint Mary's University 	|
| Abdul Basit Syed		| ab652165@dal.ca     			|Dalhousie University 		|

## Project Structure
* **[/backend_implementation](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/dev/code/mainapp/backend_implementation)** : This folder contains the code for the server.
* **[/data](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/dev/code/mainapp/data)** : This folder contains the Full and Holed datasets.
* **[/static](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/dev/code/mainapp/static)** : This folder contains the static content to be loaded on the HTML pages such as JavaScript code, CSS, and images.
* **[/templates](https://github.com/Joshua-Swain/mapping-canadian-geomagnetic-activity/tree/dev/code/mainapp/templates)** : The HTML pages to be rendered by the web-app are defined in this folder.

## Executing the code
### Dependencies
Since the web-app runs inside a Docker container, all code-level dependencies are taken care of. The only requirement is that the developer must have Docker installed and running on their system. The code can be built in two ways:
1. Use the Docker image available on DockerHub
2. Build from source

### From DockerHub
1. The Docker image of the web-app has been hosted in [this](https://cloud.docker.com/repository/docker/vismayhr/csa-challenge-2) DockerHub repository. Pull the image onto your computer by running `docker pull vismayhr/csa-challenge-2:latest` in the terminal/command prompt.
2. Start the application by running the Docker container using the command `docker run -p 1330:8001 vismayhr/csa-challenge-2:latest`
3. Open your browser and go to `127.0.0.1:1330/magnetic-field-canada`

### Build from source
1. Clone this repository onto your computer.
2. Navigate to the directory named code (where the Dockerfile is present).
3. Build the Docker image by executing the command `docker build -t map-canadian-magnetic-field:latest .`
4. Start the application by running the Docker container using the command `docker run -p 1330:8001 vismayhr/csa-challenge-2:latest`
5. Open your browser and go to `127.0.0.1:1330/magnetic-field-canada`
