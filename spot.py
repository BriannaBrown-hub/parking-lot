from flask import make_response, abort
from models import Spot, spot_schema, spots_schema

def get_spot(id):
  spot = Spot.query.filter(Spot.id == id).one_or_none()

  if spot is not None:
    return spot_schema.dump(spot)
  else:
    abort(404, f"Spot not found for Id: {id}")

def seed( ):
  spots = Spot.query.all()

  if len(spots) == 0:
    for i in range(1, 7):
      spot = Spot(id=i, type="car")
      spot.save()

    for i in range(3, 11):
      spot = Spot(id=i, type="van")
      spot.save()

    return make_response(f"Spots seeded successfully", 200)
  else:
    abort(
      400, f"Spots already seeded"
    )



  





