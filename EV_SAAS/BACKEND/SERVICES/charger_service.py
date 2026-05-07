from models import db, ChargingSlot, ChargingStation


class ChargerService:

    # ---------------- GET STATION STATUS ----------------
    @staticmethod
    def get_station_status(station_id):

        station = ChargingStation.query.get(station_id)

        if not station:
            return {"error": "Station not found"}

        total_slots = ChargingSlot.query.filter_by(
            station_id=station_id
        ).count()

        available_slots = ChargingSlot.query.filter_by(
            station_id=station_id,
            status="available"
        ).count()

        occupied_slots = total_slots - available_slots

        return {
            "station_id": station_id,
            "total_slots": total_slots,
            "available_slots": available_slots,
            "occupied_slots": occupied_slots
        }


    # ---------------- ASSIGN ANY AVAILABLE CHARGER ----------------
    @staticmethod
    def assign_any_available_slot(station_id, vehicle_number):

        slot = ChargingSlot.query.filter_by(
            station_id=station_id,
            status="available"
        ).order_by(ChargingSlot.slot_number).first()

        if not slot:
            return {"error": "No available chargers"}

        slot.status = "occupied"
        slot.vehicle_number = vehicle_number

        db.session.commit()

        return {
            "message": "Slot assigned",
            "slot_number": slot.slot_number,
            "vehicle_number": vehicle_number
        }


    # ---------------- RELEASE CHARGER ----------------
    @staticmethod
    def release_slot(station_id, slot_number):

        slot = ChargingSlot.query.filter_by(
            station_id=station_id,
            slot_number=slot_number
        ).first()

        if not slot:
            return {"error": "Slot not found"}

        slot.status = "available"
        slot.vehicle_number = None
        slot.start_time = None

        db.session.commit()

        return {
            "message": f"Slot {slot_number} released"
        }


    # ---------------- AUTO BALANCER (HYBRID SUPPORT) ----------------
    @staticmethod
    def auto_allocate(station_id, vehicle_number):

        available = ChargingSlot.query.filter_by(
            station_id=station_id,
            status="available"
        ).count()

        if available > 0:
            return ChargerService.assign_any_available_slot(
                station_id,
                vehicle_number
            )

        return {
            "message": "No chargers available. Add to queue.",
            "status": "queued"
        }