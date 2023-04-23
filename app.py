import os
from flask import render_template
import config
from models import Spot

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route("/")
def home():
    available_spots = Spot.query.filter(Spot.vehicle_id == None).count()
    return render_template("index.html", available_spots=available_spots)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
