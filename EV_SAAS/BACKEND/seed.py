from app import app
from models import db, ChargingStation

with app.app_context():

    db.create_all()

    station1 = ChargingStation(
        name="Chennai EV Hub",
        location="Chennai",
        total_chargers=10,
        available_chargers=5
    )

    db.session.add(station1)
    db.session.commit()

    print("Seed done")