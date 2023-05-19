from app.database import connection


def log_flight(flight, positions, velocities):
    with connection.cursor() as db:
        query = f"INSERT INTO flight_logs (device_code, start_time, total_time) VALUES ({flight.to_values()}) RETURNING *;"
        db.execute(query)
        row = db.fetchone()
        connection.commit()
        log_pos_values(row[0], positions)
        log_vel_values(row[0], velocities)


def log_pos_values(flight_id: int, positions):
    with connection.cursor() as db:
        query = f"CREATE TABLE IF NOT EXISTS pos_{flight_id} (uuid SERIAL PRIMARY KEY, lat decimal NOT NULL, lon decimal NOT NULL, alt decimal NOT NULL);"
        db.execute(query)
        values = ""
        for pos in positions:
            values += f"({pos.get_lat()}, {pos.get_lon()}, {pos.get_alt()}), "
        query = f"INSERT INTO pos_{flight_id} (lat, lon, alt) VALUES {values[:-2]}"
        db.execute(query)
        connection.commit()

def log_vel_values(flight_id: int, velocities):
    with connection.cursor() as db:
        query = f"CREATE TABLE IF NOT EXISTS vel_{flight_id} (uuid SERIAL PRIMARY KEY, x decimal NOT NULL, y decimal NOT NULL, z decimal NOT NULL);"
        db.execute(query)
        values = ""
        for vel in velocities:
            values += f"({vel.get_x()}, {vel.get_y()}, {vel.get_z()}), "
        query = f"INSERT INTO vel_{flight_id} (x, y, z) VALUES {values[:-2]}"
        db.execute(query)
        connection.commit()

