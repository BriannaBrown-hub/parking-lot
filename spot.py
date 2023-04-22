from flask import make_response, abort
from sqlalchemy.orm import joinedload, query
from models import Spot, spot_schema, spots_schema

def get_all():
  spots = Spot.query.options(joinedload(Spot.vehicle)).all() 

  return spots_schema.dump(spots)

def get_spot(spot_id):
  spot = Spot.query.filter(Spot.id == spot_id).one_or_none()

  if spot is not None:
    return spot_schema.dump(spot)
  else:
    abort(404, f"Spot not found for Id: {id}")




  





