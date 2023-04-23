
from flask import make_response, abort
from config import db
from models import Vehicle, Spot

def consecutive_car_spots(spot_ids):
  sort_spots = sorted(set(spot_ids))
  gaps = [[start, end] for start, end in zip(sort_spots, sort_spots[1:]) if start + 1 < end]

  if len(gaps) == 0:
    return sort_spots[:3] if len(sort_spots) >= 3 else []

  consecutive_spots = []
  previous_gap = 0

  for gap in gaps:
    consecutive_spots = sort_spots[previous_gap:gap + 1]
    consecutive_spots.append(consecutive_spots) if consecutive_spots.length >= 3 else None
    previous_gap = gap
  
  return consecutive_spots[0] if consecutive_spots.length >= 1 else []


def park(vehicle_type):
  available_spots = Spot.query.filter(Spot.vehicle_id == None)

  if available_spots.count() == 0:
    abort(404, f"There is no spot available atm")

  if vehicle_type == "Van":
    available_van_spot = Spot.query.filter(Spot.vehicle_id == None).filter(Spot.type == "van").first()

    if available_van_spot is None:
      available_spot_ids = list(map(lambda spot: spot.id, available_spots))
      
      consecutive_spots = consecutive_car_spots(available_spot_ids)

      if consecutive_spots == []:
          abort(404, f"There is no spot available for a van atm")

    spots = [available_van_spot] if available_van_spot is not None else available_spots.filter(Spot.id.in_(consecutive_spots)).all()

  else:
    spots = [available_spots[0]]

  new_vehicle = Vehicle(type=vehicle_type)
  db.session.add(new_vehicle)

  new_vehicle.spots.extend(spots)
  db.session.commit()


  return make_response(f"{vehicle_type} parked in the following spot(s): {spots}", 200)

def unpark(vehicle_id):
  vehicle = Vehicle.query.filter(Vehicle.id == vehicle_id).one_or_none()

  if vehicle is None:
    abort(404, f"Vehicle not found for Id: {vehicle_id}")

  db.session.delete(vehicle)
  db.session.commit()

  return make_response(f"{vehicle_id} left the lot", 200)
