# # Import the dependencies.

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

import datetime as dt


# #################################################
# # Database Setup
# Create a reference to the file.
# database_path = Path("/Resources/hawaii.sqlite")

# engine = create_engine(f"sqlite:///{database_path}",echo=False)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# #################################################

# # # # reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# # Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


# Calculate the latest date and previous one year date
def latest_date():
    latest_date = session.query(Measurement.date).order_by(
        Measurement.date.desc()).first()
    one_year = dt.datetime.strptime(
        one_year, "%Y-%m-%d") - dt.timedelta(days=365)
    return (one_year)


# #################################################
# # Flask Setup
# #################################################
# # Create an app, being sure to pass __name__
app = Flask(__name__)


# #################################################
# # Flask Routes
# #################################################

@app.route("/")
def homepage():
    """List all available api routes"""
    return (
        f"<h1>Welcome Hawaii climate app</h1><br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#  Explore: precipitation


@app.route("/api/v1.0/precipitation")
def Precipitation():
    one_year = latest_date()
    precipt_results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year).all()
    # change to dict for json prep
    precipt_results = dict(precipt_results)
    return jsonify(precipt_results)

# Explore: stations to return JSON list for station


@app.route("/api/v1.0/stations")
def stations():
    station = session.query(Station.station).all()
    station_data = list(np.ravel(station_data))
    return jsonify(station_data)

# Explore: to get  JSON of Temperature Observations


@app.route("/api/v1.0/tobs")
def tobs():
    tobs_results = session.query(Measurement.date, Measurement.station, Measurement.tobs).\
        filter(Measurement.date >= one_year).all()
    tobs_ = list(tobs_results)
    return jsonify(tobs_results)

# Explore: calculation MIN, AVG, and MAX for for dates greater than/equal  start date.


@app.route("/api/v1.0/start")
def startdate(date):
    startdate_temp = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= date).all()
    return jsonify(startdate_temp)


# Explore: calculation MIN, AVG, and MAX for for dates greater than/equal  start to end date.

@app.route("/api/v1.0/startend")
def startDateEndDate(start, end):
    startEnd_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start, Measurement.date <= end).all()
    startEndresults = list(np.ravel(startEnd_results))
    return jsonify(startEndresults)


# if __name__ == "__main__":
#     app.run(debug=True)
