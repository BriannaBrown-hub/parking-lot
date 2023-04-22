# parking-lot

Parking Lot API application

# Running the application

Make sure that you have docker installed

From the project directory run the following docker command to build the docker image:
`docker image build -t parking-lot .`

Next, start the container by running:
`docker run -p 5000:5000 -d parking-lot`
