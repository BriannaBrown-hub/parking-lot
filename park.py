from flask import make_response, abort
from config import db
from models import Vehicle, Spot


def consecutive_car_spots(spot_ids):
    # first make sure the spots are sorted in ascending order
    sorted_spots = sorted(set(spot_ids))
    # instantiate a sub list of consecutive spots with the first spot
    grouped = [[sorted_spots[0]]]

    # utilize negative indexing to determine if the current value
    # is consecutive to the last value added to the last sub list
    # otherwise create a new sub list with the current value
    for value in sorted_spots[1:]:
        if value == grouped[-1][-1] + 1:
            grouped[-1].append(value)
        else:
            grouped.append([value])

    three_consecutive_spots = list(filter(lambda spots: len(spots) >= 3, grouped))

    return three_consecutive_spots[0][:3] if three_consecutive_spots != [] else []


def park_van():
    available_van_spot = (
        Spot.query.filter(Spot.vehicle_id == None).filter(Spot.type == "van").first()
    )

    if available_van_spot is None:
        available_car_spots = Spot.query.filter(Spot.vehicle_id == None).filter(
            Spot.type == "car"
        )
        available_spot_ids = list(map(lambda spot: spot.id, available_car_spots))

        consecutive_spots = consecutive_car_spots(available_spot_ids)

        if consecutive_spots == []:
            abort(404, f"There is no spot available for a van atm")

    return (
        [available_van_spot]
        if available_van_spot is not None
        else available_car_spots.filter(Spot.id.in_(consecutive_spots)).all()
    )


def park_car():
    available_car_spot = (
        Spot.query.filter(Spot.vehicle_id == None)
        .filter(Spot.type != "motorcycle")
        .first()
    )

    if available_car_spot is None:
        abort(404, f"There is no spot available for a car atm")

    return [available_car_spot]


def park(vehicle_type):
    available_spots = Spot.query.filter(Spot.vehicle_id == None).order_by(Spot.id.asc())

    if available_spots.count() == 0:
        abort(404, f"There is no spot available atm")

    if vehicle_type == "Van":
        spots = park_van()
    elif vehicle_type == "Car":
        spots = park_car()
    else:
        spots = [available_spots[0]]

    new_vehicle = Vehicle(type=vehicle_type)
    db.session.add(new_vehicle)

    new_vehicle.spots.extend(spots)
    db.session.commit()

    return make_response(
        f"{vehicle_type} parked in the following spot(s): {spots}", 200
    )


def unpark(vehicle_id):
    vehicle = Vehicle.query.filter(Vehicle.id == vehicle_id).one_or_none()

    if vehicle is None:
        abort(404, f"Vehicle not found for Id: {vehicle_id}")

    db.session.delete(vehicle)
    db.session.commit()

    return make_response(f"{vehicle_id} left the lot", 200)
