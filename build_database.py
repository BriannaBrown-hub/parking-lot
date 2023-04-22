from config import app, db
from models import Spot

SPOTS = [
    {
      "id": 1,
      "type": "car"
    },
    {
      "id": 2,
      "type": "car"
    },
    {
      "id": 3,
      "type": "car"
    },
    {
      "id": 4,
      "type": "car"
    },
    {
      "id": 5,
      "type": "car"
    },
    {
      "id": 6,
      "type": "car"
    },
    {
      "id": 7,
      "type": "car"
    },
    {
      "id": 8,
      "type": "van"
    },
    {
      "id": 9,
      "type": "van"
    },
    {
      "id": 10,
      "type": "van"
    }
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for spot in SPOTS:
        s = Spot(id=spot["id"], type=spot["type"])
        db.session.add(s)
    db.session.commit()

