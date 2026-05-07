from datetime import datetime
from models import db, QueueEntry, ChargingStation


class QueueService:

    # ---------------- ADD TO QUEUE ----------------
    @staticmethod
    def add_to_queue(vehicle_number, station_id):
        entry = QueueEntry(
            vehicle_number=vehicle_number,
            station_id=station_id,
            status="waiting",
            arrival_time=datetime.utcnow()
        )

        db.session.add(entry)
        db.session.commit()

        return entry


    # ---------------- GET QUEUE ----------------
    @staticmethod
    def get_queue(station_id):
        return QueueEntry.query.filter_by(
            station_id=station_id,
            status="waiting"
        ).order_by(QueueEntry.arrival_time).all()


    # ---------------- NEXT VEHICLE ----------------
    @staticmethod
    def get_next_vehicle(station_id):
        return QueueEntry.query.filter_by(
            station_id=station_id,
            status="waiting"
        ).order_by(QueueEntry.arrival_time).first()


    # ---------------- ASSIGN CHARGER ----------------
    @staticmethod
    def assign_charger(station_id):

        station = ChargingStation.query.get(station_id)

        if not station:
            return {"error": "Station not found"}

        if station.available_chargers <= 0:
            return {"error": "No chargers available"}

        next_vehicle = QueueService.get_next_vehicle(station_id)

        if not next_vehicle:
            return {"error": "Queue is empty"}

        # allocate charger
        next_vehicle.status = "charging"
        station.available_chargers -= 1

        db.session.commit()

        return {
            "vehicle_number": next_vehicle.vehicle_number,
            "status": "assigned"
        }


    # ---------------- COMPLETE CHARGING ----------------
    @staticmethod
    def complete_charging(queue_id, station_id):

        entry = QueueEntry.query.get(queue_id)
        station = ChargingStation.query.get(station_id)

        if not entry:
            return {"error": "Queue entry not found"}

        entry.status = "completed"
        station.available_chargers += 1

        db.session.commit()

        return {"message": "Charging completed"}


    # ---------------- WAIT TIME ESTIMATE ----------------
    @staticmethod
    def estimate_wait_time(station_id, avg_time_per_vehicle=25):

        queue_length = QueueEntry.query.filter_by(
            station_id=station_id,
            status="waiting"
        ).count()

        return queue_length * avg_time_per_vehicle