# flight-tracker
A flight tracker app for logging paramoter flights.

## Key Features
- Altitude tracking
- Speed tracking
- Flight path tracking
- Pre/post-flight Notes
- Login authentication

## API

### Short description of work
The API needs to be able to recieve the data sent from the field device and perform
any formatting and processing on that data. The data should include altitude, velocity
on each axis (X, Y, Z), free-fall detection, and GPS data. The API should have routes for the client
to get each piece of data formatted and processed.

### Endpoints

#### altitude
- Sample json: { altitude: '124' }
- GET altitude/
- POST altitude/

#### gps
- Sample json: {}
- GET gps/
- POST gps/

#### velocity (ft/s)
- Sample json: { x: '620', y: '43', z: '4' }
- GET velocity/
- POST velocity/
