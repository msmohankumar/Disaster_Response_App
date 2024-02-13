Disaster Response Pipeline Project
Overview
This project is a disaster response pipeline that classifies messages based on their content to help disaster relief agencies respond more effectively. The project includes a web app where emergency workers can input new messages and see the categories they belong to.

Getting Started
Clone this repository to your local machine.
Create a Python virtual environment and activate it.
Install the required packages by running pip install -r requirements.txt.
Download the disaster response data from the Udacity workspace and place it in the data directory.
Run python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db to process the data.
Run python run.py to start the web app.
Open your web browser and navigate to http://localhost:3001 to see the web app.
Files
app: contains the Flask app for the web app.
data: contains the data processing script and the disaster response data.
models: contains the machine learning model.
requirements.txt: lists the required packages.
run.py: starts the web app.
Model
The machine learning model used in this project is a Naive Bayes classifier. It was trained on the disaster response data and can classify messages into 36 categories.

Web App
The web app allows emergency workers to input new messages and see the categories they belong to. The app also displays visualizations of the data to help workers understand the types of messages being sent during disasters.

Acknowledgements
This project was created as part of the Udacity Data Science Nanodegree program. The disaster response data was provided by Figure Eight.
