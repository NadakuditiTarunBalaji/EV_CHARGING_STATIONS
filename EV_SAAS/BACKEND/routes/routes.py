from flask import jsonify, request
from models import db, ChargingStation, QueueEntry
from services.queue_service import QueueService
def register_routes(app):

    @app.route("/")
    def home():
        return jsonify({"message": "Smart EV SaaS Backend Running"})

    @app.route("/stations", methods=["GET"])
    def get_stations():
        stations = ChargingStation.query.all()

        result = []
        for s in stations:
            result.append({
                "id": s.id,
                "name": s.name,
                "location": s.location,
                "available_chargers": s.available_chargers
            })

        return jsonify(result)

    @app.route("/queue", methods=["POST"])
    def add_queue():
        data = request.json

        entry = QueueService.add_to_queue(
            data["vehicle_number"],
            data["station_id"]
        )

        return {"message": "Added", "id": entry.id}
    @app.route("/allocate/<int:station_id>", methods=["POST"])
    def allocate(station_id):

        result = QueueService.assign_charger(station_id)

        return result
    @app.route("/wait/<int:station_id>")
    def wait(station_id):

        return {
            "estimated_wait_time": QueueService.estimate_wait_time(station_id)
        }