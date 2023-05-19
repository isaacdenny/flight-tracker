CREATE TABLE IF NOT EXISTS users (
  uuid SERIAL PRIMARY KEY,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(100) NOT NULL,
  device_code VARCHAR(7) NOT NULL,
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS flight_logs (
  uuid SERIAL PRIMARY KEY,
  device_code VARCHAR(7) NOT NULL,
  start_time decimal NOT NULL,
  total_time decimal NOT NULL,
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS devices (
  uuid SERIAL PRIMARY KEY,
  serial_number VARCHAR(255) NOT NULL UNIQUE,
  ip_address VARCHAR(255) NOT NULL,
  device_name VARCHAR(100) NOT NULL,
  device_code VARCHAR(7) NOT NULL UNIQUE,
  createdAt TIMESTAMP DEFAULT now(),
  updatedAt TIMESTAMP DEFAULT now()
);

CREATE TABLE IF NOT EXISTS known_serials (
  uuid SERIAL PRIMARY KEY,
  serial_number VARCHAR(255) NOT NULL UNIQUE,
  device_code VARCHAR(7) NOT NULL UNIQUE
);

INSERT INTO known_serials (serial_number, device_code) VALUES ('21AH250C99EV34', 'AE45980');