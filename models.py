from datetime import datetime
from config import db, ma


class Vehicle(db.Model):
    __tablename__ = "vehicle"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    spot_id = db.Column(db.Integer, db.ForeignKey("spot.id"))


class VehicleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vehicle
        load_instance = True
        sqla_session = db.session
        include_fk = True


class Spot(db.Model):
    __tablename__ = "spot"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(32))
    vehicle = db.relationship(
        Vehicle,
        backref="spot"
    )

class SpotSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Spot
        load_instance = True
        sqla_session = db.session
        include_relationships = True

spot_schema = SpotSchema()
spots_schema = SpotSchema(many=True)

vehicle_schema = VehicleSchema()
