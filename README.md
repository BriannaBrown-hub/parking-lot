# Parking Lot API

## Running the application

Make sure that you have docker installed

From the project directory run the following docker command to build the docker image:
`docker image build -t parking-lot .`

Next, start the container by running:
`docker run -p 5000:5000 -d parking-lot`

This command will also seed the database with the initial parking lot state.

After the docker container is running, you can visit `localhost:5000/api/ui` to view the application.

## Technologies Used

This project is a flask application written in python 3.9. In addition to flask, I utilized SQLAlchemy ORM to gain some model and relationship utilities and avoid writing raw sql. The data store is SQLite.

Additionally, this project utilizes swagger to define and visualize the API. `Connexion` is used to handle http requests. And `flask_marshmallow` is used to serialize the model data so that it plays nicely with the json based REST API.
