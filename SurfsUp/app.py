# Import the dependencies.
from flask import Flask, jsonify
import numpy as np
from pathlib import Path
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


import datetime as dt


# #################################################
# # Database Setup
# Create a reference to the file.
# database_path = Path("/Resources/hawaii.sqlite")

# engine = create_engine(f"sqlite:///{database_path}",echo=False)
engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

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


# #################################################
# # Flask Setup
# #################################################
# from flask import Flask
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

#  Explore: /api/v1.0/precipitation


@app.route("/")
def Precipitation():
    latest_date = session.query(func.max(Measurement.date))
    latest_date = dt.datetime.strptime(lastdate, "%Y-%m-%d").date()
    begin_date = latest_date - dt.timedelta(days=365)
    begin_date = begin_date.strftime("%Y-%m-%d")
    over_ayeardata = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date.between(begin_date, latest_date)).all()

    precipts = []
    for date, precipts in over_ayeardata:
        precipts_dict = {}
        precipts_dict['date'] = date
        precipts_dict['prcp'] = prcp
        precipts.append(precipts_dict)
    return jsonify(precipts)

# Explore: /api/v1.0/stations to return JSON list for station


@app.route("/")
def stations():

    station_data = session.query(Station.Name).all()
    station_data = list(np.ravel(station_data))
    return jsonify(station_data)


# # Explore: /api/v1.0/stations
# @app.route("/api/v1.0/stations")
# def stations():
#     station_data = session.query(Station.station, Station.name).all()
#     return jsonify(station_data)

# # Explore:/api/v1.0/tobs
# @app.route("/api/v1.0/tobs")
# def tobs():
#     tobs_data = session.query(Measurement.date, Measurement.station, Measurement.tobs).filter(Measurement.date >= last_twelve_months).all()
#     return jsonify(tobs_data)

 # Date 12 months ago


# if __name__ == "__main__":
#     app.run(debug=True)
