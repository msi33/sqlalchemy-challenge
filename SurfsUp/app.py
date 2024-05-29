# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

from flask import Flask, jsonify
import datetime as dt


# #################################################
# # Database Setup
# engine = create_engine("sqlite:///../Resources/hawaii.sqlite", echo=False)

# #################################################


# # # # reflect an existing database into a new model
# Base = automap_base()
# Base.prepare(autoload_with=engine)
# Base.prepare(engine, reflect=True)
# # # Base.classes.keys()


# # reflect the tables
# Base.prepare(autoload_with=engine)
# # Dow = Base.classes.dow


# # Reflect Database into ORM classes
# Base = automap_base()
# Base.prepare(autoload_with=engine)
# Base.classes.keys()


# # Save references to each table
# Measurement = Base.classes.measurement
# Station = Base.classes.station


# # Create our session (link) from Python to the DB


# #################################################
# # Flask Setup
# #################################################
# from flask import Flask

# # 2. Create an app, being sure to pass __name__
# app = Flask(__name__)


# # 3. Define what to do when a user hits the index route
# @app.route("/")
# def welcome():
#     """List all available api routes"""
#     return(
#         f"Available Routes:<br/>"
#         f"/api/v1.0/precipitation<br/>"
#         f"/api/v1.0/stations<br/>"
#         f"/api/v1.0/tobs<br/>"
#         f"/api/v1.0/<start><br/>"
#         f"/api/v1.0/<start>/<end><br/>"
#     )

# @app.route("/")
# def home():
#     print("Server received request for 'Home' page...")
#     return "Welcome to my 'Home' page!"

# if __name__ == "__main__":
#     app.run(debug=True)


# #################################################
# # Flask Routes
# #################################################
