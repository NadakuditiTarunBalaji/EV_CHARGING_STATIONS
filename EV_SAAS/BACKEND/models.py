from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ChargingStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(200))
    total_chargers = db.Column(db.Integer)
    available_chargers = db.Column(db.Integer)

class QueueEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(50))
    station_id = db.Column(db.Integer, db.ForeignKey('charging_station.id'))
    status = db.Column(db.String(50), default="waiting")