# flight-tracker
A flight tracker app for logging paramoter flights.

## Key Features
- live Altitude, Speed, Position tracking
- Flight logs with flight path, pre/post-flight Notes, and videos/pictures
- Past flight logs available on user account

## API

### Short description of work
The API needs to be able to recieve the data sent from the field device and perform
any formatting and processing on that data. The data should include altitude, velocity
on each axis (X, Y, Z), free-fall detection, and GPS data. The API should have routes for the client
to get each piece of data formatted and processed.

### Live Flight Endpoints

#### live flights
- GET live/{uuid}
- POST live/{uuid}/start start flight
- POST live/{uuid}/end end flight

#### in-flight data (prefixed by live flights)
- Sample json: { altitude: '124' }
- GET inflight/ { 'uuid': 1123, 'in_flight': True, 'start_time': 160908.999, 'total_time': 45.446 }

#### position
- Sample json: { 'lat': 40.009, 'lon': -77.0089, 'alt': 234 }
- GET position/
- POST position/

#### velocity (ft/s)
- Sample json: { 'x': 620, 'y': 43, 'z': 4 }
- GET velocity/
- POST velocity/

### User Endpoints

#### users
- GET users/{uuid}
- POST users/

#### logs
- GET logs/{uuid}
- GET logs/{user_id} all logs for a user
- POST logs/{uuid}

