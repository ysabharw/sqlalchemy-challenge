#please note that app.py has been made WITH THE HELP XPERT LEARNING ASSISTANT AS MY ORIGNAL CODE WAS NOT FETCHING HAWALL.SQLITE 
# IT WAS CORRUPTING THE FILE RECURSIVELY THEREFORE THE USE OF XPERT LEARNING ASSISTANT, STACKOVERFLOW, GEEKS4GEEKS 
# WAS ABSOLUTELY NECESSARY 
#  
# # Import the dependencies.
import numpy as np
import pandas as pd

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

#################################################
# Database Setup
#################################################
# Create the engine to connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables using the autoload_with parameter
Base.prepare(autoload_with=engine)

# Save references to each table
try:
    Measurement = Base.classes.measurement
    Station = Base.classes.station
except AttributeError as e:
    print(f"Error accessing table classes: {e}")

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define the homepage route
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query the last 12 months of precipitation data
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Retrieve date and precipitation data
    precip_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a dictionary
    precip_dict = {date: prcp for date, prcp in precip_data}

    # Return the JSON representation of the dictionary
    return jsonify(precip_dict)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query all the stations from the dataset
    stations_data = session.query(Station.station).all()

    # Convert the query results to a list
    stations_list = list(np.ravel(stations_data))

    # Return the JSON list of stations
    return jsonify(stations_list)

# TOBS route
@app.route("/api/v1.0/tobs")
def tobs():
    # Find the most active station
    most_active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0]

    # Query the last 12 months of temperature data for the most active station
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, '%Y-%m-%d')
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    tobs_data = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_station).filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a list
    tobs_list = list(np.ravel(tobs_data))

    # Return the JSON list of temperature observations (TOBS)
    return jsonify(tobs_list)

# Start date route
@app.route("/api/v1.0/<start>")
def start(start):
    # Query for the minimum, average, and maximum temperature for dates greater than or equal to the start date
    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    
    # Unravel the results into a list
    temp_data = list(np.ravel(results))

    # Return the results as JSON
    return jsonify(temp_data)

# Start-End date route
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Query for the minimum, average, and maximum temperature between the start and end date
    results = session.query(func.min(Measurement.tobs), 
                            func.avg(Measurement.tobs), 
                            func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Unravel the results into a list
    temp_data = list(np.ravel(results))

    # Return the results as JSON
    return jsonify(temp_data)

if __name__ == "__main__":
    app.run(debug=True)
