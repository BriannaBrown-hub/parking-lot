import os
from flask import render_template
import config

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)