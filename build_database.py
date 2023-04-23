from config import app, db
from models import Spot

SPOTS = [
    {"id": 1, "type": "motorcycle", "vehicle_id": None},
    {"id": 2, "type": "motorcycle", "vehicle_id": None},
    {"id": 3, "type": "car", "vehicle_id": None},
    {"id": 4, "type": "car", "vehicle_id": None},
    {"id": 5, "type": "car", "vehicle_id": None},
    {"id": 6, "type": "car", "vehicle_id": None},
    {"id": 7, "type": "car", "vehicle_id": None},
    {"id": 8, "type": "van", "vehicle_id": None},
    {"id": 9, "type": "van", "vehicle_id": None},
    {"id": 10, "type": "van", "vehicle_id": None},
]

with app.app_context():
    db.drop_all()
    db.create_all()
    for spot in SPOTS:
        s = Spot(id=spot["id"], type=spot["type"])
        db.session.add(s)
    db.session.commit()
