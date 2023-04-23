from flask import make_response, abort
from models import Spot, Vehicle, spot_schema, spots_schema

def get_all():
  spots = Spot.query.all() 

  return spots_schema.dump(spots)

def get_spot(spot_id):
  spot = Spot.query.filter(Spot.id == spot_id).one_or_none()

  if spot is not None:
    return spot_schema.dump(spot)
  else:
    abort(404, f"Spot not found for Id: {id}")

def get_lot_status():
  available_spots = Spot.query.filter(Spot.vehicle_id == None).count()

  if available_spots > 0:
    return make_response(f"There are {available_spots} available spots.", 200)
  if available_spots < 1:
    return make_response("There are no available spots.", 200)

def get_van_count():
  van_spots = Spot.query.join(Vehicle).filter(Vehicle.type == "Van").count()

  if van_spots > 0:
    return make_response(f"There are {van_spots} spots taken up by vans.", 200)
  if van_spots < 1:
    return make_response("There are no spots occupied by vans.", 200)



  





